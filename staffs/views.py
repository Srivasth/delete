from django.shortcuts import render,render_to_response
from Admissions.models import Scholar,Absent_date
from school.mixins import GroupRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from staffs.models import staff,subject,Test_and_exam
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from staffs.forms import DocumentForm
from django.shortcuts import redirect
from staffs.models import Document, staff
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.conf import settings
from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import CheckboxSelectMultiple
import os
from django.shortcuts import get_object_or_404
from collections import OrderedDict
from school import fusioncharts


@method_decorator(login_required,name='dispatch')
class staffview(GroupRequiredMixin,ListView):
    group_required = [u'Staff']
    model = staff
    def get_queryset(self):
        s= User.objects.get(username = self.request.user)
        return staff.objects.filter(Name = s)
    #s = staff.objects.get(Name__username='raju')
    #ct = s.Class_teacher

    #classteacher = staff.Class_teacher
    #classsection = staff.Section

    context_object_name = 'classes_list'
    template_name = 'staffs/staffview.html'
    def get_context_data(self, **kwargs):
        context = super(staffview,self).get_context_data(**kwargs)
        context['data'] = [['100', 10], ['90', 9], ['80', 8]]
        return context

@method_decorator(login_required,name='dispatch')
class test1(GroupRequiredMixin,ListView):
    group_required = [u'Staff']
    model = Scholar

    def get_queryset(self):
        s = User.objects.get(username=self.request.user)
        return Scholar.objects.filter(Level='REGISTERED', Class_teacher=s)

    context_object_name = 'staff'
    template_name = 'staffs/test1.html'
    def get_context_data(self, **kwargs):
        context = super(test1,self).get_context_data(**kwargs)
        context['subject_list']=subject.objects.all()
        context['n'] = range(subject.objects.count())
        context['test']= self.kwargs['test']
        return context

@method_decorator(login_required,name='dispatch')
class test2(GroupRequiredMixin,ListView):
    group_required = [u'Staff']
    model = Scholar

    def get_queryset(self):
        s = User.objects.get(username=self.request.user)
        return Scholar.objects.filter(Level='REGISTERED', Class_teacher=s)

    context_object_name = 'staff'
    template_name = 'staffs/test2.html'
    def get_context_data(self, **kwargs):
        context = super(test2,self).get_context_data(**kwargs)
        context['subject_list']=subject.objects.all()
        context['n'] = range(subject.objects.count())
        context['test'] = self.kwargs['test']
        return context

@method_decorator(login_required,name='dispatch')
class test3(GroupRequiredMixin,ListView):
    group_required = [u'Staff']
    model = Scholar
    def get_queryset(self):
        s = User.objects.get(username=self.request.user)
        return Scholar.objects.filter(Level='REGISTERED', Class_teacher=s)
    context_object_name = 'staff'
    template_name = 'staffs/test3.html'
    def get_context_data(self, **kwargs):
        context = super(test3,self).get_context_data(**kwargs)
        context['subject_list']=subject.objects.all()
        context['n'] = range(subject.objects.count())
        context['test'] = self.kwargs['test']
        return context

@method_decorator(login_required, name='dispatch')
class test4(GroupRequiredMixin, ListView):
    group_required = [u'Staff']
    model = Scholar

    def get_queryset(self):
        s = User.objects.get(username=self.request.user)
        return Scholar.objects.filter(Level='REGISTERED', Class_teacher=s)

    context_object_name = 'staff'
    template_name = 'staffs/test4.html'

    def get_context_data(self, **kwargs):
        context = super(test4, self).get_context_data(**kwargs)
        context['subject_list'] = subject.objects.all()
        context['n'] = range(subject.objects.count())
        context['test'] = self.kwargs['test']
        return context

@method_decorator(login_required,name='dispatch')
class test5(GroupRequiredMixin,ListView):
    group_required = [u'Staff']
    model = Scholar

    def get_queryset(self):
        s = User.objects.get(username=self.request.user)
        return Scholar.objects.filter(Level='REGISTERED', Class_teacher=s)

    context_object_name = 'staff'
    template_name = 'staffs/test5.html'
    def get_context_data(self, **kwargs):
        context = super(test5,self).get_context_data(**kwargs)
        context['subject_list']=subject.objects.all()
        context['n'] = range(subject.objects.count())
        context['test'] = self.kwargs['test']
        return context

@method_decorator(login_required,name='dispatch')
class test6(GroupRequiredMixin,ListView):
    group_required = [u'Staff']
    model = Scholar

    def get_queryset(self):
        s = User.objects.get(username=self.request.user)
        return Scholar.objects.filter(Level='REGISTERED', Class_teacher=s)

    context_object_name = 'staff'
    template_name = 'staffs/test6.html'
    def get_context_data(self, **kwargs):
        context = super(test6,self).get_context_data(**kwargs)
        context['subject_list']=subject.objects.all()
        context['n'] = range(subject.objects.count())
        context['test'] = self.kwargs['test']
        return context

@method_decorator(login_required,name='dispatch')
class test7(GroupRequiredMixin,ListView):
    group_required = [u'Staff']
    model = Scholar

    def get_queryset(self):
        s = User.objects.get(username=self.request.user)
        return Scholar.objects.filter(Level='REGISTERED', Class_teacher=s)

    context_object_name = 'staff'
    template_name = 'staffs/test7.html'
    def get_context_data(self, **kwargs):
        context = super(test7,self).get_context_data(**kwargs)
        context['subject_list']=subject.objects.all()
        context['n'] = range(subject.objects.count())
        context['test'] = self.kwargs['test']
        return context


@method_decorator(login_required,name='dispatch')
class test8(GroupRequiredMixin,ListView):
    group_required = [u'Staff']
    model = Scholar

    def get_queryset(self):
        s = User.objects.get(username=self.request.user)
        return Scholar.objects.filter(Level='REGISTERED', Class_teacher=s)

    context_object_name = 'staff'
    template_name = 'staffs/test8.html'
    def get_context_data(self, **kwargs):
        context = super(test8,self).get_context_data(**kwargs)
        context['subject_list']=subject.objects.all()
        context['n'] = range(subject.objects.count())
        context['test'] = self.kwargs['test']
        return context


@method_decorator(login_required,name='dispatch')
class test9(GroupRequiredMixin,ListView):
    group_required = [u'Staff']
    model = Scholar

    def get_queryset(self):
        s = User.objects.get(username=self.request.user)
        return Scholar.objects.filter(Level='REGISTERED', Class_teacher=s)

    context_object_name = 'staff'
    template_name = 'staffs/test9.html'
    def get_context_data(self, **kwargs):
        context = super(test9,self).get_context_data(**kwargs)
        context['subject_list']=subject.objects.all()
        context['n'] = range(subject.objects.count())
        context['test'] = self.kwargs['test']
        return context



@method_decorator(login_required,name='dispatch')
class test10(GroupRequiredMixin,ListView):
    group_required = [u'Staff']
    model = Scholar

    def get_queryset(self):
        s = User.objects.get(username=self.request.user)
        return Scholar.objects.filter(Level='REGISTERED', Class_teacher=s)

    context_object_name = 'staff'
    template_name = 'staffs/test10.html'
    def get_context_data(self, **kwargs):
        context = super(test10,self).get_context_data(**kwargs)
        context['subject_list']=subject.objects.all()
        context['n'] = range(subject.objects.count())
        context['test'] = self.kwargs['test']
        return context

@method_decorator(login_required,name='dispatch')
class myclass(GroupRequiredMixin,ListView):
    group_required = [u'Staff']
    model = Scholar
    def get_queryset(self):
        s = User.objects.get(username=self.request.user)
        return Scholar.objects.filter(Level='REGISTERED', Class_teacher=s)
    context_object_name = 'staff'

    template_name = 'staffs/html_snippets/my_class.html'


    #def get(self,request,*args,**kwargs):
     #

      #  self.object= self.get_object(queryset = Scholar.objects.filter(Level='REGISTERED', Class_teacher=s))
       # return super().get(request,*args,**kwargs)
    #def get_context_data(self,**kwargs):
        #s = User.objects.get(username=self.request.user)
        #queryset = Scholar.objects.filter(Level='REGISTERED', Class_teacher=s)
        #context = super(myclass,self).get_context_data(**kwargs)
        #context['staff']=queryset
        #context['subject'] = subject.objects.all()
       # return context

   # template_name = 'staffs/html_snippets/my_class.html'


@method_decorator(login_required,name='dispatch')
class attendanceview(GroupRequiredMixin,ListView):
    group_required = [u'Staff']
    model = Scholar
    def get_queryset(self):
        s = User.objects.get(username=self.request.user)
        return Scholar.objects.filter(Level='REGISTERED', Class_teacher=s)

    context_object_name = 'attendance_list'
    template_name = 'staffs/attendanceview.html'

@method_decorator(login_required,name='dispatch')
class absentonview(GroupRequiredMixin,CreateView):
    group_required = [u'Staff']
    model= Absent_date
    fields = '__all__'
    template_name = 'staffs/absentonview.html'
    success_url = reverse_lazy('attendanceview')

class attendanceupdateform(forms.ModelForm):
    Absent_on = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Absent_date.objects.all())

    class Meta:
        model = Scholar
        fields = ("student_first_name", "Absent_on")



def attendanceupdateview(request,pk):
    absent = get_object_or_404(Scholar,pk = pk)
    if request.method=="POST":
        form =  attendanceupdateform(request.POST,instance=absent)
        if form.is_valid():
            absent = form.save()
            return redirect('attendanceview')
    else:
        form = attendanceupdateform(instance=absent)
    return render(request,'staffs/attendanceupdate.html',{'form':form})




#class attendanceform(forms.ModelForm):
 #   student_first_name = forms.CharField(max_length=50)
  #  Absent_on = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Absent_date.objects.all(),
   #                                            required=True)
    #class Meta:
     #   model = Scholar
      #  fields = ('student_first_name', 'Absent_on',)
       # template_name = 'staffs/attendanceupdate.html'
        #success_url = reverse_lazy('attendanceview')

#class attendanceupdateview(GroupRequiredMixin,UpdateView):
 #   group_required = [u'Staff']
  #  model = Scholar
   # fields = ("student_first_name", "Absent_on")
    #template_name = 'staffs/attendanceupdate.html'
    #def get_queryset(self):
     #   scholar = Scholar.objects.get(pk=self.kwargs['pk'])
      #  return scholar




    #absent_date = forms.ModelMultipleChoiceField(Absent_date.objects.all(),widget=FilteredSelectMultiple("Absent_date",False,attrs={'rows':'10'}))

    #

    #fields = ("student_first_name", "Absent_on")

#def Form(request):
 #   attendance_update = attendanceupdateview()
  #  if request.POST:
   #     attendance_update = attendanceupdateview(request.POST)
    #    attendance_update.save()
     #   return render_to_response("staffs/attendanceview.html")
   # else:
    #    return render_to_response("staffs/attendanceupdate.html")





    #something = forms.ModelMultipleChoiceField()


@method_decorator(login_required, name='dispatch')
class studymaterial(GroupRequiredMixin,ListView):
    group_required = [u'Staff']
    model = Document

    def get_queryset(self):

        s = User.objects.get(username=self.request.user)
        return Document.objects.filter(upload_by = s)


    context_object_name = 'Document_list'
    template_name = 'staffs/studymaterial.html'

@method_decorator(login_required, name='dispatch')
class model_form_upload(GroupRequiredMixin,CreateView):
    group_required = [u'Staff']
    model = Document
    fields = '__all__'

    template_name = 'staffs/model_form_upload.html'
    success_url = reverse_lazy('studymaterial')

@method_decorator(login_required, name='dispatch')
class document_updateview(GroupRequiredMixin,UpdateView):
    group_required = [u'Staff']
    model = Document
    fields = '__all__'

    success_url = reverse_lazy('studymaterial')

@method_decorator(login_required, name='dispatch')
class libraryview(ListView):

    model = Document
    fields = '__all__'
    context_object_name = 'Document_list'
    template_name = 'staffs/digitallibrary.html'

@method_decorator(login_required, name='dispatch')
class otherclassesview1(GroupRequiredMixin,ListView):
    group_required = [u'Staff']
    model = Scholar

    def get_queryset(self):
        return Scholar.objects.filter(Class__Class = self.kwargs['classes'],Level = 'REGISTERED')

    context_object_name = 'Student_list'
    template_name = 'staffs/otherclassesview1.html'




#def model_form_upload(request):
 #   if request.method == 'POST':
 #       form = DocumentForm(request.POST, request.FILES)
  #      if form.is_valid():
   #         form.save()
    #        return redirect('/staff')
    #else:
     #   form = DocumentForm()

   # return render(request, 'staffs/model_form_upload.html', {
   #     'form': form
    #})

