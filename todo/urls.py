from django.urls import path

from . import views

urlpatterns = [
    # path('todo/', views.index),
    path('', views.TodoListView.as_view()),
]
