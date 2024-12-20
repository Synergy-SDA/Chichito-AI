import pandas as pd
import random

# تعداد کالاها
num_items = 150

# توزیع‌های نامتوازن‌تر برای ویژگی‌ها
category_weights = [0.37, 0.12, 0.06, 0.11, 0.04, 0.07, 0.04, 0.14]
color_weights = [0.3, 0.1, 0.05, 0.15, 0.05, 0.2, 0.15]
material_weights = [0.35, 0.1, 0.05, 0.2, 0.05, 0.1, 0.15]
design_style_weights = [0.4, 0.15, 0.05, 0.1, 0.1, 0.1, 0.1]
usage_weights = [0.5, 0.1, 0.05, 0.1, 0.05, 0.1, 0.1]
gender_weights = [0.6, 0.3, 0.1]

# ویژگی‌های کالا
categories = ["الکترونیک", "پوشاک و اکسسوری", "خانه و دکور", "زیبایی و بهداشت", "ورزش و تناسب اندام", "کتاب و محصولات آموزشی", "پازل ها و بازی ها", "لوازم سفر و گردشگری"]
colors = ["خنثی", "اصلی", "ثانویه", "طبیعی", "روشن و شاد", "فلزی", "تیره و لوکس"]
materials = ["پارچه", "فلزات", "پلاستیک", "چوبی", "شیشه و سرامیک", "ترکیبی", "خاص"]
design_styles = ["کلاسیک", "مدرن", "هنری", "لوکس و رسمی", "طبیعت محور", "منطقه ای", "فانتزی و خاص"]
usages = ["شخصی", "دکور", "تکنولوژی", "سرگرمی", "تناسب اندام", "کاری", "سلامت"]
genders = ["مردانه", "زنانه", "خنثی"]

# ایجاد دیتاست
items_data = {
    "product_id": list(range(1, num_items + 1)),
    "categories": random.choices(categories, weights=category_weights, k=num_items),
    "colors": random.choices(colors, weights=color_weights, k=num_items),
    "materials": random.choices(materials, weights=material_weights, k=num_items),
    "design_styles": random.choices(design_styles, weights=design_style_weights, k=num_items),
    "usages": random.choices(usages, weights=usage_weights, k=num_items),
    "genders": random.choices(genders, weights=gender_weights, k=num_items),
}

# تبدیل به DataFrame
items_df = pd.DataFrame(items_data)

# ذخیره به فایل CSV
file_path = "./datasets/items.csv"
items_df.to_csv(file_path, index=False, encoding="utf-8-sig")

print(f"دیتاست کالا با موفقیت ذخیره شد: {file_path}")
