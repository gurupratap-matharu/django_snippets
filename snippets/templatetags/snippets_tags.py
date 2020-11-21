from django import template
from django.utils import timezone
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

register = template.Library()


@register.filter(expects_localtime=True)
def days_since(created):
    dt = timezone.now() - created + timezone.timedelta(days=1)
    days = str(dt.days)
    return days


@register.filter()
def lexify(language, code):
    lexer = get_lexer_by_name(language, stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass="source")
    result = highlight(code, lexer, formatter)
    return mark_safe(result)
