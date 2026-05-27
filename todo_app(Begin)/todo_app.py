import csv
import os


# =============================================================================
# مرحله 1: کلاس Task (مدل‌سازی هر کار)
# =============================================================================
class Task:
    def __init__(self, name, description="", priority="متوسط"):
        """سازنده کلاس Task."""
        self.name = name
        self.description = description
        self.priority = priority  # می‌تواند "بالا"، "متوسط" یا "پایین" باشد

    def __str__(self):
        """نمایش کاربرپسند شیء Task."""
        return f"[{self.priority}] {self.name}: {self.description}"

    def to_csv_row(self):
        """بازگرداندن داده‌های کار به صورت یک لیست برای نوشتن در CSV."""
        return [self.name, self.description, self.priority]


# =============================================================================
# مرحله 2: کلاس ToDoList (مدیریت لیست)
# =============================================================================
class ToDoList:
    def __init__(self, filename="todo_tasks.csv"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()  # هنگام ساخت، سعی می‌کنیم لیست را از فایل بارگذاری کنیم

    # --- متدهای مدیریت لیست ---

    def add_task(self, name, description="", priority="متوسط"):
        """اضافه کردن یک کار جدید به لیست."""
        new_task = Task(name, description, priority)
        self.tasks.append(new_task)
        print(f"\n✅ کار '{name}' با موفقیت اضافه شد.")

    def delete_task(self, task_name):
        """حذف یک کار بر اساس نام آن."""
        initial_length = len(self.tasks)
        # فیلتر کردن لیست برای حذف کار مورد نظر
        self.tasks = [task for task in self.tasks if task.name != task_name]

        if len(self.tasks) < initial_length:
            print(f"\n🗑️ کار '{task_name}' با موفقیت حذف شد.")
        else:
            print(f"\n❌ خطا: کار با نام '{task_name}' در لیست یافت نشد.")

    def view_tasks(self):
        """نمایش تمامی کارها موجود در لیست."""
        if not self.tasks:
            print("\n📋 لیست کارها خالی است. هیچ کاری برای انجام دادن وجود ندارد!")
            return

        print("\n=============================================")
        print("✨ لیست کارها (To-Do List) ✨")
        print("=============================================")
        for index, task in enumerate(self.tasks):
            # نمایش اندیس برای راحتی کاربر در حذف (اختیاری)
            print(f"{index + 1}. {task}")
        print("=============================================")

    # --- متدهای مدیریت فایل (CSV) ---

    def save_to_csv(self):
        """ذخیره تمامی کارها در فایل CSV."""
        if not self.tasks:
            print("\n⚠️ لیست خالی است. هیچ داده‌ای برای ذخیره وجود ندارد.")
            return

        fieldnames = ['Name', 'Description', 'Priority']
        try:
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                # نوشتن هدر (عنوان ستون‌ها)
                writer.writeheader()

                # نوشتن داده‌ها
                for task in self.tasks:
                    writer.writerow(task.to_csv_row())
            print(f"\n💾 لیست کارها با موفقیت در '{self.filename}' ذخیره شد.")
        except IOError:
            print(f"\n❌ خطا هنگام نوشتن فایل CSV: دسترسی به سیستم فایل مسدود است.")

    def load_tasks(self):
        """بارگذاری لیست کارها از فایل CSV."""
        if not os.path.exists(self.filename):
            print(f"\nℹ️ فایل '{self.filename}' یافت نشد. شروع با یک لیست خالی.")
            return

        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                loaded_tasks = []
                for row in reader:
                    # تبدیل داده‌های خوانده شده به شیء Task
                    task = Task(
                        name=row['Name'],
                        description=row['Description'],
                        priority=row['Priority']
                    )
                    loaded_tasks.append(task)
                self.tasks = loaded_tasks
            print(f"✅ لیست کارها از '{self.filename}' با موفقیت بارگذاری شد.")
        except Exception as e:
            print(f"\n❌ خطا هنگام بارگذاری فایل CSV: {e}. شروع با لیست خالی.")
            self.tasks = []


# =============================================================================
# مرحله 3: منوی اصلی (تعامل کاربر)
# =============================================================================

def display_menu():
    """نمایش منوی تعاملی."""
    print("\n" + "=" * 40)
    print("       📝 مدیریت لیست کارها (To-Do List)")
    print("=" * 40)
    print("1. اضافه کردن کار جدید")
    print("2. مشاهده لیست کارها")
    print("3. حذف کار")
    print("4. ذخیره لیست در فایل CSV")
    print("5. خروج از برنامه")
    print("-" * 40)


def main():
    # ایجاد نمونه ToDoList با نام فایل پیش‌فرض
    todo_manager = ToDoList()

    while True:
        display_menu()
        choice = input("انتخاب خود را وارد کنید (1-5): ")

        if choice == '1':
            name = input("نام کار جدید: ")
            desc = input("توضیحات (اختیاری): ")
            priority = input("اولویت (بالا/متوسط/پایین) [پیش‌فرض متوسط]: ") or "متوسط"
            todo_manager.add_task(name, desc, priority)

        elif choice == '2':
            todo_manager.view_tasks()

        elif choice == '3':
            if todo_manager.tasks:
                task_to_delete = input("نام کاری که می‌خواهید حذف کنید: ")
                todo_manager.delete_task(task_to_delete)
            else:
                print("\n⚠️ لیست کارها خالی است.")

        elif choice == '4':
            todo_manager.save_to_csv()

        elif choice == '5':
            print("\n👋 برنامه مدیریت To-Do List با موفقیت بسته شد. خداحافظ!")
            break

        else:
            print("\n❌ انتخاب نامعتبر است. لطفاً بین 1 و 5 انتخاب کنید.")


if __name__ == "__main__":
    main()
