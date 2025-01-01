from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=["مرد", "زن"])
    category_1 = serializers.ChoiceField(choices=["الکترونیک", "پوشاک و اکسسوری", "خانه و دکور", "زیبایی و بهداشت", "ورزش و تناسب اندام", "کتاب و محصولات آموزشی", "پازل ها و بازی ها", "لوازم سفر و گردشگری"])
    category_2 = serializers.ChoiceField(choices=["الکترونیک", "پوشاک و اکسسوری", "خانه و دکور", "زیبایی و بهداشت", "ورزش و تناسب اندام", "کتاب و محصولات آموزشی", "پازل ها و بازی ها", "لوازم سفر و گردشگری"])
    category_3 = serializers.ChoiceField(choices=["الکترونیک", "پوشاک و اکسسوری", "خانه و دکور", "زیبایی و بهداشت", "ورزش و تناسب اندام", "کتاب و محصولات آموزشی", "پازل ها و بازی ها", "لوازم سفر و گردشگری"])
    psychological_traits = serializers.ChoiceField(choices=["برون گرا", "درون گرا", "خلاق و هنری", "منطقی و تحلیل گر", "احساسی و حمایتی", "ماجراجو و ورزشکار", "لوکس گرا و شیک"])
    favorite_material = serializers.ChoiceField(choices=["پارچه", "فلزات", "پلاستیک", "چوبی", "شیشه و سرامیک", "ترکیبی", "خاص"])
    favorite_design = serializers.ChoiceField(choices=["کلاسیک", "مدرن", "هنری", "لوکس و رسمی", "طبیعت محور", "منطقه ای", "فانتزی و خاص"])
    occasions = serializers.ChoiceField(choices=["تولد", "عروسی", "جشن فارغ التحصیلی", "سالگرد", "ارتقا کاری", "مناسبت فردی", "دیگر"])
    def validate(self, data):
        """
        Check that all fields have values within the specified choices.
        """
        user_mapping = {
            "category_1": ["الکترونیک", "پوشاک و اکسسوری", "خانه و دکور", "زیبایی و بهداشت", "ورزش و تناسب اندام", "کتاب و محصولات آموزشی", "پازل ها و بازی ها", "لوازم سفر و گردشگری"],
            "category_2": ["الکترونیک", "پوشاک و اکسسوری", "خانه و دکور", "زیبایی و بهداشت", "ورزش و تناسب اندام", "کتاب و محصولات آموزشی", "پازل ها و بازی ها", "لوازم سفر و گردشگری"],
            "category_3": ["الکترونیک", "پوشاک و اکسسوری", "خانه و دکور", "زیبایی و بهداشت", "ورزش و تناسب اندام", "کتاب و محصولات آموزشی", "پازل ها و بازی ها", "لوازم سفر و گردشگری"],
            "gender": ["مرد", "زن"],
            "psychological_traits": ["برون گرا", "درون گرا", "خلاق و هنری", "منطقی و تحلیل گر", "احساسی و حمایتی", "ماجراجو و ورزشکار", "لوکس گرا و شیک"],
            "favorite_material": ["پارچه", "فلزات", "پلاستیک", "چوبی", "شیشه و سرامیک", "ترکیبی", "خاص"],
            "favorite_design": ["کلاسیک", "مدرن", "هنری", "لوکس و رسمی", "طبیعت محور", "منطقه ای", "فانتزی و خاص"],
            "occasions": ["تولد", "عروسی", "جشن فارغ التحصیلی", "سالگرد", "ارتقا کاری", "مناسبت فردی", "دیگر"],
            "relationship": ["دوست", "خانواده", "همکار", "آشنا", "همسر", "پارتنر", "افراد خاص"]
        }

        for field, choices in user_mapping.items():
            if field in data and data[field] not in choices:
                raise serializers.ValidationError({field: f"Invalid value for {field}. Must be one of {choices}."})

        return data