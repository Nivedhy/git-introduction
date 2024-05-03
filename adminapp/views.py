from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
# Create your views here.
def home(request):
    return render(request,'home.html')


def admin(request):
    return render(request,'admin.html')


def login(request):
    return render(request,'login.html')





def register(request):
    course_data = course.objects.all()
    return render(request,'register.html',{'c_data':course_data})


def teacherpage(request):
    current_user = request.user
    u_id = current_user.id
    print(u_id)
    teacher_data = teacher.objects.get(user = u_id)
    return render(request,'teacher.html',{'teacher_da': teacher_data}) 

def editteacher(request,tid):
    teacher_values = teacher.objects.get(id = tid)
    return render(request,'editteacher.html',{'t_data':teacher_values})



def loginfunction(request):
    if request.method == 'POST':
        username = request.POST['uname']
        passw = request.POST['pass']
        user = auth.authenticate(username = username, password = passw)
    
        if user is not None:
            auth.login(request,user)
    
        if request.user.is_staff == 1:
            return redirect('admin')
        else:
            return redirect('teacherhome')
    else:
        return redirect('login')
    

def addcourse(request):
    if request.method == 'POST': 
        course_name = request.POST.get('course')
        course.objects.create(course_name = course_name)
        return redirect('admin') 
        
    return render(request,'admin.html')   
    
def teacherregister(request):
       if request.method == 'POST':
           fn = request.POST.get('f_name') 
           ln = request.POST.get('l_name') 
           num = request.POST.get('num') 
           email = request.POST.get('email') 
           usern = request.POST.get('usr') 
           pw = request.POST.get('psw') 
           cpw = request.POST.get('cpsw') 
           img = request.POST.get('img')
           select = request.POST.get('select') 
           cour_name = course.objects.get(id = select)


           if pw == cpw:
               if User.objects.filter(username = usern).exists():
                   return redirect('register')
               else:
                   user = User.objects.create_user(first_name = fn , last_name = ln , email = email, password = pw, username =usern)
                   user.save()
                   data = User.objects.get(id = user.id)
                   teacherdata = teacher(number = num, user = data , course_fk = cour_name )
                   teacherdata.save()
                   print('success')
                   return redirect('login')
           else:
               print('psw is not same')
               return redirect('register')
           
       else:
           print('error')
           return redirect('register')
       

def editteacher_fn(request,tid):
    if request.method == 'POST':
        data = teacher.objects.get(id = tid)
        data.user.first_name = request.POST.get('f_name')
        data.user.last_name = request.POST.get('l_name')
        data.user.email = request.POST.get('email')
        data.number = request.POST.get('numb')

        select = request.POST.get('select')
        crs = course.objects.get(id = select)
        data.course_fk = crs
        data.save()
        data.user.save()
        if request.user.is_staff == 1:
            return redirect('admin')
        else:
            return redirect('home')
        
    
    return render(request,'editteacher.html')




def dltpg(request,tid):
    teacher_values = teacher.objects.get(id = tid)
    return render(request,'delete.html',{'t_data':teacher_values})



def dltfn(request,tid):
    if request.method == 'POST':
        teacher_value = teacher.objects.get(id=tid)
        teacher_value.delete()
        if request.user.is_staff == True:
            return redirect('teacher')
        else:
            return redirect('home')

    return redirect('delete')
