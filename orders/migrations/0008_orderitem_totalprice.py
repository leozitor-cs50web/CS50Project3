# Generated by Django 3.0.6 on 2020-05-25 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='totalPrice',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4),
            preserve_default=False,
        ),
    ]
