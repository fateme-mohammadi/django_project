from django.urls import path
from . import views

urlpatterns = [
    path('', views.FoodListView.as_view()),
    path('', views.MenuListView.as_view()),
    path('<int:pk>',views.detail),

]

