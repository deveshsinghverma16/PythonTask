# Generated by Django 3.1.5 on 2021-01-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='paymentmodel',
            name='cardNumber',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='paymentmodel',
            name='secNumber',
            field=models.CharField(max_length=3),
        ),
    ]
