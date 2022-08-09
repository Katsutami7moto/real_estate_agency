from django.contrib import admin

from .models import Flat


class AdminModel(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)


admin.site.register(Flat, AdminModel)
