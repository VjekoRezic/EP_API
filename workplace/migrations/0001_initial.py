# Generated by Django 4.2.4 on 2023-08-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='workplace name')),
                ('code', models.CharField(max_length=5, verbose_name='workplace code')),
                ('points', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='workplace points')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='is_deleted')),
            ],
        ),
    ]