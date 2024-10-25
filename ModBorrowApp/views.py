from datetime import date
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import JsonResponse

from .forms import BookBorrowForm
from .models import BookBorrow
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage

# Create your views here.
@login_required
def borrowBookList(request):
    borrow_lists = BookBorrow.objects.order_by('-issue_date').all()
    return render(request,'ModBorrowApp/index.html',{'borrow_lists':borrow_lists})

@login_required
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
        return render(request,'ModBorrowApp/add_borrow.html', {'form':form})

@login_required
def returnBorrowBook(request, id):
    borrow_book = BookBorrow.objects.filter(id=id).first()
    if borrow_book:
        borrow_book.return_date=date.today()
        borrow_book.save()
        # student = Student.objects.filter(id=borrow_book.student.id).first()
        
        # mail_body='I hope you have enjoy the book , If you want to give any suggestion, You are most welcome.'
        # email = EmailMessage('Return book to Library', mail_body, to=[student.email])
        # email.send()
    return JsonResponse({'status':'success'})

        