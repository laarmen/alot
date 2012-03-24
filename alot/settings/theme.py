import os
from urwid import AttrSpec, AttrSpecError

from utils import read_config
from errors import ConfigError

DEFAULTSPATH = os.path.join(os.path.dirname(__file__), '..', 'defaults')


class Theme(object):
    """Colour theme"""
    def __init__(self, path):
        """
        :param path: path to theme file
        :type path: str
        :raises: :class:`~alot.settings.errors.ConfigError`
        """
        self._spec = os.path.join(DEFAULTSPATH, 'theme.spec')
        self._config = read_config(path, self._spec)
        self.attributes = self._parse_attributes(self._config)

    def _parse_attributes(self, c):
        """
        parse a (previously validated) valid theme file
        into urwid AttrSpec attributes for internal use.

        :param c: config object for theme file
        :type c: `configobj.ConfigObj`
        :raises: `ConfigError`
        """

        attributes = {}
        for sec in c.sections:
            try:
                colours = int(sec)
            except ValueError:
                err_msg = 'section name %s is not a valid colour mode'
                raise ConfigError(err_msg % sec)
            attributes[colours] = {}
            for mode in c[sec].sections:
                attributes[colours][mode] = {}
                if mode == 'search':
                    for tline in c[sec][mode].sections:
                        attributes[colours][mode][tline] = {}
                        space = self._read_attribute(c, [mode, tline], colours)
                        attributes[colours][mode][tline]['spaces'] = space
                        for themable in c[sec][mode][tline].sections:
                            att = self._read_attribute(c,
                                                       [mode, tline, themable],
                                                       colours)
                            attributes[colours][mode][tline][themable] = att
                else:
                    for themable in c[sec][mode].sections:
                        att = self._read_attribute(c, [mode, themable],
                                                   colours)
                        attributes[colours][mode][themable] = att
        return attributes

    def _read_attribute(self, cfg, path, colours):
        bg = 'default'
        if colours != 1:
            bg = self._get_leaf_value(cfg, [str(colours)] + path + ['bg'])
            if bg == None:
                if colours == 16:
                    bg = self._get_leaf_value(cfg, ['1'] + path + ['bg'])
                else:
                    bg = self._get_leaf_value(cfg, ['16'] + path + ['bg'])
        bg = bg or 'default'

        fg = self._get_leaf_value(cfg, [str(colours)] + path + ['fg'])
        if fg == None:
            if colours == 16:
                fg = self._get_leaf_value(cfg, ['1'] + path + ['fg'])
            else:
                fg = self._get_leaf_value(cfg, ['16'] + path + ['fg'])
        fg = fg or 'default'

        try:
            att = AttrSpec(fg, bg, colours)
        except AttrSpecError, e:
            raise ConfigError(e)
        return att

    def _get_leaf_value(self, cfg, path):
        if len(path) == 1:
            if path[0] not in cfg.scalars:
                return None
            else:
                return cfg[path[0]]
        else:
            return self._get_leaf_value(cfg[path[0]], path[1:])

    def get_attribute(self, mode, name, colourmode):
        """
        returns requested attribute

        :param mode: ui-mode (e.g. `search`,`thread`...)
        :type mode: str
        :param name: identifier of the atttribute
        :type name: str
        :param colourmode: colour mode; in [1, 16, 256]
        :type colourmode: int
        """
        return self.attributes[colourmode][mode][name]
