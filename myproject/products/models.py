from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    product_info = models.TextField(null=True, blank=True)
    product_type = models.CharField(max_length=10, choices=[('Free', _('Free')), ('Paid', _('Paid'))], null=True, blank=True)

    def __str__(self):
        return self.name if self.name else 'Unnamed Product'
    
class Video(models.Model):
    product = models.ForeignKey(Product, related_name='videos', on_delete=models.CASCADE)
    alt_text = models.CharField(max_length=255, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    
    def __str__(self):
        return self.info

class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    alt_text = models.CharField(max_length=255, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.info

class Cart(models.Model):
    product = models.ForeignKey(Product, related_name='carts', null=True, blank=True, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255, null=True, blank=True)
    item_code = models.CharField(max_length=255, null=True, blank=True)
    item_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.item_name

class Review(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, related_name='reviews', on_delete=models.CASCADE)
    review = models.TextField(null=True, blank=True)
    reviewer_name = models.CharField(max_length=255, null=True, blank=True)
    review_title = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.review_title