from django.contrib import admin
from test_rest_api_app import models

# Register your models here.
admin.site.register(models.UserProfile) #registers our userModel
admin.site.register(models.ProfileFeedItem) #registers our Profile model