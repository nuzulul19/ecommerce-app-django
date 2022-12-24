from django import template

register = template.Library()


@register.filter
def rupiah_format(value):
    y = str(value)
    if len(y) <= 3:
        return "Rp " + y
    else:
        p = y[-3:]
        q = y[:-3]
        return rupiah_format(q) + "." + p
