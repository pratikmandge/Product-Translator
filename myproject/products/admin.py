from django.contrib import admin
from .models import Product, Video, Image, Cart, Review

class VideoInline(admin.TabularInline):
    model = Video

class ImageInline(admin.TabularInline):
    model = Image

class CartInline(admin.TabularInline):
    model = Cart

class ReviewInline(admin.TabularInline):
    model = Review

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        VideoInline,
        ImageInline,
        CartInline,
        ReviewInline,
    ]
    list_display = ('name', 'slug', 'product_type')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Video)
admin.site.register(Image)
admin.site.register(Cart)
admin.site.register(Review)