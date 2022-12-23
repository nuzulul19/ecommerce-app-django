from django import template

register = template.Library()


@register.filter
def rupiah_format(value):
    result = ""
    str_value = str(value)
    for index, val in enumerate(str_value):
        if (index + 1) % 3 == 0 and index + 1 != len(str_value):
            result += val + "."
        else:
            result += val
    return "Rp " + result
