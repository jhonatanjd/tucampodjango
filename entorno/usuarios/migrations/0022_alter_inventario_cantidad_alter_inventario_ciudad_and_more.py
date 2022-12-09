# Generated by Django 4.1.3 on 2022-12-08 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0021_alter_inventario_cantidad_alter_inventario_ciudad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='cantidad',
            field=models.CharField(choices=[('70 kgs', '70 kgs'), ('60 kgs', '60 kgs'), ('90 kgs', '90 kgs'), ('100 kgs', '100 kgs'), ('80 kgs', '80 kgs'), ('50 kgs', '50 kgs')], max_length=254),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='ciudad',
            field=models.CharField(choices=[('boyaca', 'boyaca'), ('apartado', 'apartado'), ('tunja', 'tunja'), ('rionegro', 'rionegro'), ('el carmen de bolivar', 'el carmen de bolivar'), ('medellin', 'medellin'), ('leticia', 'leticia'), ('fusagasuga', 'fusagasuga'), ('zipaquira', 'zipaquira'), ('turbo', 'turbo'), ('girardot', 'girardot'), ('cartagena', 'cartagena'), ('cali', 'cali'), ('arauca', 'arauca'), ('barranquilla', 'barranquilla'), ('facatativa', 'facatativa'), ('bogota', 'bogota'), ('magangue', 'magangue'), ('cucuta', 'cucuta'), ('caucasia', 'caucasia'), ('sabanalarga', 'sabanalarga')], max_length=254),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'pendiente'), ('no disponible', 'no disponible'), ('Disponible', 'disponible')], max_length=254),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='ofrece_transporte',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=254),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='producto',
            field=models.CharField(choices=[('mandarina', 'mandarina'), ('uvas', 'uvas'), ('manzana', 'manzana'), ('papaya', 'papaya'), ('banano', 'banano'), ('fresa', 'fresa')], max_length=254),
        ),
        migrations.AlterField(
            model_name='productos',
            name='cantidad',
            field=models.CharField(choices=[('70 kgs', '70 kgs'), ('60 kgs', '60 kgs'), ('90 kgs', '90 kgs'), ('100 kgs', '100 kgs'), ('80 kgs', '80 kgs'), ('50 kgs', '50 kgs')], max_length=254),
        ),
        migrations.AlterField(
            model_name='productos',
            name='ciudad',
            field=models.CharField(choices=[('boyaca', 'boyaca'), ('apartado', 'apartado'), ('tunja', 'tunja'), ('rionegro', 'rionegro'), ('el carmen de bolivar', 'el carmen de bolivar'), ('medellin', 'medellin'), ('leticia', 'leticia'), ('fusagasuga', 'fusagasuga'), ('zipaquira', 'zipaquira'), ('turbo', 'turbo'), ('girardot', 'girardot'), ('cartagena', 'cartagena'), ('cali', 'cali'), ('arauca', 'arauca'), ('barranquilla', 'barranquilla'), ('facatativa', 'facatativa'), ('bogota', 'bogota'), ('magangue', 'magangue'), ('cucuta', 'cucuta'), ('caucasia', 'caucasia'), ('sabanalarga', 'sabanalarga')], max_length=254),
        ),
        migrations.AlterField(
            model_name='productos',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'pendiente'), ('no disponible', 'no disponible'), ('Disponible', 'disponible')], max_length=254),
        ),
        migrations.AlterField(
            model_name='productos',
            name='ofrece_transporte',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=254),
        ),
        migrations.AlterField(
            model_name='productos',
            name='producto',
            field=models.CharField(choices=[('mandarina', 'mandarina'), ('uvas', 'uvas'), ('manzana', 'manzana'), ('papaya', 'papaya'), ('banano', 'banano'), ('fresa', 'fresa')], max_length=254),
        ),
        migrations.AlterField(
            model_name='registro',
            name='ciudad',
            field=models.CharField(choices=[('boyaca', 'boyaca'), ('apartado', 'apartado'), ('tunja', 'tunja'), ('rionegro', 'rionegro'), ('el carmen de bolivar', 'el carmen de bolivar'), ('medellin', 'medellin'), ('leticia', 'leticia'), ('fusagasuga', 'fusagasuga'), ('zipaquira', 'zipaquira'), ('turbo', 'turbo'), ('girardot', 'girardot'), ('cartagena', 'cartagena'), ('cali', 'cali'), ('arauca', 'arauca'), ('barranquilla', 'barranquilla'), ('facatativa', 'facatativa'), ('bogota', 'bogota'), ('magangue', 'magangue'), ('cucuta', 'cucuta'), ('caucasia', 'caucasia'), ('sabanalarga', 'sabanalarga')], max_length=40),
        ),
        migrations.AlterField(
            model_name='registro',
            name='rol',
            field=models.CharField(choices=[('eres conductor', 'eres conducto'), ('eres productor', 'eres productor'), ('eres cliente', 'eres cliente')], max_length=254),
        ),
    ]