from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<slug:language>/', views.LanguageView.as_view(), name='language'),
    path('user/<slug:user>/', views.UserSnippets.as_view(), name='user_snippets'),
    path('add/', views.SnippetCreate.as_view(), name='snippet_add'),
    path('<uuid:pk>/', views.SnippetDetailView.as_view(), name='snippet'),
    path('<uuid:pk>/edit/', views.SnippetUpdate.as_view(), name='snippet_edit'),
    path('<uuid:pk>/delete/', views.SnippetDelete.as_view(), name='snippet_delete'),
]
