from django.contrib import admin

# Register your models here.
from User.models import CustomUser

admin.site.register(CustomUser)
