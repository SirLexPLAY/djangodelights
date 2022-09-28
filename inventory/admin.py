from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

# admin login: dawid
# admin password: admin123

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)