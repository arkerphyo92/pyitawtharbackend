# Generated by Django 5.1.6 on 2025-02-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("business", "0007_remove_discount_discount_percentage_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="price",
            name="retail_pay_type",
            field=models.CharField(
                choices=[
                    ("Kilograms", "Kg"),
                    ("Grams", "Gram"),
                    ("Pieces", "Pcs"),
                    ("Sets", "Set"),
                    ("Dozen", "Dozen"),
                ],
                default="Pieces",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="price",
            name="wholesale_pay_type",
            field=models.CharField(
                choices=[
                    ("Kilograms", "Kg"),
                    ("Grams", "Gram"),
                    ("Pieces", "Pcs"),
                    ("Sets", "Set"),
                    ("Dozen", "Dozen"),
                ],
                default="Pieces",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="stock_type",
            field=models.CharField(
                choices=[
                    ("Kilograms", "Kg"),
                    ("Grams", "Gram"),
                    ("Pieces", "Pcs"),
                    ("Sets", "Set"),
                    ("Dozen", "Dozen"),
                ],
                default="Pieces",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="weight_type",
            field=models.CharField(
                choices=[("Kilograms", "Kg"), ("Grams", "Gram")],
                default="Kilograms",
                max_length=20,
            ),
        ),
    ]
