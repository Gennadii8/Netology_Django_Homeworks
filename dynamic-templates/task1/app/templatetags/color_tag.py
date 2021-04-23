from django import template

register = template.Library()


@register.filter
def coloring(item):
    if item != '-':
        item = float(item)
        if item < 0:
            return 'green'
        if 1 <= item <= 2:
            return 'lightpink'
        if 2 < item <= 5:
            return 'orangered'
        if item > 5:
            return 'maroon'
        else:
            return ''
