from django.contrib import admin

from cars.models import Car


@admin.register(Car)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', ]
