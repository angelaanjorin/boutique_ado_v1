from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

class PrimaryCategory(models.Model):
    """
    Categories that are unique to a product, like hair_wigs, hair_extensions, etc.
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Primary Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class SpecialCategory(models.Model):
    """
    Optional categories like deals, new_arrivals, and best_collections.
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Special Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    primary_category = models.ForeignKey(
        PrimaryCategory,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='products'
    )
    special_categories = models.ManyToManyField(
        SpecialCategory,
        blank=True,
        related_name='products'
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    stock_amount = models.IntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )
    in_stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.IntegerField(null=True, blank=True)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def price_discount(self):
        """
        Calculate discount based on new price.
        """
        if self.sale_price:
            discount = ((self.price - self.sale_price) / self.price) * 100
            return round(discount)
        return None

    @property
    def product_in_stock(self):
        """
        Determines if the product is in stock based on the stock amount.
        """
        return self.stock_amount >= 1

    @property
    def product_price(self):
        """
        Returns the price of item based on whether it is on sale.
        """
        if self.on_sale and self.sale_price < self.price:
            return self.sale_price
        return self.price

    def save(self, *args, **kwargs):
        self.discount = self.price_discount
        self.in_stock = self.product_in_stock
        if not self.on_sale:
            self.sale_price = None
        super().save(*args, **kwargs)
