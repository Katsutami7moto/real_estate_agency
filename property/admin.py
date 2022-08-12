from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats_owned.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', )
    readonly_fields = ('created_at',)
    list_display = (
        'address', 'price', 'new_building', 
        'construction_year', 'town',
    )
    list_editable = ('new_building',)
    list_filter = (
        'new_building', 'rooms_number', 
        'has_balcony', 'active',
    )
    raw_id_fields = ('liked_by',)
    inlines = (OwnerInline,)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats_owned',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
