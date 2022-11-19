from statistics import mode
from django.contrib import admin
from . import models
#Register your models here.

admin.site.register(models.user)
admin.site.register(models.artical)
admin.site.register(models.Publications)
admin.site.register(models.media)
admin.site.register(models.Aprea_memberships)
admin.site.register(models.license_Person)
admin.site.register(models.artical_comments)
# admin.site.register(models.organization_members)