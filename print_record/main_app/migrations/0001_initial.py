<<<<<<< HEAD
# Generated by Django 5.0.6 on 2024-06-07 13:13

=======
# Generated by Django 5.0.6 on 2024-06-07 13:06

import django.db.models.deletion
from django.conf import settings
>>>>>>> main
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
=======
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> main
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
                ('date_hired', models.DateField()),
                ('date_terminated', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
=======
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollnum', models.IntegerField()),
                ('printed_pages', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
>>>>>>> main
            ],
        ),
    ]
