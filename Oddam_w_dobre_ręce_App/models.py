from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=125)


CHOICES = [
        ('FOUNDATION', 'fundacja'),
        ('NON-GOVERNMENTAL ORGANIZATION', 'organizacja pozarządowa'),
        ('LOCAL_COLLECTION', 'zbiórka lokalna'),
]

class Institution(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField()
    type = models.CharField(max_length=125, choices=CHOICES, default='FOUNDATION')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.name}, {self.description}, {self.type}"

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=125)
    phone_number = models.CharField(max_length=9)
    city = models.CharField(max_length=125)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)