# Generated by Django 3.0.8 on 2021-06-01 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0004_auto_20210601_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_detail',
            name='tot_price',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=12, null=True),
        ),
    ]
