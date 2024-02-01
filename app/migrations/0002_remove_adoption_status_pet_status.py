# Generated by Django 5.0 on 2024-02-01 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoption',
            name='status',
        ),
        migrations.AddField(
            model_name='pet',
            name='status',
            field=models.CharField(choices=[('Adopted', 'Adopted'), ('Available', 'Available')], default='Available', max_length=200),
        ),
    ]