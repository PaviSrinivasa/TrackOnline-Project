# Generated by Django 3.1.7 on 2021-06-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0004_auto_20210518_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]