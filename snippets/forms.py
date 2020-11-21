import logging

from django import forms
from django.core.mail import send_mail

from snippets.models import Snippet

logger = logging.getLogger(__name__)


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['name', 'language', 'description', 'snippet', 'public']
        widget = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 3})
        }

    def send_mail(self, **kwargs):
        user_email = self.instance.user.email
        logger.info('Name: %s', self.instance.name)
        logger.info('Description: %s', self.instance.description)
        logger.info('sending snippet creation email to %s...', user_email)
        subject, message = self.instance.name, self.instance.description
        send_mail(subject=subject, message=message,
                  from_email='site@domain.com',
                  recipient_list=['gurupratap.matharu@gmail.com', user_email],
                  fail_silently=False)
