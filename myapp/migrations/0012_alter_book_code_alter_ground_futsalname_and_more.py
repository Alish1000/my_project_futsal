# Generated by Django 4.0 on 2022-03-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20220321_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='code',
            field=models.CharField(default='CSJU6', max_length=5),
        ),
        migrations.AlterField(
            model_name='ground',
            name='FutsalName',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ground',
            name='code',
            field=models.CharField(default='CSJU6', max_length=5),
        ),
    ]