# Generated by Django 2.0.6 on 2018-07-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20180629_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
