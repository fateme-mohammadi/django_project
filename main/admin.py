from django.contrib import admin
from .models import Customer
from .models import Food
from .models import Section
from .models import Factor
from .models import Select

# Register your models here.

admin.site.register(Customer)
admin.site.register(Food)
admin.site.register(Section)
admin.site.register(Factor)
admin.site.register(Select)