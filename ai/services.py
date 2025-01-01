
from django.core.cache import cache
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np
from .models import *
from django.core.cache import cache
from datetime import timedelta

class Evaluation:
    def __init__(self, user_data):
        self.user_data = user_data
    

    def get_user_data(self):
        self.user_data = pd.DataFrame(self.user_data)
        column_rename_mapping = {
            "دسته_بندی_۱": "category_1",
            "دسته_بندی_۲": "category_2",
            "دسته_بندی_۳": "category_3",
            "جنسیت": "gender",
            "ویژگی_های_روانی": "psychological_traits",
            "متریال_مورد_علاقه": "favorite_material",
            "طراحی_مورد_علاقه": "favorite_design",
            "مناسبت_ها": "occasions",
            "روابط": "relationship"
        }

        # Rename columns in user_data
        self.user_data.rename(columns=column_rename_mapping, inplace=True)

    def product_data(self):
        # Fetch products
        user_gender = self.user_data["جنسیت"].iloc[0]

        # Fetch products with filtering based on user gender
        if user_gender == "مرد":
            products = ExternalProduct.objects.using('external').filter(features__feature_name="جنسیت", features__value__in=["مردانه", "خنثی"]).distinct()
        elif user_gender == "زن":
            products = ExternalProduct.objects.using('external').filter(features__feature_name="جنسیت", features__value__in=["زنانه", "خنثی"]).distinct()
        else:
            products = ExternalProduct.objects.using('external').all()
        
        product_data = []

        for product in products:
            # Fetch features for each product
            features = FeatureValue.objects.using('external').filter(product=product)
            feature_dict = {f.feature_name: f.value for f in features if f.feature_name in ["نوع رنگ", "سبک طراحی", "کاربرد", "جنسیت", "متریال"]}

            # Combine product and feature data
            product_info = {
                "id": product.id,
                "categories": product.category,  # Add categories field
                "نوع رنگ": feature_dict.get("نوع رنگ", None),
                "سبک طراحی": feature_dict.get("سبک طراحی", None),
                "کاربرد": feature_dict.get("کاربرد", None),
                "جنسیت": feature_dict.get("جنسیت", None),
                "متریال": feature_dict.get("متریال", None),
            }
            product_data.append(product_info)

        # Convert to DataFrame for further processing
        self.products_data = pd.DataFrame(product_data)

        # Rename columns according to product_mapping keys
        column_rename_mapping = {
            "نوع رنگ": "colors",
            "سبک طراحی": "design_styles",
            "کاربرد": "usages",
            "جنسیت": "genders",
            "متریال": "materials"
        }
        self.products_data.rename(columns=column_rename_mapping, inplace=True)

    
    def encoding(self):
        def manual_encoder(df, mapping_dict):
            for col, mapping in mapping_dict.items():
                if col in df.columns:
                    df[col] = df[col].apply(lambda x: mapping.get(x, -1))
            return df

        user_mapping = {
        "category_1": {v: i for i, v in enumerate(["الکترونیک", "پوشاک و اکسسوری", "خانه و دکور", "زیبایی و بهداشت", "ورزش و تناسب اندام", "کتاب و محصولات آموزشی", "پازل ها و بازی ها", "لوازم سفر و گردشگری"])},
        "category_2": {v: i for i, v in enumerate(["الکترونیک", "پوشاک و اکسسوری", "خانه و دکور", "زیبایی و بهداشت", "ورزش و تناسب اندام", "کتاب و محصولات آموزشی", "پازل ها و بازی ها", "لوازم سفر و گردشگری"])},
        "category_3": {v: i for i, v in enumerate(["الکترونیک", "پوشاک و اکسسوری", "خانه و دکور", "زیبایی و بهداشت", "ورزش و تناسب اندام", "کتاب و محصولات آموزشی", "پازل ها و بازی ها", "لوازم سفر و گردشگری"])},
        "gender": {v: i for i, v in enumerate(["مرد", "زن"])},
        "psychological_traits": {v: i for i, v in enumerate(["برون گرا", "درون گرا", "خلاق و هنری", "منطقی و تحلیل گر", "احساسی و حمایتی", "ماجراجو و ورزشکار", "لوکس گرا و شیک"])},
        "favorite_material": {v: i for i, v in enumerate(["پارچه", "فلزات", "پلاستیک", "چوبی", "شیشه و سرامیک", "ترکیبی", "خاص"])},
        "favorite_design": {v: i for i, v in enumerate(["کلاسیک", "مدرن", "هنری", "لوکس و رسمی", "طبیعت محور", "منطقه ای", "فانتزی و خاص"])},
        "occasions": {v: i for i, v in enumerate(["تولد", "عروسی", "جشن فارغ التحصیلی", "سالگرد", "ارتقا کاری", "مناسبت فردی", "دیگر"])},
        "relationship": {v: i for i, v in enumerate(["دوست", "خانواده", "همکار", "آشنا", "همسر", "پارتنر", "افراد خاص"])}
        }
        
        product_mapping = {
        "categories": {v: i for i, v in enumerate(["الکترونیک", "پوشاک و اکسسوری", "خانه و دکور", "زیبایی و بهداشت", "ورزش و تناسب اندام", "کتاب و محصولات آموزشی", "پازل ها و بازی ها", "لوازم سفر و گردشگری"])},
        "colors": {v: i for i, v in enumerate(["خنثی", "اصلی", "ثانویه", "طبیعی", "روشن و شاد", "فلزی", "تیره و لوکس"])},
        "materials": {v: i for i, v in enumerate(["پارچه", "فلزات", "پلاستیک", "چوبی", "شیشه و سرامیک", "ترکیبی", "خاص"])},
        "design_styles": {v: i for i, v in enumerate(["کلاسیک", "مدرن", "هنری", "لوکس و رسمی", "طبیعت محور", "منطقه ای", "فانتزی و خاص"])},
        "usages": {v: i for i, v in enumerate(["شخصی", "دکور", "تکنولوژی", "سرگرمی", "تناسب اندام", "کاری", "سلامت"])},
        "genders": {v: i for i, v in enumerate(["مردانه", "زنانه", "خنثی"])}
        }

        self.encoded_user_data = manual_encoder(self.encoded_user_data, user_mapping)
        self.encoded_products_data = manual_encoder(self.encoded_products_data, product_mapping)
    def load_pretrained_model(self):
        try:
            self.model = keras.models.load_model("./best_model.keras")
            print("Model loaded successfully!")
        except Exception as e:
            print(f"Error loading model: {e}")
    def evaluate(self):
        cache_key = f"user_predictions_{hash(str(self.user_data))}"
        cached_results = cache.get(cache_key)
        if cached_results:
            return cached_results
        user_data_np = self.encoded_user_data.to_numpy()
        product_data_np = self.encoded_products_data.drop(columns=["id"]).to_numpy()
        predictions = self.model.predict([product_data_np, np.repeat(user_data_np, len(product_data_np), axis=0)])
        top_predictions = np.argsort(-predictions.flatten())[:10]
        top_products = self.encoded_products_data.iloc[top_predictions]

        product_ids = top_products["id"].tolist()
        products = ExternalProduct.objects.filter(id__in=product_ids).prefetch_related('features')

        results = []
        for product in products:
            product_info = {
                "id": product.id,
                "name": product.name,
                "category": product.category,
                "price": product.price,
                "count_exist": product.count_exist,
                "is_available": product.is_available,
                "features": [
                    {
                        "feature_name": feature.feature_name,
                        "value": feature.value
                    }
                    for feature in product.features.all()
                ]
            }
            results.append(product_info)

        cache.set(cache_key, results, timeout=15*60)
        return results


    