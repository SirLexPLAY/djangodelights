from django.db import models

# This model represents an  ingredient that the restaurant has in its inventory.
class Ingredient(models.Model):
    POUNDS = "LB"
    TABLESPOON = "TB"
    TEASPOON = "TS"
    CUPS = "CU"
    UNIT_CHOICES = [
        (POUNDS, "lbs"),
        (TABLESPOON, "tbsp"),
        (TEASPOON, "tsp"),
        (CUPS, "c")
    ]

    name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    unit_price = models.FloatField(default=0)

# This model represents an item on the restaurant's menu.
class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField(default=0)

