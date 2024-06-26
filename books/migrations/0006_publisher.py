# Generated by Django 5.0.4 on 2024-05-08 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_comment_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name', 'code'], name='books_publi_name_e27346_idx')],
            },
        ),
    ]
