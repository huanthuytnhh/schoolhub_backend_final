# menu/admin.py

from django.contrib import admin
from .models import Menu, MenuItem

# Inline for MenuItem to be managed directly from the Menu admin page
class MenuItemInline(admin.TabularInline): # or admin.StackedInline
    model = MenuItem
    extra = 1 # Number of empty forms to display

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('date', 'imageUrl')
    search_fields = ('date',)
    inlines = [MenuItemInline] # Add MenuItemInline here
