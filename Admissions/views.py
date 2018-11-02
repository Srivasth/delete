from django.shortcuts import render
from Admissions.models import Scholar,info
from django.views.generic import ListView
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from school.mixins import Exportcsvmixin
from school.mixins import GroupRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from sortable_listview import SortableListView


@method_decorator(login_required,name='dispatch')
class admissionview(GroupRequiredMixin,SortableListView):
        group_required = [u'Office']


        allowed_sort_fields = {'student_first_name':{'default_direction':'', 'verbose_name':'Student name'},
                               'Contact_number': {'default_direction': '', 'verbose_name': 'Contact number'},
                               'Date_of_Birth': {'default_direction': '', 'verbose_name': 'Date of birth'},
                               'email_id': {'default_direction': '', 'verbose_name': 'email id'},
                               'Level_Choices': {'default_direction': '', 'verbose_name': 'email id'},}

        default_sort_field = 'student_first_name'
        model = Scholar

        paginate_by = 25
        context_object_name = 'Scholar_list'


@method_decorator(login_required,name='dispatch')
class admission_new(GroupRequiredMixin,CreateView):
    group_required = [u'Office']
    model = Scholar
    fields = ("student_first_name", "student_last_name", "Fathers_name", "Contact_number","Date_of_Birth", "email_id", "Address","Previous_school","Level","Class","Class_teacher")

    success_url = reverse_lazy('admissionview')



@method_decorator(login_required,name='dispatch')
class admission_edit(GroupRequiredMixin,UpdateView):
    group_required = [u'Office']
    model = Scholar
    fields = ("student_first_name", "student_last_name", "Fathers_name", "Contact_number","Date_of_Birth", "email_id", "Address","Previous_school","Level","Class","Class_teacher")
    success_url = reverse_lazy('admissionview')

@method_decorator(login_required,name='dispatch')
class admission_delete(GroupRequiredMixin,DeleteView):
    group_required = [u'Office']
    model = Scholar
    success_url = reverse_lazy('admissionview')




#@group_required('Office')
#@login_required()
#def admission_new(request):
#    if request.method == "POST":
 #       form = admissionform(request.POST)
  #      if form.is_valid():
   #         Scholar = form.save(commit=False)
    #        Scholar.save()
     #       return redirect('/admission')
    #else:
     #       form = admissionform()
    #return render(request, 'Admissions/Scholar_form.html', {'form':form})


#def admission_edit(self,request, pk):
 #   scholars = get_object_or_404(Scholar, pk=pk)
  #  if request.method == "POST":
   #     form = admissionform(request.POST, instance=scholars)
    #    if form.is_valid():
     #       Scholar = form.save(commit=False)
      #      Scholar.save()
       #     return redirect('/admission', pk=Scholar.pk)
    #else:
     #   form = admissionform(instance=scholars)
    #return render(request, 'Admissions/Scholar_form.html', {'form': form})
