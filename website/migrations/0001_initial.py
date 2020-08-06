# Generated by Django 3.0.8 on 2020-08-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=2)),
                ('label', models.CharField(max_length=1)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
