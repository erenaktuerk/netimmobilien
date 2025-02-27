from django.contrib import admin
from .models import *


class PropertyImageInLine(admin.TabularInline):
    model = Property_images


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['id', 'property_title', 'object_type',
                    'street', 'postialcode', 'city', 'price', 'is_available']
    list_editable = ['is_available', 'price']
    list_display_links = ['id', 'property_title']
    search_fields = ('id', 'property_title', 'street',
                     'housenumber', 'postialcode', 'city')
    list_filter = ('city', 'object_type', 'country')
    inlines = [PropertyImageInLine]


admin.site.register(Property_images)
admin.site.register(DetailPropertyInteres)
