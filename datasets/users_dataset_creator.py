import pandas as pd
import random

# تعداد کاربران
num_users = 500

# ویژگی‌های کاربران
ages = [random.randint(1, 60) for _ in range(num_users)]
genders = ["مرد", "زن"]
categories = ["الکترونیکی", "پوشاک", "ورزشی", "کتاب", "دکور"]
psychological_traits = ["خلاق", "منظم", "اجتماعی", "درون‌گرا", "برون‌گرا"]
materials = ["چوب", "فلز", "پلاستیک", "چرم", "شیشه"]
work_styles = ["مدرن", "کلاسیک", "مینیمال", "رنگارنگ"]
occasions = ["تولد", "عروسی", "جشن فارغ‌التحصیلی", "سالگرد", None]
relationships = ["دوست", "خانواده", "همکار", "آشنا", "نامشخص"]

# ایجاد دیتاست
users_data = {
    "شناسه کاربر": list(range(1, num_users + 1)),
    "سن": ages,
    "جنسیت": [random.choice(genders) for _ in range(num_users)],
    "اولویت دسته‌بندی 1": [random.choice(categories) for _ in range(num_users)],
    "اولویت دسته‌بندی 2": [random.choice(categories) for _ in range(num_users)],
    "اولویت دسته‌بندی 3": [random.choice(categories) for _ in range(num_users)],
    "ویژگی روان‌شناختی": [random.choice(psychological_traits) for _ in range(num_users)],
    "علاقه به متریال": [random.choice(materials) for _ in range(num_users)],
    "سبک کاری مورد علاقه": [random.choice(work_styles) for _ in range(num_users)],
    "مناسبت هدیه": [random.choice(occasions) for _ in range(num_users)],
    "نوع ارتباط با فرد گیرنده هدیه": [
        random.choice(relationships) for _ in range(num_users)
    ],
}

# تبدیل به DataFrame
users_df = pd.DataFrame(users_data)

# ذخیره به فایل CSV
file_path = "./datasets/users.csv"
users_df.to_csv(file_path, index=False, encoding="utf-8-sig")

print(f"دیتاست کاربران با موفقیت ذخیره شد: {file_path}")
