# Generated by Django 5.0.6 on 2024-06-04 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('receta', models.BooleanField()),
                ('autor', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Comida',
        ),
        migrations.RenameField(
            model_name='postres',
            old_name='nombre',
            new_name='titulo',
        ),
    ]
