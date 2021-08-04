from django.db import models

# Create your models here.
class price(models.Model):
    BRAND_CHOICES = (
        ('Audi', 'Audi'),
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes')
    )
    MODEL_CHOICES = (
        ('A3', 'A3'),
        ('3 SERIES', '3 SERIES'),
        ('CLA', 'CLA')
    )
    engine_displacement = models.IntegerField(default=2000)
    horsepower = models.IntegerField(default=200)
    mileage = models.IntegerField(default=30000)
    brand = models.CharField(max_length=30, choices=BRAND_CHOICES)
    model = models.CharField(max_length=30, choices=MODEL_CHOICES)
    year = models.IntegerField(default=2015)

    def __str__(self):
        return self.brand, self.brand
        