from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),          # مسیر اصلی (برای نمایش لیست)
    path('add/', views.add_todo, name='add_todo'),       # افزودن کار جدید
    path('delete/<int:item_id>/', views.delete_todo, name='delete_todo'), # حذف کار بر اساس ID
]
