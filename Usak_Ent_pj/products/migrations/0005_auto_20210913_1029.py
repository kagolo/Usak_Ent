# Generated by Django 3.2.6 on 2021-09-13 17:29

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Men_wear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.CharField(max_length=200, unique=True)),
                ('item_name', models.CharField(max_length=200)),
                ('stock_date', models.DateField(auto_now_add=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('item_image', models.ImageField(upload_to='')),
                ('item_price', models.CharField(max_length=200)),
                ('item_status', models.CharField(choices=[('USED', 'USED'), ('NEW', 'NEW')], max_length=100)),
                ('item_special_deal', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=200)),
                ('item_special_offer', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=200)),
                ('item_sub_image1', models.ImageField(upload_to='')),
                ('item_sub_image2', models.ImageField(upload_to='')),
                ('item_sub_image3', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Scarves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.CharField(max_length=200, unique=True)),
                ('item_name', models.CharField(max_length=200)),
                ('stock_date', models.DateField(auto_now_add=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('item_image', models.ImageField(upload_to='')),
                ('item_price', models.CharField(max_length=200)),
                ('item_status', models.CharField(choices=[('USED', 'USED'), ('NEW', 'NEW')], max_length=100)),
                ('item_special_deal', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=200)),
                ('item_special_offer', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=200)),
                ('item_sub_image1', models.ImageField(upload_to='')),
                ('item_sub_image2', models.ImageField(upload_to='')),
                ('item_sub_image3', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Shiphon_brouses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.CharField(max_length=200, unique=True)),
                ('item_name', models.CharField(max_length=200)),
                ('stock_date', models.DateField(auto_now_add=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('item_image', models.ImageField(upload_to='')),
                ('item_price', models.CharField(max_length=200)),
                ('item_status', models.CharField(choices=[('USED', 'USED'), ('NEW', 'NEW')], max_length=100)),
                ('item_special_deal', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=200)),
                ('item_special_offer', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=200)),
                ('item_sub_image1', models.ImageField(upload_to='')),
                ('item_sub_image2', models.ImageField(upload_to='')),
                ('item_sub_image3', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='bags',
            name='item_price',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bags',
            name='item_special_deal',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bags',
            name='item_special_offer',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bags',
            name='item_status',
            field=models.CharField(choices=[('USED', 'USED'), ('NEW', 'NEW')], default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bags',
            name='item_sub_image1',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bags',
            name='item_sub_image2',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bags',
            name='item_sub_image3',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]