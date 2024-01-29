# Generated by Django 5.0 on 2024-01-29 05:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0003_remove_owner_user_remove_pet_owner_remove_pet_type_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
                ('picture', models.ImageField(upload_to='images/pets')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=13, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='images/profile_pics')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Adoption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Adopted', 'Adopted'), ('Available', 'Available')], max_length=200, null=True)),
                ('note', models.CharField(max_length=1000, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.owner')),
                ('pet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.pet')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='type',
            field=models.ManyToManyField(to='app.type'),
        ),
    ]
