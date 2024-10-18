from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import BookBorrowForm
from .models import Student,BookBorrow
from ModBookApp.models import Book

# Create your views here.
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

        