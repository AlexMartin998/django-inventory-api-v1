# Generated by Django 5.0.4 on 2024-05-07 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]