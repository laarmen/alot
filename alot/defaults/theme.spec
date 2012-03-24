[1]
[[global]]
    [[[footer]]]
        fg = string(default=None)
    [[[notify_error]]]
        fg = string(default=None)
    [[[notify_normal]]]
        fg = string(default=None)
    [[[prompt]]]
        fg = string(default=None)
    [[[tag]]]
        fg = string(default=None)
    [[[tag_focus]]]
        fg = string(default=None)
    [[[tag_draft]]]
        fg = string(default=None)
[[help]]
    [[[text]]]
        fg = string(default=None)
    [[[section]]]
        fg = string(default=None)
    [[[title]]]
        fg = string(default=None)
[[bufferlist]]
    [[[focus]]]
        fg = string(default=None)
    [[[results_even]]]
        fg = string(default=None)
    [[[results_odd]]]
        fg = string(default=None)
[[search]]
    [[[threadline]]]
        fg = string(default=None)
        fg_focus = string(default=None)
        bg = string(default=None)
        bg_focus = string(default=None)
        # order subwidgets are displayed. subset of {date,mailcount,tags,authors,subject,count}
        # every element listed must have its own subsection below
        order = string_list(default=list(date,mailcount,tags,authors,subject))
        [[[[__many__]]]]
            fg = string(default=None)
            fg_focus = string(default=None)
            bg = string(default=None)
            bg_focus = string(default=None)
            width_fixed = integer(default=None)
            width_weight = integer(default=None)
    [[[__many__]]]
        fg = string(default=None)
        fg_focus = string(default=None)
        bg = string(default=None)
        bg_focus = string(default=None)
        #condition = 'tags:foo,bar' or 'query:QUERYSTRING'
        criterion = string
        order = string_list(default=list(date,mailcount,tags,authors,subject))
        [[[[__many__]]]]
            fg = string(default=None)
            fg_focus = string(default=None)
            bg = string(default=None)
            bg_focus = string(default=None)
            width_fixed = integer(default=None)
            width_weight = integer(default=None)
[[thread]]
    [[[attachment]]]
        fg = string(default=None)
    [[[attachment_focus]]]
        fg = string(default=None)
    [[[body]]]
        fg = string(default=None)
    [[[header]]]
        fg = string(default=None)
    [[[header_key]]]
        fg = string(default=None)
    [[[header_value]]]
        fg = string(default=None)
    [[[summary_even]]]
        fg = string(default=None)
    [[[summary_focus]]]
        fg = string(default=None)
    [[[summary_odd]]]
        fg = string(default=None)

[16]
[[global]]
    [[[footer]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[notify_error]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[notify_normal]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[prompt]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[tag]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[tag_focus]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[tag_draft]]]
        bg = string(default=None)
        fg = string(default=None)
[[help]]
    [[[text]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[section]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[title]]]
        bg = string(default=None)
        fg = string(default=None)
[[bufferlist]]
    [[[focus]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[results_even]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[results_odd]]]
        bg = string(default=None)
        fg = string(default=None)
[[thread]]
    [[[attachment]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[attachment_focus]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[body]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[header]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[header_key]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[header_value]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[summary_even]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[summary_focus]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[summary_odd]]]
        bg = string(default=None)
        fg = string(default=None)
[[search]]
    [[[threadline]]]
        fg = string(default=None)
        fg_focus = string(default=None)
        bg = string(default=None)
        bg_focus = string(default=None)
        # order subwidgets are displayed. subset of {date,mailcount,tags,authors,subject,count}
        # every element listed must have its own subsection below
        order = string_list(default=list(date,mailcount,tags,authors,subject))
        [[[[__many__]]]]
            fg = string(default=None)
            fg_focus = string(default=None)
            bg = string(default=None)
            bg_focus = string(default=None)
            width_fixed = integer(default=None)
            width_weight = integer(default=None)
    [[[__many__]]]
        fg = string(default=None)
        fg_focus = string(default=None)
        bg = string(default=None)
        bg_focus = string(default=None)
        #condition = 'tags:foo,bar' or 'query:QUERYSTRING'
        criterion = string
        order = string_list(default=list(date,mailcount,tags,authors,subject))
        [[[[__many__]]]]
            fg = string(default=None)
            fg_focus = string(default=None)
            bg = string(default=None)
            bg_focus = string(default=None)
            width_fixed = integer(default=None)
            width_weight = integer(default=None)

[256]
[[global]]
    # attributes used in all modi
    [[[footer]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[notify_error]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[notify_normal]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[prompt]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[tag]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[tag_focus]]]
        bg = string(default=None)
        fg = string(default=None)
[[help]]
    # formatting of the `help bindings` overlay
    [[[text]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[section]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[title]]]
        bg = string(default=None)
        fg = string(default=None)
# mode specific attributes
[[bufferlist]]
    [[[focus]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[results_even]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[results_odd]]]
        bg = string(default=None)
        fg = string(default=None)
[[search]]
    [[[threadline]]]
        fg = string(default=None)
        fg_focus = string(default=None)
        bg = string(default=None)
        bg_focus = string(default=None)
        # order subwidgets are displayed. subset of {date,mailcount,tags,authors,subject,count}
        # every element listed must have its own subsection below
        order = string_list(default=list(date,mailcount,tags,authors,subject))
        [[[[__many__]]]]
            fg = string(default=None)
            fg_focus = string(default=None)
            bg = string(default=None)
            bg_focus = string(default=None)
            width_fixed = integer(default=None)
            width_weight = integer(default=None)
    [[[__many__]]]
        fg = string(default=None)
        fg_focus = string(default=None)
        bg = string(default=None)
        bg_focus = string(default=None)
        #condition = 'tags:foo,bar' or 'query:QUERYSTRING'
        criterion = string
        order = string_list(default=list(date,mailcount,tags,authors,subject))
        [[[[__many__]]]]
            fg = string(default=None)
            fg_focus = string(default=None)
            bg = string(default=None)
            bg_focus = string(default=None)
            width_fixed = integer(default=None)
            width_weight = integer(default=None)
[[thread]]
    [[[attachment]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[attachment_focus]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[body]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[header]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[header_key]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[header_value]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[summary_even]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[summary_focus]]]
        bg = string(default=None)
        fg = string(default=None)
    [[[summary_odd]]]
        bg = string(default=None)
        fg = string(default=None)


