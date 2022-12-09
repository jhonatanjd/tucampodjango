# Generated by Django 4.1.3 on 2022-12-07 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0019_frutas_granos_legumbres_verduras_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='cantidad',
            field=models.CharField(choices=[('70 kgs', '70 kgs'), ('80 kgs', '80 kgs'), ('100 kgs', '100 kgs'), ('60 kgs', '60 kgs'), ('90 kgs', '90 kgs'), ('50 kgs', '50 kgs')], max_length=254),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='ciudad',
            field=models.CharField(choices=[('tunja', 'tunja'), ('zipaquira', 'zipaquira'), ('bogota', 'bogota'), ('rionegro', 'rionegro'), ('facatativa', 'facatativa'), ('caucasia', 'caucasia'), ('barranquilla', 'barranquilla'), ('girardot', 'girardot'), ('apartado', 'apartado'), ('arauca', 'arauca'), ('cartagena', 'cartagena'), ('magangue', 'magangue'), ('cali', 'cali'), ('turbo', 'turbo'), ('fusagasuga', 'fusagasuga'), ('leticia', 'leticia'), ('cucuta', 'cucuta'), ('el carmen de bolivar', 'el carmen de bolivar'), ('sabanalarga', 'sabanalarga'), ('medellin', 'medellin'), ('boyaca', 'boyaca')], max_length=254),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='estado',
            field=models.CharField(choices=[('Disponible', 'disponible'), ('pendiente', 'pendiente'), ('no disponible', 'no disponible')], max_length=254),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='ofrece_transporte',
            field=models.CharField(choices=[('NO', 'NO'), ('SI', 'SI')], max_length=254),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='producto',
            field=models.CharField(choices=[('uvas', 'uvas'), ('fresa', 'fresa'), ('banano', 'banano'), ('papaya', 'papaya'), ('mandarina', 'mandarina'), ('manzana', 'manzana')], max_length=254),
        ),
        migrations.AlterField(
            model_name='productos',
            name='cantidad',
            field=models.CharField(choices=[('70 kgs', '70 kgs'), ('80 kgs', '80 kgs'), ('100 kgs', '100 kgs'), ('60 kgs', '60 kgs'), ('90 kgs', '90 kgs'), ('50 kgs', '50 kgs')], max_length=254),
        ),
        migrations.AlterField(
            model_name='productos',
            name='ciudad',
            field=models.CharField(choices=[('tunja', 'tunja'), ('zipaquira', 'zipaquira'), ('bogota', 'bogota'), ('rionegro', 'rionegro'), ('facatativa', 'facatativa'), ('caucasia', 'caucasia'), ('barranquilla', 'barranquilla'), ('girardot', 'girardot'), ('apartado', 'apartado'), ('arauca', 'arauca'), ('cartagena', 'cartagena'), ('magangue', 'magangue'), ('cali', 'cali'), ('turbo', 'turbo'), ('fusagasuga', 'fusagasuga'), ('leticia', 'leticia'), ('cucuta', 'cucuta'), ('el carmen de bolivar', 'el carmen de bolivar'), ('sabanalarga', 'sabanalarga'), ('medellin', 'medellin'), ('boyaca', 'boyaca')], max_length=254),
        ),
        migrations.AlterField(
            model_name='productos',
            name='estado',
            field=models.CharField(choices=[('Disponible', 'disponible'), ('pendiente', 'pendiente'), ('no disponible', 'no disponible')], max_length=254),
        ),
        migrations.AlterField(
            model_name='productos',
            name='producto',
            field=models.CharField(choices=[('uvas', 'uvas'), ('fresa', 'fresa'), ('banano', 'banano'), ('papaya', 'papaya'), ('mandarina', 'mandarina'), ('manzana', 'manzana')], max_length=254),
        ),
        migrations.AlterField(
            model_name='registro',
            name='ciudad',
            field=models.CharField(choices=[('tunja', 'tunja'), ('zipaquira', 'zipaquira'), ('bogota', 'bogota'), ('rionegro', 'rionegro'), ('facatativa', 'facatativa'), ('caucasia', 'caucasia'), ('barranquilla', 'barranquilla'), ('girardot', 'girardot'), ('apartado', 'apartado'), ('arauca', 'arauca'), ('cartagena', 'cartagena'), ('magangue', 'magangue'), ('cali', 'cali'), ('turbo', 'turbo'), ('fusagasuga', 'fusagasuga'), ('leticia', 'leticia'), ('cucuta', 'cucuta'), ('el carmen de bolivar', 'el carmen de bolivar'), ('sabanalarga', 'sabanalarga'), ('medellin', 'medellin'), ('boyaca', 'boyaca')], max_length=40),
        ),
    ]
