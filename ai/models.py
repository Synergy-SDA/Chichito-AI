from django.db import models

class ExternalCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False  # This model is managed externally
        db_table = 'category_category'  # Use the actual table name

    def __str__(self):
        return self.name

class ExternalFeature(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False  # This model is managed externally
        db_table = 'product_feature'  # Use the actual table name

    def __str__(self):
        return self.name

class ExternalFeatureValue(models.Model):
    feature = models.ForeignKey(ExternalFeature, related_name='external_values', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False  # This model is managed externally
        db_table = 'product_featurevalue'  # Use the actual table name

    def __str__(self):
        return f'{self.feature.name}: {self.value}'

class ExternalProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count_exist = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        ExternalCategory,
        related_name='external_products',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        managed = False  # This model is managed externally
        db_table = 'product_product'  # Use the actual table name

    def __str__(self):
        return self.name

class ProductFeatureValue(models.Model):
    product = models.ForeignKey(ExternalProduct, related_name='external_product_features', on_delete=models.CASCADE)
    feature_value = models.ForeignKey(ExternalFeatureValue, related_name='external_product_features', on_delete=models.CASCADE, db_column='featurevalue_id')

    class Meta:
        managed = False  # This model is managed externally
        db_table = 'product_product_features'  # Use the actual table name