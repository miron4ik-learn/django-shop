from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = [ 'name', 'slug' ]
  prepopulated_fields = { 'slug': ('name',) }
  
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = [ 'name', 'slug', 'image_show', 'price', 'available', 'created_at', 'updated_at' ]
  list_filter = [ 'available', 'created_at', 'updated_at' ]
  list_editable = [ 'price', 'available' ]
  prepopulated_fields = { 'slug': ('name',) }
  
  def image_show(self, obj):
    if obj.image:
      return mark_safe('<img src="{}" width="30">'.format(obj.image.url))
    return 'None'
  image_show.__name__ = 'Картинка'