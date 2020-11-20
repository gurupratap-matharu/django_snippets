import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from snippets.models import Language, Snippet

logger = logging.getLogger(__name__)


def login(request):
    return render(request, 'login.html', {})


def logout(request):
    return render(request, 'login.html', {})


class HomePageView(ListView):
    model = Snippet
    template_name = 'home.html'
    context_object_name = 'snippet_list'
    paginate_by = 12


class LanguageView(ListView):
    model = Snippet
    context_object_name = 'snippet_list'
    template_name = 'home.html'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        language = self.request.kwargs['language']
        logger.info('language: %s', language)
        return queryset.filter(language=language)


class UserSnippets(ListView):
    model = Snippet
    context_object_name = 'snippet_list'
    template_name = 'snippets/user_snippets.html'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class SnippetDetailView(DetailView):
    model = Snippet
    context_object_name = 'snippet'
    template_name = 'snippets/snippet_detail.html'


class SnippetCreate(CreateView):
    model = Snippet
    fields = ['name', '']
    template_name = 'snippets/snippet_add.html'


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
