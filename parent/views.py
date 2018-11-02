from django.shortcuts import render,render_to_response , redirect
from school.mixins import GroupRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from staffs.models import staff
from staffs.models import Document, staff
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import forms
from Admissions.models import Scholar
from django.http import HttpResponse
from django.forms import ModelForm



#class loginform(ModelForm):
    #class Meta:
        #model = Scholar
        #fields =('Contact_number','Password',)

class scorecardview(ListView):
    model = Scholar
    def get_queryset(self):
        return Scholar.objects.get(pk = self.kwargs['pk'])

    context_object_name = 'Student'
    template_name = 'parent/scorecardview.html'


def parentlogin(request):
    if request.method == "POST":
        data=request.POST
        contact = data['username']
        pwd = data['Password']
        x = Scholar.objects.filter(Contact_number = contact,Password = pwd).count()

        if x:
            return redirect('parentview',pk = contact)
        else:
                return HttpResponse("<h3>Sorry You are not authenticated</h3>")
    else:
        return render(request, 'parent/parent_login.html')
    #def post(self,request):
     #   form = loginform()
      #  if form.is_valid():
       #     contact = form.cleaned_data['Contact_number']
        #    pwd = form.cleaned_data['Password']
         #   filteredscholar = Scholar.objects.filter(Contact_number = contact, Password =pwd)
          #  if filteredscholar.objects.count>0:
           #     return HttpResponse("<h2>Hey</h2>")



class parentview(ListView):
    model = Scholar
    def get_queryset(self):
        return Scholar.objects.get(pk = self.kwargs['pk'])
    context_object_name = 'Student'
    template_name = 'parent/parentview.html'







