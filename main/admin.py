from django.contrib import admin
from .models import Customer
from .models import Food
from .models import Section
from .models import Factor
from .models import Select
from .models import BikeDelivery

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

admin.site.register(Customer)
admin.site.register(Food)
admin.site.register(Section)
admin.site.register(Factor)
admin.site.register(Select)
admin.site.register(BikeDelivery)
