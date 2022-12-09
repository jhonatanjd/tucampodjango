# Generated by Django 4.1.3 on 2022-12-07 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0017_productos_delete_prueba_alter_registro_ciudad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=254)),
                ('cantidad', models.CharField(max_length=254)),
                ('precio_kgs', models.CharField(max_length=254)),
                ('precio_total', models.CharField(max_length=254)),
                ('ciudad', models.CharField(max_length=254)),
                ('fecha_disponible', models.CharField(max_length=254)),
                ('ofrece_transporte', models.CharField(max_length=254)),
                ('descripcion', models.CharField(max_length=254)),
                ('estado', models.CharField(max_length=254)),
            ],
            options={
                'db_table': 'invenatrio',
            },
        ),
        migrations.AlterField(
            model_name='productos',
            name='cantidad',
            field=models.CharField(choices=[('80 kgs', '80 kgs'), ('60 kgs', '60 kgs'), ('70 kgs', '70 kgs'), ('50 kgs', '50 kgs'), ('90 kgs', '90 kgs'), ('100 kgs', '100 kgs')], max_length=254),
        ),
        migrations.AlterField(
            model_name='productos',
            name='ciudad',
            field=models.CharField(choices=[('barranquilla', 'barranquilla'), ('rionegro', 'rionegro'), ('boyaca', 'boyaca'), ('magangue', 'magangue'), ('cartagena', 'cartagena'), ('tunja', 'tunja'), ('facatativa', 'facatativa'), ('zipaquira', 'zipaquira'), ('bogota', 'bogota'), ('girardot', 'girardot'), ('cali', 'cali'), ('arauca', 'arauca'), ('cucuta', 'cucuta'), ('el carmen de bolivar', 'el carmen de bolivar'), ('fusagasuga', 'fusagasuga'), ('turbo', 'turbo'), ('caucasia', 'caucasia'), ('medellin', 'medellin'), ('leticia', 'leticia'), ('apartado', 'apartado'), ('sabanalarga', 'sabanalarga')], max_length=254),
        ),
        migrations.AlterField(
            model_name='productos',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'pendiente'), ('Disponible', 'disponible'), ('no disponible', 'no disponible')], max_length=254),
        ),
        migrations.AlterField(
            model_name='productos',
            name='ofrece_transporte',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=254),
        ),
        migrations.AlterField(
            model_name='productos',
            name='producto',
            field=models.CharField(choices=[('mandarina', 'mandarina'), ('manzana', 'manzana'), ('banano', 'banano'), ('fresa', 'fresa'), ('papaya', 'papaya'), ('uvas', 'uvas')], max_length=254),
        ),
        migrations.AlterField(
            model_name='registro',
            name='ciudad',
            field=models.CharField(choices=[('barranquilla', 'barranquilla'), ('rionegro', 'rionegro'), ('boyaca', 'boyaca'), ('magangue', 'magangue'), ('cartagena', 'cartagena'), ('tunja', 'tunja'), ('facatativa', 'facatativa'), ('zipaquira', 'zipaquira'), ('bogota', 'bogota'), ('girardot', 'girardot'), ('cali', 'cali'), ('arauca', 'arauca'), ('cucuta', 'cucuta'), ('el carmen de bolivar', 'el carmen de bolivar'), ('fusagasuga', 'fusagasuga'), ('turbo', 'turbo'), ('caucasia', 'caucasia'), ('medellin', 'medellin'), ('leticia', 'leticia'), ('apartado', 'apartado'), ('sabanalarga', 'sabanalarga')], max_length=40),
        ),
        migrations.AlterField(
            model_name='registro',
            name='rol',
            field=models.CharField(choices=[('eres cliente', 'eres cliente'), ('eres productor', 'eres productor'), ('eres conductor', 'eres conducto')], max_length=254),
        ),
    ]
