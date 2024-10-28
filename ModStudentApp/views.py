from django.shortcuts import get_object_or_404, redirect, render
from .forms import StudentForm
from .models import Student
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

@login_required
def addNewStudent(request):
    if request.method=='POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('borrow_list')
        else:
            return render(request, 'ModStudentApp/add_student.html', {'form':form})
    else:
        form = StudentForm()
        return render(request, 'ModStudentApp/add_student.html', {'form':form})

@login_required
def studentList(request):
    student_lists = Student.objects.order_by('-pk').all()
    paginator = Paginator(student_lists, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'ModStudentApp/student_list.html',{'students_list':page_obj})

@login_required
def studentCard(request, sid):
    student = Student.objects.get(id=sid)
    qr_code_url='http://127.0.0.1:8000/student/'+str(sid)
    return render(request, 'ModStudentApp/student_card.html', {'student':student,'qr_code_url':qr_code_url})

@login_required
def studentDelete(request, sid):
    student = Student.objects.filter(id=sid).first()
    message = f'{student.first_name} {student.last_name} has deleted succesfully.'
    student.delete()

    messages.success(request,message)
    return redirect('student_list')

@login_required
def studentUpdate(request, sid):

    instance = get_object_or_404(Student, id=sid)
    form = StudentForm(instance=instance)
    if request.method=='POST':
        form = StudentForm(request.POST or None, request.FILES or None,  instance=instance)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            return render(request, 'ModStudentApp/update_student.html', {"form":form}) 
    return render(request, 'ModStudentApp/update_student.html', {"form":form})