from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('snippets/python/', views.language, name='language'),
    path('snippets/user/juancito/', views.user_snippets, name='user_snippets'),
    path('snippets/snippet/', views.snippet, name='snippet'),
    path('snippets/add/', views.snippet_add, name='snippet_add'),
    path('snippets/edit/', views.snippet_edit, name='snippet_edit'),
    path('snippets/delete/', views.snippet_delete, name='snippet_delete'),
]