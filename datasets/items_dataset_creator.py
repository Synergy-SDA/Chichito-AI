import pandas as pd
import random

# تعداد کالاها
num_items = 1400

# ویژگی‌های کالا
categories = ["الکترونیک", "پوشاک و اکسسوری", "خانه و دکور", "زیبایی و بهداشت", "ورزش و تناسب اندام", "کتاب و محصولات آموزشی","پازل‌ها و بازی‌ها","لوازم سفر و گردشگری"]
colors = ["خنثی", "اصلی", "ثانویه", "طبیعی", "روشن و شاد", "فلزی", "تیره و لوکس"]
materials = ["پارچه", "فلزات", "پلاستیک", "چوبی", "شیشه و سرامیک", "ترکیبی", "خاص"]
design_styles = ["کلاسیک", "مدرن", "هنری", "لوکس و رسمی", "طبیعت‌محور", "منطقه‌ای", "فانتزی و خاص"]
usages = ["شخصی", "دکور", "تکنولوژی", "سرگرمی", "تناسب اندام", "کاری", "سلامت"]
genders = ["مردانه", "زنانه", "خنثی"]

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
