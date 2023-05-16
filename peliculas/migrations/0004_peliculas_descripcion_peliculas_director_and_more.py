# Generated by Django 4.1.7 on 2023-04-09 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0003_categoria_alter_peliculas_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='peliculas',
            name='descripcion',
            field=models.TextField(default='Sin descripción'),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='director',
            field=models.CharField(default='Sin director', max_length=160),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peliculas',
            name='duracion',
            field=models.CharField(default='103 min', max_length=55),
            preserve_default=False,
        ),
    ]
