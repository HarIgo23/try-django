# Generated by Django 2.2.3 on 2020-01-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200107_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]