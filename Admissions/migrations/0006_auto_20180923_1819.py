# Generated by Django 2.1 on 2018-09-23 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admissions', '0005_auto_20180921_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholar',
            name='Contact_number',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]
