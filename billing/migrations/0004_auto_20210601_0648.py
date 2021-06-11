# Generated by Django 3.0.8 on 2021-06-01 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_auto_20210531_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ord_price',
            new_name='tot_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='order',
            name='prod',
        ),
        migrations.CreateModel(
            name='Order_detail',
            fields=[
                ('det_id', models.AutoField(primary_key=True, serialize=False)),
                ('ord_qty', models.BigIntegerField()),
                ('tot_price', models.FloatField(max_length=100)),
                ('pay_mode', models.CharField(max_length=50)),
                ('ord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.Order')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.Products')),
            ],
            options={
                'db_table': 'tbl_order_details',
            },
        ),
    ]
