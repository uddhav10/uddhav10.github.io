# Generated by Django 4.2.1 on 2023-06-01 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_dcb', '0002_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.AddField(
            model_name='complaint',
            name='created_by',
            field=models.IntegerField(default=1),
        ),
    ]