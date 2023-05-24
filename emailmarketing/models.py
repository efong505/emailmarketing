from django.db import models


class Subscriber(models.Model):
    class Status(models.TextChoices):
        SUBSCRIBED = 'Subscribed'
        PENDING = 'Pending'
        UNSUBSCRIBED = 'Unsubscribed'
        
    

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=12, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,
                              choices=Status.choices, 
                              default=Status.SUBSCRIBED)
    
    def __str__(self):
        return self.first_name + " " + self.last_name