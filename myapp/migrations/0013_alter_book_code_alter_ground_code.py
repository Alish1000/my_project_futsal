# Generated by Django 4.0 on 2022-03-23 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_book_code_alter_ground_futsalname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='code',
            field=models.CharField(default='SFKIG', max_length=5),
        ),
        migrations.AlterField(
            model_name='ground',
            name='code',
            field=models.CharField(default='SFKIG', max_length=5),
        ),
    ]