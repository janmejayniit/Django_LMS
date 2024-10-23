from django.shortcuts import redirect, render, HttpResponse
from .models import Book, BookStocks
from .forms import BookForm, BookStockForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def addNew(request):

    if request.method=='POST':
        form=BookForm(request.POST, request.FILES)
        book_stock_form=BookStockForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user =  request.user
            book.save()
            return redirect('add_new')
        else:
            return render(request, {'form':form,'book_stock_form':book_stock_form})
    else:
        form = BookForm()
        book_stock_form=BookStockForm()
        return render(request,'ModBookApp/add_new.html', {'form':form,'book_stock_form':book_stock_form})

@login_required
def listBook(request):
    book_lists = Book.objects.order_by('-pk').all()
    paginator = Paginator(book_lists, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'ModBookApp/index.html',{'book_lists':page_obj})


@login_required
def printBookBarcode(request):
    from .mybarcode import MyBarcodeDrawing
    d = MyBarcodeDrawing("HELLO WORLD")
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')

    # books_list = Book.objects.order_by('-pk').all()
    # return render(request, 'ModBookApp/print_book_barcode.html',{'books_list':books_list})

# def generateBarcode(request):
#     book_isbn = request.form.data('book_isbn')
#     total_number = request.form.data('total_number')
