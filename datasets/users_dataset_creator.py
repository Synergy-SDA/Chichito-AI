import pandas as pd
import random

# تعداد کاربران
num_users = 150

# توزیع‌های واقعی‌تر برای ویژگی‌ها
gender_weights = [0.63, 0.37]  # احتمال مرد و زن
category_weights = [0.3, 0.1, 0.1, 0.05, 0.15, 0.03, 0.13, 0.14]
trait_weights = [0.35, 0.1, 0.18, 0.12, 0.08, 0.12, 0.05]
material_weights = [0.3, 0.05, 0.11, 0.19, 0.03, 0.18, 0.14]
work_style_weights = [0.11, 0.29, 0.12, 0.18, 0.11, 0.07, 0.13]
occasion_weights = [0.28, 0.12, 0.17, 0.12, 0.06, 0.13, 0.12]
relationship_weights = [0.4, 0.15, 0.06, 0.14, 0.2, 0.03, 0.02]

# ویژگی‌های کاربران
genders = ["مرد", "زن"]
categories = ["الکترونیک", "پوشاک و اکسسوری", "خانه و دکور", "زیبایی و بهداشت", "ورزش و تناسب اندام", "کتاب و محصولات آموزشی", "پازل‌ها و بازی‌ها", "لوازم سفر و گردشگری"]
psychological_traits = ["برون‌گرا", "درون‌گرا", "خلاق و هنری", "منطقی و تحلیل‌گر", "احساسی و حمایتی", "ماجراجو و ورزشکار", "لوکس‌گرا و شیک"]
materials = ["پارچه", "فلزات", "پلاستیک", "چوبی", "شیشه و سرامیک", "ترکیبی", "خاص"]
work_styles = ["کلاسیک", "مدرن", "هنری", "لوکس و رسمی", "طبیعت‌محور", "منطقه‌ای", "فانتزی و خاص"]
occasions = ["تولد", "عروسی", "جشن فارغ‌التحصیلی", "سالگرد", "ارتقا کاری", "مناسبت فردی", "دیگر"]
relationships = ["دوست", "خانواده", "همکار", "آشنا", "همسر", "پارتنر", "افراد خاص"]

# ایجاد دیتاست
users_data = {
    "شناسه کاربر": list(range(1, num_users + 1)),
    "سن": [random.randint(1, 70) for _ in range(num_users)],
    "جنسیت": random.choices(genders, weights=gender_weights, k=num_users),
    "اولویت دسته‌بندی 1": random.choices(categories, weights=category_weights, k=num_users),
    "اولویت دسته‌بندی 2": random.choices(categories, weights=category_weights, k=num_users),
    "اولویت دسته‌بندی 3": random.choices(categories, weights=category_weights, k=num_users),
    "ویژگی روان‌شناختی": random.choices(psychological_traits, weights=trait_weights, k=num_users),
    "علاقه به متریال": random.choices(materials, weights=material_weights, k=num_users),
    "سبک کاری مورد علاقه": random.choices(work_styles, weights=work_style_weights, k=num_users),
    "مناسبت هدیه": random.choices(occasions, weights=occasion_weights, k=num_users),
    "نوع ارتباط با فرد گیرنده هدیه": random.choices(relationships, weights=relationship_weights, k=num_users),
}

# تبدیل به DataFrame
users_df = pd.DataFrame(users_data)

# ذخیره به فایل CSV
file_path = "./datasets/users.csv"
users_df.to_csv(file_path, index=False, encoding="utf-8-sig")

print(f"دیتاست کاربران با موفقیت ذخیره شد: {file_path}")
