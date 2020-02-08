from django.db import models
from django.utils import timezone


class College(models.Model):
    en_name = models.TextField()
    kr_name = models.TextField()

    def __str__(self):
        return self.kr_name


class Restaurant(models.Model):
    # code = models.TextField()
    en_name = models.TextField()
    kr_name = models.TextField()
    operating_hours = models.TextField()
    hours_breakfast = models.TextField()
    hours_lunch = models.TextField()
    hours_dinner = models.TextField()
    # location = models.TextField()
    # latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    college = models.ForeignKey(College, related_name="res", on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.kr_name


class Meal(models.Model):
    en_name = models.TextField()
    kr_name = models.TextField()
    price = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    # TYPES = (('BR', 'breakfast'), ('LU', 'lunch'), ('DN', 'dinner'))
    # type = models.CharField(max_length=2, choices=TYPES, blank=True)

    def __str__(self):
        return self.kr_name


class Menu(models.Model):
    meals = models.ManyToManyField(Meal)
    date = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    TYPES = (('BR', 'breakfast'), ('LU', 'lunch'), ('DN', 'dinner'))
    type = models.CharField(max_length=2, choices=TYPES, blank=True)

    def __str__(self):
        return f"{self.date} {self.restaurant} {self.type}"
