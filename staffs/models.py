from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class mark(models.Model):
    mark = models.CharField(max_length=5,blank=True)


class subject(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Document(models.Model):
    document = models.FileField(upload_to='')
    subject = models.ForeignKey(subject, on_delete='CASCADE')
    ct1 = (
        ('pre k.g', 'PRE KG'),
        ('l.k.g', 'LKG'),
        ('u.k.g', 'UKG'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('General', 'GENERAL')
    )
    Class = models.CharField(max_length=10,choices=ct1)
    description = models.CharField(max_length=5000)
    upload_by = models.ForeignKey('auth.User',related_name='uploaded_documents',on_delete= 'CASCADE')
    choices = {
        ('question_paper', 'Question Paper'),
        ('Book', 'BOOK'),
        ('Notes', 'NOTES'),
        ('Magazines', 'MAGAZINES'),
        ('others', 'OTHERS'),



    }
    Document_type = models.CharField(max_length=25, choices=choices)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.document.name

class Test_and_exam(models.Model):
    Test = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.Test

class classdivision(models.Model):
    Class = models.CharField(max_length=15,default='1:A',help_text='example :LKG:A UKG:A 1:A 1:B 2:A 2:B......12:A 12:B 12:C 12:D ')
    Tests = models.ManyToManyField(Test_and_exam, blank= True)
    Subject = models.ManyToManyField(subject)
    def __str__(self):
        return self.Class

class staff(models.Model):
    Name = models.ForeignKey(User,on_delete= 'CASCADE')

    #Level_Choices = (
        #('tamil','TAMIL'),
        #( 'english','ENGLISH'),
        #( 'maths','MATHS'),
        #('physics','PHYSICS'),
        #('chemistry','CHEMISTRY'),
        #('social', 'SOCIAL'),
        #('science', 'SCIENCE'),
        #( 'botany','BOTANY'),
        #('zoology','ZOOLOGY'),
        #('history','HISTORY'),
        #('geography','GEOGRAPHY'),
        #('economics','ECONOMICS'),
       # ('accounts','ACCOUNTS'),
       # ( 'business_maths','BUSINESS MATHS'),
      #  ( 'p_e_t','PHYSICAL EDUCATION'),
     #   ('g_k','GENERAL KNOWLEDGE'),
    #    ('hindi','HINDI'),
   #     ('others','OTHERS')
  #  )
    #Subject = models.CharField(max_length=20, choices= Level_Choices, default=  'NONE')


    Subject = models.ManyToManyField(subject)
    classes =  models.ManyToManyField(classdivision)
    def __str__(self):
        return self.Name.username










