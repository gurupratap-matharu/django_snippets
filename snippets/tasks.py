from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_snippet_creation_mail(subject, message, user_email):
    send_mail(subject=subject,
              message=message,
              from_email=['site@domain.com'],
              recipient_list=[user_email],
              fail_silently=False)
