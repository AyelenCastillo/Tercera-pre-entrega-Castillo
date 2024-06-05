# Generated by Django 5.0.6 on 2024-05-30 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_entregable_estudiante_email_profesor_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('receta', models.BooleanField()),
                ('autor', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Postres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('receta', models.BooleanField()),
                ('autor', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameModel(
            old_name='Estudiante',
            new_name='Registro',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
