from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('snippets/python/', views.LanguageView.as_view(), name='language'),
    path('snippets/user/juancito/', views.UserSnippets.as_view(), name='user_snippets'),
    path('snippets/snippet/<int:pk>/', views.SnippetDetailView.as_view(), name='snippet'),
    path('snippets/add/', views.SnippetCreate.as_view(), name='snippet_add'),
    path('snippets/edit/', views.SnippetUpdate.as_view(), name='snippet_edit'),
    path('snippets/delete/', views.SnippetDelete.as_view(), name='snippet_delete'),
]
