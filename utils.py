import misaka

"""
Custom HTML renderer used by Flask-Misaka.

For the most part, it's just applying the class names materializecss expects.

The names for the methods it expects are described in full here:
https://github.com/FSX/misaka/blob/master/misaka/callbacks.py

e.g. for the cFFI callback `rndr_list` (from https://github.com/FSX/misaka/blob/master/misaka/hoedown/html.c) it calls: `renderer.list(content, is_ordered, is_block)` so we need to make a function called list, that accepts those arguments and returns the HTML. Easy.

"""
class MaterializeRenderer(misaka.HtmlRenderer):
    # TODO: couldn't figure out when is_block=True, or what to do in that case.
    def list(self, content, is_ordered, is_block):
        tag_name = "ol" if is_ordered else "ul"
        return "<{tag} class='collection'>{}</{tag}>".format(content, tag=tag_name, is_block=is_block)
    
    def listitem(self, content, is_ordered, is_block):
        return "<li class='collection-item'>{}</li>".format(content, is_block=is_block)
    
    def link(self, content, link, title):
        is_internal = "://kasra.date" in link
        link_target = "" if is_internal else "_blank" 
        return "<a href='{link}' target='{target}' title='{title}'>{}</a>".format(
            content, link=link, target=link_target, title=title)
