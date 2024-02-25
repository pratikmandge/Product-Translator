from rest_framework import serializers
from .models import Product, Video, Image, Cart, Review

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['alt_text', 'info']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['alt_text', 'info']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['item_name', 'item_code', 'item_price']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['review', 'reviewer_name', 'review_title']

class ProductSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True)
    images = ImageSerializer(many=True)
    carts = CartSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name', 'slug', 'product_info', 'product_type', 'videos', 'images', 'carts', 'reviews']
