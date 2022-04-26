# Generated by Django 3.0.5 on 2022-03-21 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20220321_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='code',
            field=models.CharField(default='ymtUu', max_length=5),
        ),
        migrations.AlterField(
            model_name='ground',
            name='FutsalName',
            field=models.CharField(choices=[('Shantinagar', 'Shantinagar'), ('Shrestha Futsal', 'Shrestha Futsal'), ('Dhuku', 'Dhuku'), ('Hardik Futsal', 'Hardik Futsal'), ('Green Wish', 'Green Wish'), ('Dhanwontari', 'Dhanwontari'), ('Shankhamul', 'Shankhamul'), ('Imadol', 'Imadol'), ('Chyasal', 'Chyasal')], max_length=30),
        ),
        migrations.AlterField(
            model_name='ground',
            name='code',
            field=models.CharField(default='ymtUu', max_length=5),
        ),
    ]
