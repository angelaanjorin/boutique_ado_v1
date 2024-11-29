from django.contrib import admin
from .models import Product, PrimaryCategory, SpecialCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'primary_category',  # Display the primary category
        'get_special_categories',  # Display special categories
        'price',
        'rating',
        'image',
    )
    ordering = ('name',)  # Orders products by name

    def get_special_categories(self, obj):
        """
        Returns a comma-separated list of special categories a product belongs to.
        """
        return ", ".join([category.name for category in obj.special_categories.all()])
    get_special_categories.short_description = 'Special Categories'  # Column name

class PrimaryCategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')
    ordering = ('name',)

class SpecialCategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')
    ordering = ('name',)


# Register models in the admin site
admin.site.register(Product, ProductAdmin)
admin.site.register(PrimaryCategory, PrimaryCategoryAdmin)
admin.site.register(SpecialCategory, SpecialCategoryAdmin)
