from django.urls import path
from . import views

urlpatterns = [
    path('', views.FoodListView.as_view()),
    path('food/', views.food_list, name='food_list'),
    path('<int:pk>',views.detail),

]

