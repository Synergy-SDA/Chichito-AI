import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np
from .models import *
from django.core.cache import cache
from datetime import timedelta
import os

class Evaluation:
    def __init__(self, user_data):
        self.user_data = user_data
        self.products_data = None
        self.encoded_user_data = None
        self.encoded_products_data = None
        self.model = None        
    

    def get_user_data(self):
        diction = {'age': self.user_data['age'], 'gender': self.user_data['gender'],
                   'category_1': self.user_data['category_1'], 'category_2': self.user_data['category_2'],
                   'category_3': self.user_data['category_3'], 'psychological_traits': self.user_data['psychological_traits'],
                   'favorite_material': self.user_data['favorite_material'], 'favorite_design': self.user_data['favorite_design'],
                   'occasions': self.user_data['occasions'], 'relationship': self.user_data['relationship']}
        print(diction)
        self.user_data = pd.DataFrame(diction, index = np.arange(1))
        # print(self.user_data)

       
    def product_data(self):
        # Get user gender from user data
        user_gender = self.user_data["gender"].iloc[0]

        # Fetch products with filtering based on user gender
        if user_gender == "مرد":
            products = ExternalProduct.objects.using('external').filter(
                external_product_features__feature_value__feature__name="جنسیت",
                external_product_features__feature_value__value__in=["مردانه", "خنثی"]
            ).distinct()
        elif user_gender == "زن":
            products = ExternalProduct.objects.using('external').filter(
                external_product_features__feature_value__feature__name="جنسیت",
                external_product_features__feature_value__value__in=["زنانه", "خنثی"]
            ).distinct()
        else:
            products = ExternalProduct.objects.using('external').all()

        product_data = []

        for product in products:
            # Fetch features for each product
            product_feature_values = ProductFeatureValue.objects.using('external').filter(product=product).select_related('feature_value__feature')
            feature_dict = {pfv.feature_value.feature.name: pfv.feature_value.value for pfv in product_feature_values if pfv.feature_value.feature.name in ["نوع رنگ", "سبک طراحی", "کاربرد", "جنسیت", "متریال"]}

            # Combine product and feature data
            product_info = {
                "id": product.id,
                "category": product.category.name if product.category else None,  # Get category name
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
            "category": "categories",
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

        self.encoded_user_data = manual_encoder(self.user_data, user_mapping)
        self.encoded_products_data = manual_encoder(self.products_data, product_mapping)
    def load_pretrained_model(self):
        try:
            model_path = os.path.join(os.path.dirname(__file__), "best_model.keras")
            self.model = keras.models.load_model(model_path)
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

        # Ensure the input data matches the expected shape
        expected_user_shape = (None, 10)  # User input shape
        expected_product_shape = (None, 6)  # Product input shape

        if user_data_np.shape[1] != expected_user_shape[1]:
            raise ValueError(f"Expected user data shape {expected_user_shape}, but got {user_data_np.shape}")

        if product_data_np.shape[1] != expected_product_shape[1]:
            raise ValueError(f"Expected product data shape {expected_product_shape}, but got {product_data_np.shape}")

        predictions = []
        for product in product_data_np:
            repeated_user_data_np = np.tile(user_data_np, (1, 1))
            prediction = self.model.predict([product.reshape(1, -1), repeated_user_data_np])
            predictions.append(prediction[0][0])

        top_predictions = np.argsort(-np.array(predictions))[:10]
        top_products = self.encoded_products_data.iloc[top_predictions]

        product_ids = top_products["id"].tolist()
        products = ExternalProduct.objects.using('external').filter(id__in=product_ids)

        results = []
        for product in products:
            # Combine product data
            product_info = {
                "id": product.id,
                "name": product.name,
                "category": product.category.name if product.category else None,  # Get category name
                "price": product.price,
                "count_exist": product.count_exist,
                "is_available": product.is_available,
            }
            results.append(product_info)

        cache.set(cache_key, results, timeout=15*60)
        return results