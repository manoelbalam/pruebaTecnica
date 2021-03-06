# Generated by Django 4.0.6 on 2022-07-14 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserAccess', models.CharField(max_length=50, verbose_name='UserAccess')),
                ('PassAccess', models.CharField(max_length=50, verbose_name='PassAccess')),
                ('TokenAccess', models.CharField(max_length=240, verbose_name='TokenAccess')),
                ('ExpirationAccess', models.DateField(verbose_name='ExpirationAccess')),
            ],
        ),
    ]
