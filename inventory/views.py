from django.shortcuts import render
from .models import Ingredient
from django.views.generic import ListView


# Create your views here.
def home(request):
    return render(request, "inventory/home.html")

class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/inv_list.html"
