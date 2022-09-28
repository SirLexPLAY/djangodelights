from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("/inv_list", views.IngredientList.as_view(), name="inv_list")
]