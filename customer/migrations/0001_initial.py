# Generated by Django 3.2.12 on 2022-03-30 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=300)),
                ('is_Caterer', models.BooleanField(default=False)),
                ('is_Customer', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
    ]