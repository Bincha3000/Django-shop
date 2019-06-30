from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'slug']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    def body_short(self, obj: Product):
        return f'{obj.body[:30]}...'

    list_display = ['id', 'title', 'slug', 'body_short', 'price']