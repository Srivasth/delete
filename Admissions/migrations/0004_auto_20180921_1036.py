# Generated by Django 2.1 on 2018-09-21 05:06

from django.db import migrations, models
import school.checkbox


class Migration(migrations.Migration):

    dependencies = [
        ('Admissions', '0003_auto_20180915_2315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='absent_date',
            options={'verbose_name': 'Today'},
        ),
        migrations.AlterField(
            model_name='scholar',
            name='Absent_on',
            field=school.checkbox.CheckBoxManyToMany(blank=True, to='Admissions.Absent_date'),
        ),
        migrations.AlterField(
            model_name='scholar',
            name='Gender',
            field=models.CharField(choices=[('female', 'FEMALE'), ('others', 'OTHERS'), ('male', 'MALE')], default='MALE', max_length=10),
        ),
    ]
