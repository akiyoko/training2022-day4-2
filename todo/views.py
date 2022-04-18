from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils import timezone
from django.views import View

from .models import Todo


# Step 1. はじめての画面表示
# def todo_list(request):
#     if request.method == 'GET':
#         today = timezone.localdate()
#         return HttpResponse('今日は {} です。'.format(today))


# Step 2. クラスベースで書き直す
# class TodoListView(View):
#     def get(self, request, *args, **kwargs):
#         today = timezone.localdate()
#         return HttpResponse('今日は {} です。'.format(today))


# Step 3. HTMLを使ったレスポンスを返す
# class TodoListView(View):
#     def get(self, request, *args, **kwargs):
#         today = timezone.localdate()
#         return HttpResponse("""
# <html>
# <body>
# <h1>TODOリスト</h1>
# <p>今日は {} です。</p>
# </body>
# </html>
#         """.format(today))


# # Step 4. テンプレートを使う
# class TodoListView(View):
#     def get(self, request, *args, **kwargs):
#         today = timezone.localdate()
#         context = {
#             'today': today,
#         }
#         return TemplateResponse(request, 'todo/todo_list.html', context)


# Step 5. モデルを使う
class TodoListView(View):
    def get(self, request, *args, **kwargs):
        today = timezone.localdate()
        todo_list = Todo.objects.order_by('expiration_date')
        context = {
            'today': today,
            'todo_list': todo_list,
        }
        return TemplateResponse(request, 'todo/todo_list.html', context)
