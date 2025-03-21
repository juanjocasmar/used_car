# Generated by Django 5.1.5 on 2025-02-14 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('anio', models.IntegerField()),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_venta', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estado', models.CharField(choices=[('Disponible', 'Disponible'), ('Vendido', 'Vendido')], default='Disponible', max_length=20)),
            ],
        ),
    ]
