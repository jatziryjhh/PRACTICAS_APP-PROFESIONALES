# Generated by Django 5.1.5 on 2025-02-13 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_producto_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='imagen',
            new_name='Imagen',
        ),
    ]
