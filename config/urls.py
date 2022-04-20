from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    # Note: 「/」にアクセスした場合に「/todo/」にリダイレクトする
    path('', RedirectView.as_view(url='/todo/')),
    path('todo/', include('todo.urls')),
]
