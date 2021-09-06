from django.contrib import admin
from .models import company, User, customer, order
# Register your models here.
admin.site.register(company)
admin.site.register(User)
admin.site.register(customer)
admin.site.register(order)