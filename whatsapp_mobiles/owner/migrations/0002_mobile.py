# Generated by Django 4.1.5 on 2023-01-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_name', models.CharField(max_length=100)),
                ('mobile_brand', models.CharField(max_length=50)),
                ('mobile_rate', models.FloatField(default='')),
                ('mobile_image', models.ImageField(upload_to='mobiles/')),
            ],
        ),
    ]
