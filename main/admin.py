from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = [ 'name', 'slug' ]
  prepopulated_fields = { 'slug': ('name',) }
  
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = [ 'name', 'slug', 'price', 'available', 'created_at', 'updated_at' ]
  list_filter = [ 'available', 'created_at', 'updated_at' ]
  list_editable = [ 'price', 'available' ]
  prepopulated_fields = { 'slug': ('name',) }