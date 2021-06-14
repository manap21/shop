from django.db import models

class user(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=250)
    country_code = models.IntegerField(max_length=10)

class countries(models.Model):
    code = models.IntegerField(max_length=10)
    name = models.CharField(max_length=100)

class products(models.Model):
    CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии')
    )

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to='products')
    price = models.IntegerField(max_length=20)
    status = models.CharField(choices=CHOICES)

