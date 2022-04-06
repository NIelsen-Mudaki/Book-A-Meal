# Generated by Django 3.2.12 on 2022-04-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'NewsLetter',
            },
        ),
    ]