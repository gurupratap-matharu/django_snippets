from django.shortcuts import render


def login(request):
    return render(request, 'login.html', {})


def logout(request):
    return render(request, 'login.html', {})


def index(request):
    return render(request, 'index.html', {})


def language(request):
    return render(request, 'index.html', {})


def user_snippets(request):
    return render(request, 'snippets/user_snippets.html', {})


def snippet(request):
    return render(request, 'snippets/snippet.html', {})


def snippet_add(request):
    return render(request, 'snippets/snippet_add.html', {})


def snippet_edit(request):
    return render(request, 'snippets/snippet_add.html', {})


def snippet_delete(request):
    return render(request, 'snippets/user_snippets.html', {})
