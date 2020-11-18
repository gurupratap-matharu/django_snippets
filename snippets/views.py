import logging

from django.contrib import messages
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


class IndexView(ListView):
    model = Snippet
    template_name = 'index.html'
    context_object_name = 'snippet_list'
    paginate_by = 12


class LanguageView(ListView):
    model = Snippet
    context_object_name = 'snippet_list'
    template_name = 'index.html'
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
    template_name = 'snippets/snippet.html'


class SnippetCreate(CreateView):
    model = Snippet
    template_name = 'snippets/snippet_add.html'


class SnippetUpdate(UpdateView):
    model = Snippet
    template_name = 'snippets/snippet_add.html'


class SnippetDelete(DeleteView):
    model = Snippet
    template_name = 'snippets/user_snippets.html'
    success_url = reverse_lazy('user_snippets')
    success_message = 'Snippet deleted successfully!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(SnippetDelete, self).delete(request, *args, **kwargs)
