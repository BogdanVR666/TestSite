# Generated by Django 3.2.5 on 2021-08-11 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='RODUCT_DESCRIPTION',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='PRODUCT_PRICE',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='PRODUCT_TITLE',
            new_name='title',
        ),
    ]