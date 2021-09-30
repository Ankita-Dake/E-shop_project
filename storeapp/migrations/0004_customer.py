# Generated by Django 3.2.6 on 2021-08-31 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
