from django.shortcuts import render,redirect,get_object_or_404

from .models import Student
from .forms import studentform, RegisterForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'index.html')

def Home(request):
    return render(request,'home.html')

def reshome(request):
    return render(request,'reshome.html')

def about(request):
    return render(request,'about.html')


def resabout(request):
    return render(request,'resabout.html')


def contact(request):
    return render(request,'contact.html')

# read
def student_list(request):
    stud = Student.objects.all()    #it's just a variable to hold the data of all students. it's may have any name
    return render(request,'studentlist.html',{'students':stud})  # the 'students' is from html page and 'stude' is from this page


# create
def add_student(request):
    form = studentform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'add_student.html',{'form':form})

# update
def edit_student(request,pk):
    student = get_object_or_404(Student,pk=pk)
    form = studentform(request.POST or None , instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'edit_student.html',{'form':form})


# delete
def delete_student(request,pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method =='POST':
        student.delete()
        return redirect('student_list')
    return render(request,'delete_student.html',{'student':student}) #first 'student' is taken from delete_student.html
    
    
#register
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered successfully!")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()  # for GET request

    return render(request, 'register.html', {'form': form})