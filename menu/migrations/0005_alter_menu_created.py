# Generated by Django 3.2.12 on 2022-03-31 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20220331_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
