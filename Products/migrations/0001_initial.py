# Generated by Django 3.2.14 on 2023-02-28 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductForCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=244)),
                ('Product_Category', models.CharField(max_length=255)),
                ('Product_price', models.IntegerField()),
                ('Product_Discription', models.CharField(max_length=1000)),
                ('Product_Stock', models.IntegerField(max_length=255)),
                ('Product_Image', models.FileField(upload_to='Customer_products')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]