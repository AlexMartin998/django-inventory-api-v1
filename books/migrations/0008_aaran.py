# Generated by Django 5.0.4 on 2024-05-08 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_aba'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]