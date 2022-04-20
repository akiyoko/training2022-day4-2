from django.urls import path

from . import views

urlpatterns = [
    # TODOリスト画面
    # path('', views.todo_list),
    path('', views.TodoListView.as_view()),
    # TODO追加画面
    path('create/', views.TodoCreateView.as_view()),
    # TODO変更画面
    path('update/<int:pk>/', views.TodoUpdateView.as_view()),
]
