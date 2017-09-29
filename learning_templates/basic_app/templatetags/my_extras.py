from django import template


register = template.Library()

@register.filter(name='cut')    # decorator replaces statement below
def cut(value,arg):
    """
    This cuts out all values of "arg" from string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)   #   one way to do this
