from django.db import models
from datetime import date
from django.contrib.auth.models import User
from staffs.models import classdivision, subject
from django.contrib.postgres.fields import ArrayField

class info(models.Model):
    Information = models.CharField(max_length=2000, blank=True)
    infolink = models.CharField(max_length=150,blank = True)

class Absent_date(models.Model):
    absent_on = models.DateField(default= date.today, blank= True)
    class Meta:
        verbose_name = "Today"

    def __str__(self):
        return str(self.absent_on)

class Scholar(models.Model):

    student_first_name = models.CharField(max_length=200)
    student_last_name= models.CharField(max_length=100)
    Fathers_name= models.CharField(max_length=1000)
    Contact_number =  models.CharField(max_length= 12, primary_key= True)
    Date_of_Birth = models.DateField()
    Gender_choices = {
        ( 'male','MALE'),
        ('female', 'FEMALE'),
        ('others', 'OTHERS'),
    }
    Gender = models.CharField(max_length=10,choices=Gender_choices,default='MALE')

    email_id =  models.EmailField(max_length=100)
    Address = models.CharField(max_length=500)
    Level_Choices = (
        ('INQUIRY', 'Inquiry'),
        ('APPLICANT', 'applicant'),
        ('CANDIDATE', 'candidate'),
        ('DECISION', 'decision'),
        ('ACCEPTED', 'accepted'),
        ('REGISTERED', 'registered'),
        ('DISCONTINUED','Discontinued')

    )
    Level = models.CharField(max_length=100, choices=Level_Choices, default='INQUIRY')
    Previous_school = models.CharField(max_length=200, blank= True)
    Class = models.ForeignKey(classdivision,on_delete='CASCADE')
    Password = models.CharField(max_length=20,default='STUDENT')
    Class_teacher  = models.ForeignKey(User,on_delete='CASCADE')
    Absent_on = models.ManyToManyField(Absent_date,blank=True)
    Test1_subject1 = models.CharField(max_length=4, blank=True)
    Test1_subject2 = models.CharField(max_length=4, blank=True)
    Test1_subject3 = models.CharField(max_length=4, blank=True)
    Test1_subject4 = models.CharField(max_length=4, blank=True)
    Test1_subject5 = models.CharField(max_length=4, blank=True)
    Test1_subject6 = models.CharField(max_length=4, blank=True)
    Test1_subject7 = models.CharField(max_length=4, blank=True)
    Test1_subject8 = models.CharField(max_length=4, blank=True)
    Test1_subject9 = models.CharField(max_length=4, blank=True)
    Test1_subject10 = models.CharField(max_length=4, blank=True)
    Test1_Rank = models.CharField(max_length=4,blank=True)


    Test2_subject1 = models.CharField(max_length=4, blank=True)
    Test2_subject2 = models.CharField(max_length=4, blank=True)
    Test2_subject3 = models.CharField(max_length=4, blank=True)
    Test2_subject4 = models.CharField(max_length=4, blank=True)
    Test2_subject5 = models.CharField(max_length=4, blank=True)
    Test2_subject6 = models.CharField(max_length=4, blank=True)
    Test2_subject7 = models.CharField(max_length=4, blank=True)
    Test2_subject8 = models.CharField(max_length=4, blank=True)
    Test2_subject9 = models.CharField(max_length=4, blank=True)
    Test2_subject10 = models.CharField(max_length=4, blank=True)
    Test2_Rank = models.CharField(max_length=4, blank=True)
    Test3_subject1 = models.CharField(max_length=4, blank=True)
    Test3_subject2 = models.CharField(max_length=4, blank=True)
    Test3_subject3 = models.CharField(max_length=4, blank=True)
    Test3_subject4 = models.CharField(max_length=4, blank=True)
    Test3_subject5 = models.CharField(max_length=4, blank=True)
    Test3_subject6 = models.CharField(max_length=4, blank=True)
    Test3_subject7 = models.CharField(max_length=4, blank=True)
    Test3_subject8 = models.CharField(max_length=4, blank=True)
    Test3_subject9 = models.CharField(max_length=4, blank=True)
    Test3_subject10 = models.CharField(max_length=4, blank=True)
    Test3_Rank = models.CharField(max_length=4, blank=True)

    Test4_subject1 = models.CharField(max_length=4, blank=True)
    Test4_subject2 = models.CharField(max_length=4, blank=True)
    Test4_subject3 = models.CharField(max_length=4, blank=True)
    Test4_subject4 = models.CharField(max_length=4, blank=True)
    Test4_subject5 = models.CharField(max_length=4, blank=True)
    Test4_subject6 = models.CharField(max_length=4, blank=True)
    Test4_subject7 = models.CharField(max_length=4, blank=True)
    Test4_subject8 = models.CharField(max_length=4, blank=True)
    Test4_subject9 = models.CharField(max_length=4, blank=True)
    Test4_subject10 = models.CharField(max_length=4, blank=True)
    Test4_Rank = models.CharField(max_length=4, blank=True)

    Test5_subject1 = models.CharField(max_length=4, blank=True)
    Test5_subject2 = models.CharField(max_length=4, blank=True)
    Test5_subject3 = models.CharField(max_length=4, blank=True)
    Test5_subject4 = models.CharField(max_length=4, blank=True)
    Test5_subject5 = models.CharField(max_length=4, blank=True)
    Test5_subject6 = models.CharField(max_length=4, blank=True)
    Test5_subject7 = models.CharField(max_length=4, blank=True)
    Test5_subject8 = models.CharField(max_length=4, blank=True)
    Test5_subject9 = models.CharField(max_length=4, blank=True)
    Test5_subject10 = models.CharField(max_length=4, blank=True)
    Test5_Rank = models.CharField(max_length=4, blank=True)

    Test6_subject1 = models.CharField(max_length=4, blank=True)
    Test6_subject2 = models.CharField(max_length=4, blank=True)
    Test6_subject3 = models.CharField(max_length=4, blank=True)
    Test6_subject4 = models.CharField(max_length=4, blank=True)
    Test6_subject5 = models.CharField(max_length=4, blank=True)
    Test6_subject6 = models.CharField(max_length=4, blank=True)
    Test6_subject7 = models.CharField(max_length=4, blank=True)
    Test6_subject8 = models.CharField(max_length=4, blank=True)
    Test6_subject9 = models.CharField(max_length=4, blank=True)
    Test6_subject10 = models.CharField(max_length=4, blank=True)
    Test6_Rank = models.CharField(max_length=4, blank=True)

    Test7_subject1 = models.CharField(max_length=4, blank=True)
    Test7_subject2 = models.CharField(max_length=4, blank=True)
    Test7_subject3 = models.CharField(max_length=4, blank=True)
    Test7_subject4 = models.CharField(max_length=4, blank=True)
    Test7_subject5 = models.CharField(max_length=4, blank=True)
    Test7_subject6 = models.CharField(max_length=4, blank=True)
    Test7_subject7 = models.CharField(max_length=4, blank=True)
    Test7_subject8 = models.CharField(max_length=4, blank=True)
    Test7_subject9 = models.CharField(max_length=4, blank=True)
    Test7_subject10 = models.CharField(max_length=4, blank=True)
    Test7_Rank = models.CharField(max_length=4, blank=True)


    Test8_subject1 = models.CharField(max_length=4, blank=True)
    Test8_subject2 = models.CharField(max_length=4, blank=True)
    Test8_subject3 = models.CharField(max_length=4, blank=True)
    Test8_subject4 = models.CharField(max_length=4, blank=True)
    Test8_subject5 = models.CharField(max_length=4, blank=True)
    Test8_subject6 = models.CharField(max_length=4, blank=True)
    Test8_subject7 = models.CharField(max_length=4, blank=True)
    Test8_subject8 = models.CharField(max_length=4, blank=True)
    Test8_subject9 = models.CharField(max_length=4, blank=True)
    Test8_subject10 = models.CharField(max_length=4, blank=True)
    Test8_Rank = models.CharField(max_length=4, blank=True)

    Test9_subject1 = models.CharField(max_length=4, blank=True)
    Test9_subject2 = models.CharField(max_length=4, blank=True)
    Test9_subject3 = models.CharField(max_length=4, blank=True)
    Test9_subject4 = models.CharField(max_length=4, blank=True)
    Test9_subject5 = models.CharField(max_length=4, blank=True)
    Test9_subject6 = models.CharField(max_length=4, blank=True)
    Test9_subject7 = models.CharField(max_length=4, blank=True)
    Test9_subject8 = models.CharField(max_length=4, blank=True)
    Test9_subject9 = models.CharField(max_length=4, blank=True)
    Test9_subject10 = models.CharField(max_length=4, blank=True)
    Test9_Rank = models.CharField(max_length=4, blank=True)

    Test10_subject1 = models.CharField(max_length=4, blank=True)
    Test10_subject2 = models.CharField(max_length=4, blank=True)
    Test10_subject3 = models.CharField(max_length=4, blank=True)
    Test10_subject4 = models.CharField(max_length=4, blank=True)
    Test10_subject5 = models.CharField(max_length=4, blank=True)
    Test10_subject6 = models.CharField(max_length=4, blank=True)
    Test10_subject7 = models.CharField(max_length=4, blank=True)
    Test10_subject8 = models.CharField(max_length=4, blank=True)
    Test10_subject9 = models.CharField(max_length=4, blank=True)
    Test10_subject10 = models.CharField(max_length=4, blank=True)
    Test10_Rank = models.CharField(max_length=4, blank=True)

    def __str__(self):
         return self.student_first_name
