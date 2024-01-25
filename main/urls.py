from django.urls import path
from . import views

urlpatterns = [
    path("", views.FoodListView.as_view(), name= "food_list"),
    #path("details/",views.HomePageView.as_view(),name="details"),
]

