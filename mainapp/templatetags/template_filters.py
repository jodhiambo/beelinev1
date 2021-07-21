# from django import template
# from django.utils.safestring import mark_safe
#
# register = template.Library()
#
# @register.filter
# def highlight_search(text, search):
#     highlighted = text.replace(search, '<span class="highlight">{}</span>'.format(search)
#     return mark_safe(highlighted)

from django import template


register = template.Library()


@register.filter
def duration(td):
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    days = hours // 24

    return '{} minutes'.format(minutes)
