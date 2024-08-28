from django.contrib import admin
from . import models 

admin.site.register(models.City ),  
admin.site.register(models.Appartment),
admin.site.register(models.Image),
admin.site.register(models.User),
admin.site.register(models.Estimation),