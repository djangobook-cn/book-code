from django import template
from markdown import markdown

register = template.Library()


@register.simple_tag
def markdown2html(content):
    return markdown(content)
