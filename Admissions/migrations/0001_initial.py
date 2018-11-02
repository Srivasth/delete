# Generated by Django 2.1 on 2018-09-15 17:40

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staffs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Absent_date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('absent_on', models.DateField(blank=True, default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Information', models.CharField(blank=True, max_length=2000)),
                ('infolink', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Scholar',
            fields=[
                ('student_first_name', models.CharField(max_length=200)),
                ('student_last_name', models.CharField(max_length=100)),
                ('Fathers_name', models.CharField(max_length=1000)),
                ('Contact_number', models.IntegerField(max_length=12, primary_key=True, serialize=False)),
                ('Date_of_Birth', models.DateField()),
                ('Gender', models.CharField(choices=[('female', 'FEMALE'), ('others', 'OTHERS'), ('male', 'MALE')], default='MALE', max_length=10)),
                ('email_id', models.EmailField(max_length=100)),
                ('Address', models.CharField(max_length=500)),
                ('Level', models.CharField(choices=[('INQUIRY', 'Inquiry'), ('APPLICANT', 'applicant'), ('CANDIDATE', 'candidate'), ('DECISION', 'decision'), ('ACCEPTED', 'accepted'), ('REGISTERED', 'registered'), ('DISCONTINUED', 'Discontinued')], default='INQUIRY', max_length=100)),
                ('Previous_school', models.CharField(blank=True, max_length=200)),
                ('Password', models.CharField(default='STUDENT', max_length=20)),
                ('Absent_on', models.ManyToManyField(blank=True, to='Admissions.Absent_date')),
                ('Class', models.ForeignKey(on_delete='CASCADE', to='staffs.classdivision')),
                ('Class_teacher', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
