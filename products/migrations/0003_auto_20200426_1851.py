# Generated by Django 3.0.4 on 2020-04-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200324_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]