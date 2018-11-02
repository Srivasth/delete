from django.contrib import admin
from Admissions.models import Scholar,info,Absent_date

from school.mixins import Exportcsvmixin
from django.urls import path
import csv
from django.shortcuts import redirect
from django import forms
from django.shortcuts import render
from io import TextIOWrapper
# Register your models here.
class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

class scholaradmin(admin.ModelAdmin,Exportcsvmixin):
    list_display = ("student_first_name", "student_last_name", "Fathers_name", "Contact_number","Date_of_Birth", "email_id", "Address","Previous_school","Class","Level","Class_teacher","Password")
    list_filter = ("Previous_school","Level","Class")
    search_fields = ("student_first_name","Contact_number","email_id")
    change_list_template = "entities/student_change_list.html"
    actions = ["export_as_csv"]
    fields = ("student_first_name", "student_last_name", "Fathers_name", "Contact_number","Date_of_Birth", "email_id", "Address","Previous_school","Class","Level","Class_teacher","Absent_on","Test1_subject1","Test1_subject3","Test1_Rank")
    filter_horizontal = ('Absent_on',)
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/',self.import_csv),

        ]
        return my_urls + urls
    def import_csv(self,request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            reader = csv.DictReader(csv_file)


            for row in reader:

                    created = Scholar.objects.get_or_create(
                        student_first_name = row['student_first_name'],
                        student_last_name = row['student_last_name'],
                        Fathers_name=row['Fathers_name'],
                        Contact_number=row['Contact_number'],
                        Date_of_Birth=row['Date_of_Birth'],
                        Gender = row['Gender'],
                        email_id = row['email_id'],
                        Address = row['Address'],
                        Level=row['Level'],
                        Previous_school=row['Previous_school'],
                        Class=row['Class'],
                        Password = row['Password'],
                        Class_teacher = row['Class_teacher'],

                     )
                    created.save()


            self.message_user(request,"Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        student = {"form":form}
        return render(
            request, "admin/csv_form.html",student
        )

admin.site.register(Absent_date)
admin.site.register(info)
admin.site.register(Scholar,scholaradmin)







