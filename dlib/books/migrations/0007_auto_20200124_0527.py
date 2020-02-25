# Generated by Django 2.2.9 on 2020-01-24 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200122_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.CharField(default='0000', max_length=5),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.FileField(max_length=128, upload_to='static/uploads/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='filename',
            field=models.FileField(max_length=128, upload_to='static/uploads/'),
        ),
    ]