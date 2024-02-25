from modeltranslation.translator import TranslationOptions, register
from .models import Product, Video, Image, Cart, Review

class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'product_info', 'product_type')

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'product_info', 'product_type')

class VideoTranslationOptions(TranslationOptions):
    fields = ('alt_text', 'info')

@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('alt_text', 'info')

class ImageTranslationOptions(TranslationOptions):
    fields = ('alt_text', 'info')

@register(Image)
class ImageTranslationOptions(TranslationOptions):
    fields = ('alt_text', 'info')

class CartTranslationOptions(TranslationOptions):
    fields = ('item_name',)

@register(Cart)
class CartTranslationOptions(TranslationOptions):
    fields = ('item_name',)

class ReviewTranslationOptions(TranslationOptions):
    fields = ('review', 'reviewer_name', 'review_title')

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('review', 'reviewer_name', 'review_title')
