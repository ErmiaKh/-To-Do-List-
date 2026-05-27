from django.http import HttpResponse
from django.shortcuts import render
from .models import TodoItem


def todo_list(request):
    # ... (کد نمایش لیست) ...
    all_items = TodoItem.objects.all().order_by('-created_at')
    output = "=======================================\n"
    output += "         📋 لیست کارهای To-Do 📋\n"
    output += "=======================================\n"

    for item in all_items:
        status_color = ""
        if item.status == 'Done':
            status_color = "\033[92m"
        elif item.status == 'InProgress':
            status_color = "\033[93m"
        else:
            status_color = "\033[91m"

        output += f"{status_color}[{item.status}] {item.title}\033[0m\n"
        if item.description:
            output += f"   توضیحات: {item.description}\n"
        output += "---------------------------------------\n"
    return HttpResponse(output)


def add_todo(request):
    # ... (کد افزودن کار - که قبلاً درست بود) ...
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        status = request.POST.get('status', 'Pending')

        if title:
            TodoItem.objects.create(
                title=title,
                description=description,
                status=status
            )
            from django.shortcuts import redirect
            return redirect('todo_list')
        else:
            return HttpResponse("❌ خطا: عنوان کار نمی‌تواند خالی باشد.", status=400)

    return render(request, 'todo/add_todo.html')
    # این مسیر باید دقیقاً با ساختار پوشه مطابقت داشته باشد.


def delete_todo(request, item_id):  # 👈 این تابع باید دقیقاً همین نام داشته باشد!
    """حذف یک آیتم کار بر اساس ID."""
    try:
        item = TodoItem.objects.get(id=item_id)
        item.delete()
        return HttpResponse(f"🗑️ موفقیت! کار '{item.title}' حذف شد.", status=200)
    except TodoItem.DoesNotExist:
        return HttpResponse("❌ خطا: آیتم مورد نظر یافت نشد.", status=404)
