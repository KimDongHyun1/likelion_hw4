# Generated by Django 2.2.2 on 2019-06-20 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
