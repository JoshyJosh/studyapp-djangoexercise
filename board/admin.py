from django.contrib import admin

from .models import User, Topic, Subscription

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Subscription)
# Register your models here.
