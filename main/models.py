from django.db import models

class Category(models.Model):
  class Meta:
    ordering = ('name',)
    verbose_name = 'Категория',
    verbose_name_plural = 'Категории'
  
  name = models.CharField(verbose_name='Название', max_length=100, db_index=True)
  slug = models.SlugField(max_length=100, unique=True)
  
  def __str__(self):
    return self.name
  
class Product(models.Model):
  class Meta:
    ordering = ('name',)
    verbose_name = 'Товар',
    verbose_name_plural = 'Товары'
    index_together = (('id', 'slug'),)
    
  category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
  
  name = models.CharField(verbose_name='Название', max_length=150, db_index=True)
  slug = models.SlugField(max_length=150, db_index=True, unique=True)
  
  image = models.ImageField(verbose_name='Картинка', upload_to='product/%Y/%m/%d', blank=True)
  description = models.TextField(verbose_name='Описание', max_length=1000, blank=True)
  price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
  available = models.BooleanField(verbose_name='Наличие', default=True)
  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name