from django.urls import path

from . import views

urlpatterns = [
    # path('', views.todo_list),
    path('', views.TodoListView.as_view()),
    path('create/', views.TodoCreateView.as_view()),
]
