# Generated by Django 4.0.2 on 2022-02-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField(max_length=1000)),
                ('image', models.ImageField(default='', upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=2)),
                ('dis_price', models.DecimalField(decimal_places=2, max_digits=2)),
                ('in_stock', models.IntegerField()),
                ('is_lattest', models.BooleanField(default=True)),
                ('catagory', models.CharField(choices=[('men', 'men'), ('wahmen', 'women'), ('kid', "kid's")], max_length=6)),
            ],
        ),
    ]
