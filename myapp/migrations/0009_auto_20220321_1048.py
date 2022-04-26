# Generated by Django 3.0.5 on 2022-03-21 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20220321_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='FutsalName',
            field=models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='myapp.ground'),
        ),
        migrations.AlterField(
            model_name='book',
            name='code',
            field=models.CharField(default='cbdWg', max_length=5),
        ),
        migrations.AlterField(
            model_name='ground',
            name='code',
            field=models.CharField(default='cbdWg', max_length=5),
        ),
    ]