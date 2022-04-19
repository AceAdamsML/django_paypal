from django.contrib import admin

# Register your models here.

from .models import Movie, Order, Seat

admin.site.register(Movie)
admin.site.register(Order)
admin.site.register(Seat)