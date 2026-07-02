from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    pass

class Dataset(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='datasets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'dataset'

class Insight(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'insight'

class Forecast(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    column_name = models.CharField(max_length=100)
    predicted_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'forecast'

class ColumnMapping(models.Model):
    dataset = models.OneToOneField(Dataset, on_delete=models.CASCADE)
    revenue_column = models.CharField(max_length=100)
    sales_column = models.CharField(max_length=100)
    product_column = models.CharField(max_length=100)
    date_column = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'column_mapping'

