# Generated by Django 4.0.2 on 2022-02-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='desc',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='dis_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]