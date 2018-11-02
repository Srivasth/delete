from django.shortcuts import render
from Admissions.models import info
from django.views.generic import ListView

class main_view(ListView):
    model = info
    context_object_name = 'info_list'
    template_name = 'school/school.html'
