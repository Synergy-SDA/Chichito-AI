import pandas as pd
import random

# تعداد کاربران
num_users = 500

# ویژگی‌های کاربران
ages = [random.randint(1, 100) for _ in range(num_users)]
genders = ["مرد", "زن"]
categories = ["الکترونیک", "پوشاک و اکسسوری", "خانه و دکور", "زیبایی و بهداشت", "ورزش و تناسب اندام", "کتاب و محصولات آموزشی","پازل‌ها و بازی‌ها","لوازم سفر و گردشگری"]
psychological_traits = ["برون‌گرا", "درون‌گرا", "خلاق و هنری", "منطقی و تحلیل‌گر", "احساسی و حمایتی", "ماجراجو و ورزشکار", "لوکس‌گرا و شیک"]
materials = ["پارچه", "فلزات", "پلاستیک", "چوبی", "شیشه و سرامیک", "ترکیبی", "خاص"]
work_styles = ["کلاسیک", "مدرن", "هنری", "لوکس و رسمی", "طبیعت‌محور", "منطقه‌ای", "فانتزی و خاص"]
occasions = ["تولد", "عروسی", "جشن فارغ‌التحصیلی", "سالگرد", "ارتقا کاری", "مناسبت فردی", "دیگر"]
relationships = ["دوست", "خانواده", "همکار", "آشنا", "همسر", "پارتنر", "افراد خاص"]

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
