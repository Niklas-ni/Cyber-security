from django.contrib import admin

# Register your models here.
from .models import Blacklist


admin.site.register(Blacklist)