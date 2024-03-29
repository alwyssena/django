# Generated by Django 4.2.3 on 2024-03-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('Picture', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('username', models.CharField(max_length=30)),
                ('Email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('confirm_password', models.CharField(max_length=30)),
                ('line_1', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
            ],
        ),
    ]
