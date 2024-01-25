from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Food
from django.views.generic import ListView

'''
def Food_list(request):
    foods = Food.objects.all()
    context = {
        "foods":foods
    }
    return render(request,"foods.html",context)
'''
class FoodListView(ListView):
    model = Food
    template_name = "foods/foods.html"
    context_object_name = "foods"
