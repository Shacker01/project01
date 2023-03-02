# Generated by Django 4.1.7 on 2023-03-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20230226_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicines',
            old_name='quantity',
            new_name='quantity_in_ml',
        ),
        migrations.RenameField(
            model_name='medicines',
            old_name='types',
            new_name='type_of_drug',
        ),
        migrations.AlterField(
            model_name='medicines',
            name='name_of_medicine_used',
            field=models.CharField(max_length=15),
        ),
    ]