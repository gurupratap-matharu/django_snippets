from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('snippets/python/', views.LanguageView.as_view(), name='language'),
    path('snippets/user/juancito/', views.UserSnippets.as_view(), name='user_snippets'),
    path('snippets/<uuid:pk>/', views.SnippetDetailView.as_view(), name='snippet_detail'),
    path('snippets/add/', views.SnippetCreate.as_view(), name='snippet_add'),
    path('snippets/<uuid:pk>/update/', views.SnippetUpdate.as_view(), name='snippet_update'),
    path('snippets/<uuid:pk>/delete/', views.SnippetDelete.as_view(), name='snippet_delete'),
]
