
from django.contrib import admin
from staffs.models import staff
from staffs.models import subject
from staffs.models import Document,classdivision,Test_and_exam

# Register your models here.


admin.site.register(Document)
admin.site.register(subject)

class staffadmin(admin.ModelAdmin):
    filter_horizontal = ('Subject','classes')

class classdivisionadmin(admin.ModelAdmin):
    filter_horizontal = ('Subject','Tests')





admin.site.register(Test_and_exam)
admin.site.register(staff,staffadmin)

admin.site.register(classdivision,classdivisionadmin)
