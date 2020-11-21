import logging

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls.base import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from snippets.forms import SnippetForm
from snippets.models import Language, Snippet
from snippets.tasks import send_snippet_creation_mail

logger = logging.getLogger(__name__)


class HomePageView(ListView):
    model = Snippet
    template_name = 'home.html'
    context_object_name = 'snippet_list'
    paginate_by = 12

    def get_queryset(self):
        return super().get_queryset().filter(public=True)


class LanguageView(ListView):
    model = Snippet
    context_object_name = 'snippet_list'
    template_name = 'home.html'
    paginate_by = 12

    def get_queryset(self):
        language_slug = self.kwargs.get('language_slug')
        language = get_object_or_404(Language, slug=language_slug)
        logger.info('language: %s', language)
        return super().get_queryset().filter(language=language).filter(public=True)


class UserSnippets(ListView):
    model = Snippet
    context_object_name = 'snippet_list'
    template_name = 'snippets/user_snippets.html'
    paginate_by = 12
    filtered_user = None

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(get_user_model(), id=user_id)
        self.filtered_user = user
        logger.info('user: %s user_id: %s', user, user_id)
        queryset = super().get_queryset().filter(user=user)

        if user != self.request.user:
            queryset = queryset.filter(public=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtered_user'] = self.filtered_user
        return context


class SnippetDetailView(DetailView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'snippets/snippet_detail.html'


class SnippetCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Snippet
    form_class = SnippetForm
    template_name = 'snippets/snippet_form.html'
    success_message = "%(name)s successfully created!"

    def form_valid(self, form):
        form.instance.user = self.request.user
        subject, message, user_email = form.instance.name, form.instance.description, self.request.user.email
        logger.info('sending snippet creation email...')
        # send default django email
        form.send_mail()
        # send email with celery
        send_snippet_creation_mail(subject=subject, message=message, user_email=user_email)
        return super().form_valid(form)


class SnippetUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Snippet
    fields = ['name', 'description', 'language', 'snippet', 'public']
    template_name = 'snippets/snippet_update_form.html'
    success_message = "%(name)s successfully updated!"

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.can_update(self.request.user):
            logger.warning('Possible attack: \nuser: %s\nobj: %s', self.request.user, obj)
            raise Http404
        return obj


class SnippetDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Snippet
    template_name = 'snippets/snippet_confirm_delete.html'
    success_url = reverse_lazy('home')
    success_message = 'Snippet deleted successfully!'

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.can_delete(self.request.user):
            logger.warning('Possible attack: \nuser: %s\nobj: %s', self.request.user, obj)
            raise Http404
        return obj

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(SnippetDelete, self).delete(request, *args, **kwargs)
