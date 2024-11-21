import pandas as pd
import random

# تعداد کالاها
num_items = 1500

# ویژگی‌های کالا
categories = ["الکترونیکی", "پوشاک", "ورزشی", "کتاب", "دکور"]
colors = ["طلایی", "مشکی", "سفید", "آبی", "قرمز", "سبز"]
materials = ["چوب", "فلز", "پلاستیک", "چرم", "شیشه"]
design_styles = ["مدرن", "کلاسیک", "مینیمال", "رنگارنگ"]
usages = ["تزئینی", "کاربردی", "ورزشی", "آموزشی", "دکوری"]
genders = ["مردانه", "زنانه", "بدون جنسیت"]

# ایجاد دیتاست
items_data = {
    "شناسه کالا": list(range(1, num_items + 1)),
    "دسته‌بندی": [random.choice(categories) for _ in range(num_items)],
    "رنگ": [random.choice(colors) for _ in range(num_items)],
    "متریال": [random.choice(materials) for _ in range(num_items)],
    "سبک طراحی": [random.choice(design_styles) for _ in range(num_items)],
    "کاربرد": [random.choice(usages) for _ in range(num_items)],
    "جنسیت": [random.choice(genders) for _ in range(num_items)],
}

# تبدیل به DataFrame
items_df = pd.DataFrame(items_data)

# ذخیره به فایل CSV
file_path = "./datasets/items.csv"
items_df.to_csv(file_path, index=False, encoding="utf-8-sig")

print(f"دیتاست کالا با موفقیت ذخیره شد: {file_path}")
