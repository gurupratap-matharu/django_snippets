from django import template
from django.utils import timezone

register = template.Library()


@register.filter(expects_localtime=True)
def days_since(created):
    dt = timezone.now() - created + timezone.timedelta(days=1)
    days = str(dt.days)
    return days
