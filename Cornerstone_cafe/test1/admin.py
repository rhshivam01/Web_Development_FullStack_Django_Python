from django.contrib import admin
from .models import Products
from .models import contact_query

# Register your models here.
admin.site.register(Products)
admin.site.register(contact_query)
