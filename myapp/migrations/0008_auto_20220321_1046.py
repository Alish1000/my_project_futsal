# Generated by Django 3.0.5 on 2022-03-21 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_book_code_alter_ground_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='code',
            field=models.CharField(default='CT32m', max_length=5),
        ),
        migrations.AlterField(
            model_name='ground',
            name='FutsalName',
            field=models.CharField(choices=[('Shantinagar', 'Shantinagar'), ('Green Wish', 'Green Wish')], default='Sankhamul', max_length=30),
        ),
        migrations.AlterField(
            model_name='ground',
            name='code',
            field=models.CharField(default='CT32m', max_length=5),
        ),
    ]