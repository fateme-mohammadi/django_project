from django.urls import path
from . import views

urlpatterns = [
    path("", views.FoodListView.as_view(), name= "food_list"),
    #path("details/",views.HomePageView.as_view(),name="details"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]

