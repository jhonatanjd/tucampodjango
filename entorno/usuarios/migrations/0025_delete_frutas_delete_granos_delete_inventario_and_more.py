# Generated by Django 4.1.3 on 2022-12-08 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0024_alter_inventario_cantidad_alter_inventario_ciudad_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='frutas',
        ),
        migrations.DeleteModel(
            name='granos',
        ),
        migrations.DeleteModel(
            name='inventario',
        ),
        migrations.DeleteModel(
            name='legumbres',
        ),
        migrations.DeleteModel(
            name='productos',
        ),
        migrations.DeleteModel(
            name='verduras',
        ),
        migrations.AlterField(
            model_name='registro',
            name='ciudad',
            field=models.CharField(choices=[('apartado', 'apartado'), ('cartagena', 'cartagena'), ('turbo', 'turbo'), ('tunja', 'tunja'), ('medellin', 'medellin'), ('magangue', 'magangue'), ('zipaquira', 'zipaquira'), ('el carmen de bolivar', 'el carmen de bolivar'), ('sabanalarga', 'sabanalarga'), ('caucasia', 'caucasia'), ('cali', 'cali'), ('barranquilla', 'barranquilla'), ('cucuta', 'cucuta'), ('girardot', 'girardot'), ('bogota', 'bogota'), ('facatativa', 'facatativa'), ('boyaca', 'boyaca'), ('leticia', 'leticia'), ('fusagasuga', 'fusagasuga'), ('rionegro', 'rionegro'), ('arauca', 'arauca')], max_length=40),
        ),
        migrations.AlterField(
            model_name='registro',
            name='rol',
            field=models.CharField(choices=[('eres productor', 'eres productor'), ('eres cliente', 'eres cliente'), ('eres conductor', 'eres conducto')], max_length=254),
        ),
    ]
