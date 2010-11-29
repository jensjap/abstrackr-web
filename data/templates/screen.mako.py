# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291066762.777
_template_filename='C:\\dev\\abstrackr_web\\abstrackr\\abstrackr\\templates/screen.mako'
_template_uri='/screen.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'site.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n')
        # SOURCE LINE 2
        __M_writer(u'\r\n\r\n<div class="breadcrumbs">\r\n./<a href="')
        # SOURCE LINE 5
        __M_writer(escape(url(controller='account', action='welcome')))
        __M_writer(u'">dashboard</a>\r\n          /<a href="')
        # SOURCE LINE 6
        __M_writer(escape(url(controller='review', action='show_review', id=c.review_id)))
        __M_writer(u'">show_review</a>\r\n</div>\r\n\r\n<div id="citation" class="content" style=\'float: center\'>\r\n<h2>')
        # SOURCE LINE 10
        __M_writer(escape(c.cur_citation.title))
        __M_writer(u'</h2>\r\n')
        # SOURCE LINE 11
        __M_writer(escape(c.cur_citation.authors))
        __M_writer(u'<br/><br/>\r\n')
        # SOURCE LINE 12
        __M_writer(escape(c.cur_citation.abstract))
        __M_writer(u'\r\n</div>\r\n\r\n<center>\r\n<div id="wait"></div>\r\n</center>\r\n\r\n<script type="text/javascript">\r\n    $(document).ready(function() {\r\n\r\n        $("#accept").click(function() {\r\n            $("#wait").text("hold on to your horses..")\r\n            $("#citation").fadeOut(\'slow\', function() {\r\n                $("#citation").load("')
        # SOURCE LINE 25
        __M_writer(escape('/label/%s/%s/1' % (c.review_id, c.cur_citation.citation_id)))
        __M_writer(u'", function() {\r\n                     $("#citation").fadeIn(\'slow\');\r\n                     $("#wait").text("");\r\n                });\r\n            });\r\n         });   \r\n               \r\n        $("#maybe").click(function() {\r\n            $("#wait").text("hold on to your horses..")\r\n            $("#citation").fadeOut(\'slow\', function() {\r\n                $("#citation").load("')
        # SOURCE LINE 35
        __M_writer(escape('/label/%s/%s/0' % (c.review_id, c.cur_citation.citation_id)))
        __M_writer(u'", function() {\r\n                     $("#citation").fadeIn(\'slow\');\r\n                     $("#wait").text("");\r\n                });\r\n            });\r\n         });   \r\n        \r\n        $("#reject").click(function() {\r\n            $("#wait").text("hold on to your horses..")\r\n            $("#citation").fadeOut(\'slow\', function() {\r\n                $("#citation").load("')
        # SOURCE LINE 45
        __M_writer(escape('/label/%s/%s/-1' % (c.review_id, c.cur_citation.citation_id)))
        __M_writer(u'", function() {\r\n                     $("#citation").fadeIn(\'slow\');\r\n                     $("#wait").text("");\r\n                });\r\n            });\r\n         });  \r\n        \r\n    });\r\n</script>\r\n\r\n\r\n<br/><br/>\r\n<center>\r\n\r\n\r\n<a href="#" id="accept"><img src = "../../accept.png"/></a> \r\n<a href="#" id="maybe"><img src = "../../maybe.png"/></a> \r\n<a href="#" id="reject"><img src = "../../reject.png"/></a> \r\n\r\n</center>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'screen')
        return ''
    finally:
        context.caller_stack._pop_frame()


