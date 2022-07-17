from django.contrib import admin
from .models import Image

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'path', 'date', 'display')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'path')
    list_editable = ('display',)
    list_filter = ('name', 'path', 'display', 'date')

admin.site.register(Image, ImageAdmin)