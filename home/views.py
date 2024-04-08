from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import *
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    return render(request, 'home.html')

def adminpg(request):
    return render(request, 'adminpg.html')

# login page
def login_page(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(request, username = uname, password=pwd)


        if user is not None and user.is_staff == 1:
            login(request,user)
            return render(request, 'adminpg.html')
        
        elif user is not None and user.usertype == 'Student':
            student=Student.objects.get(sid=user)
            # request.session['sname']=user.id           

            if student.status == 'allow':
                login(request, user)  
                request.session['sname']=student.sname
                                           
                return render(request, 'stud_home.html', {'name':student.sname})
            else:
                return HttpResponse('sorry your account is blocked !!!')
            

            
        elif user is not None and user.usertype == 'Teacher':
            teacher = Teacher.objects.get(tid=user)
            
            if teacher.status == 'allow':
                login(request,user)
                request.session['name'] = teacher.tname
                return render(request, 'teacher_home.html', {'name': teacher.tname})
            else:
                return HttpResponse('sorry your account is blocked !!!')
                
        else: 
            return HttpResponse('Sorry, invalid details.')
    else:
        return render(request, 'login.html')

                        
# teacher registration
def teach_reg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('department')
        sts = request.POST.get('status')
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        n = User.objects.create_user(first_name=name, username=uname, password=pwd, usertype='Teacher')

        Teacher.objects.create(department=dept, status=sts, tid=n,tname=name)
        
        return render(request, 'adminpg.html')
    else:
        return render(request, 'teach_reg.html')
    

# admin show all teachers
def show_teach(request) :
    teachview = Teacher.objects.all()
    return render(request, 'show_teach.html', {'teachers' : teachview})


# admin delete teacher
def destroy_teach(request,id):
   teachdel = Teacher.objects.get(id=id)
   teachdel.delete()
   return redirect('/show_teach')



# admin update teacher
def teach_edit(request,id):
    if request.method=="POST":
        name=request.POST['name']
        department=request.POST['department']
        status=request.POST['status']
        
        edit = Teacher.objects.get(id=id)
        edit.tname = name
        edit.department = department
        edit.status = status
        edit.save()
        return redirect('/show_teach')
    
    d = Teacher.objects.get(id=id)
    return render(request, 'teach_edit.html', {"d":d})


# admin show all students
def show_stud(request) :
    studview = Student.objects.all()
    return render(request, 'show_stud.html', {'st' : studview})



# admin delete student
def admin_del_stud(request, i):
    stdel = Student.objects.get(id=i)
    stdel.delete()
    return redirect('/show_stud')


# admin edit student
def admin_edit_stud(request,i):
    if request.method=="POST":
        name=request.POST['name']
        department=request.POST['department']
        status=request.POST['status']
        
        edit = Student.objects.get(id=i)
        edit.sname = name
        edit.department = department
        edit.status = status
        edit.save()
        return redirect('/show_stud')
    
    d = Student.objects.get(id=i)
    return render(request, 'admin_edit_student.html', {"d":d})    



# admin approve student
def approve_stud(request):
    app = Student.objects.filter(status = 'block').values()
    return render(request, 'approve_stud.html', {'std' : app})
def approve(request, id):
    app = Student.objects.get(id=id)
    app.status = 'allow'
    app.save()
    return render(request, 'adminpg.html', {"approve": app})



# admin assign a teacher to student
def assignpg(request):
    studview = Student.objects.filter(tea = 'None').values()
    return render(request, 'assignpg.html', {'st' : studview})
def assign_teach(request,id):
    if request.method=="POST":
        teach=request.POST['tea']
        
        edit = Student.objects.get(id=id)
        edit.tea = teach
        edit.save()
        return redirect('/assignpg')
    
    d = Student.objects.get(id=id)
    return render(request, 'assign_teach.html', {"d":d})
# __________________________________________________________________________________________________________________________________________________


# ______________TEACHER Moule_____________

# teacher home 
def thome(request):
    return render(request, 'teacher_home.html')


# teacher show all students
def teach_show_stud(request) :
    studview = Student.objects.all()
    return render(request, 'teacher_show_stud.html', {'st' : studview})



# view teacher profile
def teacher_profile(request):
    x =  request.session['name'] 
    t = Teacher.objects.get(tname = x)
    return render(request, 'teacher_profile.html', {'tt':t})



# Edit teacher profile
def te_edit(request):
    nam = request.session['name']
    na = Teacher.objects.get(tname = nam )
    idd = na.tid_id
    us = User.objects.get(id = idd)
    return render(request, 'tedit.html', {'fo':na, 'f': us})

def tedit(request):
    if request.method=="POST":
        nam = request.session['name']

        name=request.POST['name']
        department=request.POST['department']        
        edit = Teacher.objects.get(tname = nam)
        ed = User.objects.get(first_name = nam)


        edit.tname= name
        edit.department = department

        ed.first_name = name
        ed.save()

        edit.save()
        
        return redirect('/thome')
    else:
        return render(request, 'tedit.html')


# ___________________________________________________________________________________________________________________________________________________


# _____________student module______________

# student home
def shome(request):
    return render(request, 'stud_home.html')


# student registration
def register(request):
    if request.method=='POST':
        name = request.POST.get('name')
        dept = request.POST.get('department')
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        n = User.objects.create_user(first_name = name, username = uname, password=pwd, usertype = 'Student')

        Student.objects.create(department=dept, sid=n, sname = name)

        return render(request, 'login.html')
    else:
        return render(request, 'register.html')
    

# student show teachers
def stud_show_teach(request) :
    teachview = Teacher.objects.all()
    return render(request, 'stud_show_teach.html', {'teachers' : teachview})



# edit student
def stud_edit(request):
    m= request.session['sname']
    st =  Student.objects.get(sname = m)
    n = st.sid_id
    us = User.objects.get(id = n)
    return render(request, 'stud_edit.html', {'form': st, 'nn': us})

def stud_update(request):
    if request.method=="POST":
        nam = request.session['sname']
        print(nam)

        name=request.POST['name']
        department=request.POST['department'] 
        user = request.POST['username']
        pwd = request.POST['password']    
        sid = request.POST['sid']    
        print(sid)

        edit = Student.objects.get(sname = nam)
        ed = User.objects.get(id = sid)

        edit.sname= name
        edit.department = department

        ed.first_name = name
        ed.username = user
        ed.set_password(pwd)
        ed.save()
        edit.save()
        
        return redirect('/shome')
    else:
        return redirect('/stud_edit')
    
# student leave application
def stud_leave(request):
    s = request.session['sname']
    if request.method == "POST":
        dt = request.POST['date']
        r = request.POST['reason']
        t = request.POST['teacher']
        Leave.objects.create(sfrom=s, totea=t, date=dt, msg=r)
        return redirect('/shome')
    else:
        return render(request,'stud_leave.html')



# teacher view leave applications
def teach_leave(request):
    t = request.session['name']
    d = Leave.objects.filter(totea=t, status='NotApproved')
    return render(request, 'teach_leave.html', {'st': d})


# teacher approve leave
def leaveapp(request,id):
    app = Leave.objects.get(id=id)
    app.status = 'Approved'
    app.save()
    return redirect('/teach_leave')



# student view leave application status
def stu_leave_sts(request):
    t = request.session['sname']
    d = Leave.objects.filter(sfrom=t)
    return render(request, 'stud_leave_sts.html', {'st': d })
