from django.contrib import admin
from django.urls import path, include  # 👈 باید 'include' را وارد کنیم

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')), # 👈 این خط کلیدی است! مسیر اصلی (/) را به اپلیکیشن todo می‌دهیم.
]
