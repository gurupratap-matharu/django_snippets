from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('snippets/user/<int:user_id>/', views.UserSnippets.as_view(), name='user_snippets'),
    path('snippets/<uuid:pk>/', views.SnippetDetailView.as_view(), name='snippet_detail'),
    path('snippets/add/', views.SnippetCreate.as_view(), name='snippet_add'),
    path('snippets/<uuid:pk>/update/', views.SnippetUpdate.as_view(), name='snippet_update'),
    path('snippets/<uuid:pk>/delete/', views.SnippetDelete.as_view(), name='snippet_delete'),
    path('snippets/<slug:language_slug>/', views.LanguageView.as_view(), name='language'),
]
