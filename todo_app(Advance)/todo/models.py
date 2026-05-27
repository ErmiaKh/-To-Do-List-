from django.db import models

class TodoItem(models.Model):
    """مدل اصلی برای ذخیره آیتم‌های To-Do."""
    title = models.CharField(max_length=200, verbose_name="عنوان کار")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    status = models.CharField(
        max_length=10,
        default='Pending',  # وضعیت پیش‌فرض: Pending (در انتظار)
        choices=[
            ('Pending', 'در انتظار'),
            ('InProgress', 'در حال انجام'),
            ('Done', 'انجام شد')
        ],
        verbose_name="وضعیت کار"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
