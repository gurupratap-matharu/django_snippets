from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('python/', views.LanguageView.as_view(), name='language'),
    path('user/juancito/', views.UserSnippets.as_view(), name='user_snippets'),
    path('snippet/<uuid:pk>/', views.SnippetDetailView.as_view(), name='snippet'),
    path('add/', views.SnippetCreate.as_view(), name='snippet_add'),
    path('<uuid:pk>/edit/', views.SnippetUpdate.as_view(), name='snippet_edit'),
    path('<uuid:pk>/delete/', views.SnippetDelete.as_view(), name='snippet_delete'),
]
