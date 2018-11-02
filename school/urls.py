"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from Admissions.views import admissionview
from Admissions.views import admission_new, admission_edit, admission_delete
from school.views import main_view
from parent.views import parentlogin,parentview,scorecardview
from staffs.views import staffview
from staffs.views import myclass, model_form_upload, studymaterial,document_updateview,libraryview,otherclassesview1,attendanceview,attendanceupdateview,absentonview,test1,test2,test3,test5,test6,test7,test8,test9,test10,test4
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admission/',admissionview.as_view(),name='admissionview'),
    path('admission/new',admission_new.as_view(), name='admission_new'),
    path('admission/<int:pk>/edit/', admission_edit.as_view(), name='admission_edit'),
    path('delete/', admission_delete.as_view(), name='admission_delete'),
    path(r'', main_view.as_view(), name='main_view'),
    path('parent/login',parentlogin,name='parentlogin'),
    path('parent/<int:pk>/home',parentview.as_view(),name='parentview'),
    path('parent/<int:pk>/scorecardview',scorecardview.as_view(),name='scorecardview'),
    path('staff/',staffview.as_view(),name='staffview'),
    path('staff/tests/1/<test>',test1.as_view(),name='test1view'),
    path('staff/tests/2/<test>',test2.as_view(),name='test2view'),
    path('staff/tests/3/<test>',test3.as_view(),name='test3view'),
    path('staff/tests/4/<test>',test4.as_view(),name='test4view'),
    path('staff/tests/5/<test>',test5.as_view(),name='test5view'),
    path('staff/tests/6/<test>',test6.as_view(),name='test6view'),
    path('staff/tests/7/<test>',test7.as_view(),name='test7view'),
    path('staff/tests/8/<test>',test8.as_view(),name='test8view'),
    path('staff/tests/9/<test>',test9.as_view(),name='test9view'),
    path('staff/tests/10/<test>',test10.as_view(),name='test10view'),
    path('staff/myclass',myclass.as_view(),name='myclass'),
    path('staff/studymaterial', studymaterial.as_view(),name = 'studymaterial'),
    path('staff/studymaterial/upload', model_form_upload.as_view(),name = 'document_upload'),
    path('staff/<int:pk>/edit/', document_updateview.as_view(), name='document_update'),
    path('digitallibrary', libraryview.as_view(), name='libraryview'),
    path('staff/otherclasses/<classes>', otherclassesview1.as_view(), name='otherclassesview'),
    path('staff/attendance', attendanceview.as_view(), name='attendanceview'),
    path('staff/<int:pk>/attendance/edit/', attendanceupdateview, name='attendanceupdateview'),
    path('staff/attendance/absent', absentonview.as_view(), name='absentonview'),
   
]


if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



