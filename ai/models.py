from django.db import models

class ExternalProduct(models.Model):
    class Meta:
        managed = False
        db_table = 'product'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    count_exist = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FeatureValue(models.Model):
    class Meta:
        managed = False
        db_table = 'feature_value'

    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        ExternalProduct, 
        related_name='features', 
        on_delete=models.DO_NOTHING
    )
    feature_name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.feature_name}: {self.value}"
