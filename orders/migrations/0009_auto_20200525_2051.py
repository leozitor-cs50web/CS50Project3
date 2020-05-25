# Generated by Django 3.0.6 on 2020-05-25 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_orderitem_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='status',
            field=models.CharField(choices=[(0, 'Initiated'), (1, 'Pending'), (2, 'Completed')], default=0, max_length=64),
        ),
    ]
