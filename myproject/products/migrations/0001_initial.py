# Generated by Django 5.0.2 on 2024-02-25 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('name_en', models.CharField(blank=True, max_length=255, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('product_info', models.TextField(blank=True, null=True)),
                ('product_info_en', models.TextField(blank=True, null=True)),
                ('product_info_fr', models.TextField(blank=True, null=True)),
                ('product_type', models.CharField(blank=True, choices=[('Free', 'Free'), ('Paid', 'Paid')], max_length=10, null=True)),
                ('product_type_en', models.CharField(blank=True, choices=[('Free', 'Free'), ('Paid', 'Paid')], max_length=10, null=True)),
                ('product_type_fr', models.CharField(blank=True, choices=[('Free', 'Free'), ('Paid', 'Paid')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_text', models.CharField(blank=True, max_length=255, null=True)),
                ('alt_text_en', models.CharField(blank=True, max_length=255, null=True)),
                ('alt_text_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('info_en', models.TextField(blank=True, null=True)),
                ('info_fr', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=255, null=True)),
                ('item_name_en', models.CharField(blank=True, max_length=255, null=True)),
                ('item_name_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('item_code', models.CharField(blank=True, max_length=255, null=True)),
                ('item_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, null=True)),
                ('review_en', models.TextField(blank=True, null=True)),
                ('review_fr', models.TextField(blank=True, null=True)),
                ('reviewer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('reviewer_name_en', models.CharField(blank=True, max_length=255, null=True)),
                ('reviewer_name_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('review_title', models.CharField(blank=True, max_length=255, null=True)),
                ('review_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('review_title_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_text', models.CharField(blank=True, max_length=255, null=True)),
                ('alt_text_en', models.CharField(blank=True, max_length=255, null=True)),
                ('alt_text_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('info_en', models.TextField(blank=True, null=True)),
                ('info_fr', models.TextField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='products.product')),
            ],
        ),
    ]
