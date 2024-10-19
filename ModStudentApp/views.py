from datetime import date
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import JsonResponse

from .forms import BookBorrowForm, StudentForm
from .models import BookBorrow, Student
from django.core.paginator import Paginator

# Create your views here.
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

def studentList(request):
    student_lists = Student.objects.order_by('-pk').all()
    paginator = Paginator(student_lists, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'ModStudentApp/student_list.html',{'students_list':page_obj})

def studentCard(request, sid):
    student = Student.objects.get(id=sid)
    qr_code_url='http://127.0.0.1:8000/student/'+str(sid)
    return render(request, 'ModStudentApp/student_card.html', {'student':student,'qr_code_url':qr_code_url})

def borrowBookList(request):
    borrow_lists = BookBorrow.objects.order_by('-issue_date').all()
    return render(request,'ModStudentApp/index.html',{'borrow_lists':borrow_lists})

def addBorrowBook(request):
    if request.method=='POST':
        form = BookBorrowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrow_list')
        else:
            messages.add_message(request, messages.ERROR, str(form))
            return redirect('add_borrow_book')
    else:
        form = BookBorrowForm()
        return render(request,'ModStudentApp/add_borrow.html', {'form':form})

def returnBorrowBook(request, id):
    borrow_book = BookBorrow.objects.filter(id=id).first()
    if borrow_book:
        borrow_book.return_date=date.today()
        borrow_book.save()
    return JsonResponse({'status':'success'})

        