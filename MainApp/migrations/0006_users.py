# Generated by Django 5.0.6 on 2024-06-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_comida_postres_rename_estudiante_registro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=20)),
            ],
        ),
    ]