# Generated by Django 4.1.4 on 2022-12-22 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('brand', models.CharField(default='un-branded', max_length=50)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'products',
            },
        ),
    ]
