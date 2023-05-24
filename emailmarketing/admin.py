from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'email', 'phone', 'city', 'state', 'zip', 'status']
admin.site.register(Subscriber, SubscriberAdmin)

