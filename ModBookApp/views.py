from django.shortcuts import redirect, render
from .models import Book
from .forms import BookForm
from django.core.paginator import Paginator

# Create your views here.
def addNew(request):

    if request.method=='POST':
        form=BookForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save(commit=False)
            book.user =  request.user
            book.save()
            return redirect('add_new')
    else:
        form = BookForm()
        return render(request,'ModBookApp/add_new.html', {'form':form})

def listBook(request):
    book_lists = Book.objects.order_by('-pk').all()
    paginator = Paginator(book_lists, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'ModBookApp/index.html',{'book_lists':page_obj})