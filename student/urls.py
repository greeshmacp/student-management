"""
URL configuration for student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('adminpg/', views.adminpg),
    path('login/',views.login_page),
    path('register/',views.register),
    path('teach_reg/',views.teach_reg),
    path('show_teach/', views.show_teach),
    path('show_stud/', views.show_stud),
    path('del/<int:id>', views.destroy_teach),
    path('edit/<int:id>', views.teach_edit),
    path('del_stud/<int:i>', views.admin_del_stud),
    path('edit_stud/<int:i>', views.admin_edit_stud),
    path('shome/', views.shome),
    path('stud_edit/', views.stud_edit),
    path('stud_update/', views.stud_update),
    path('stud_show_teach/', views.stud_show_teach),
    path('approve_stud/', views.approve_stud), 
    path('approve/<int:id>', views.approve),
    path('assignpg/', views.assignpg),
    path('assign/<int:id>', views.assign_teach),
    path('teach/', views.teach_show_stud),
    path('thome/', views.thome),
    path('teacher_profile/', views.teacher_profile),
    path('tedit/', views.te_edit),
    path('te/',views.tedit),
    path('leave/', views.stud_leave),
    path('leaveapp/<int:id>', views.leaveapp),
    # path('reject_leave/<int:i>', views.reject_leave),
    path('teach_leave/', views.teach_leave),
    path('stu_leave_sts/', views.stu_leave_sts),
]

urlpatterns += staticfiles_urlpatterns()