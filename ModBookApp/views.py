from turtle import title
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Book, BookStocks
from .forms import BookForm, BookStockForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import csv

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
    paginator = Paginator(book_lists, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'ModBookApp/index.html',{'book_lists':page_obj})


@login_required
def printBookBarcode(request):
    books_list = Book.objects.order_by('-pk').all()
    return render(request, 'ModBookApp/print_book_barcode.html',{'books_list':books_list})

def generateBarcode(request):
    book_isbn = request.POST.get('book_isbn','')
    total_number = request.POST.get('total_number','')

    from io import BytesIO
    import barcode

    rv = BytesIO()
    # code = barcode.get('code128', book_isbn, writer=barcode.writer.SVGWriter())
    code = barcode.get('code39', book_isbn, writer=barcode.writer.SVGWriter())
    code.write(rv)

    rv.seek(0)
    svg = rv.read()

    return JsonResponse({'svg':svg.decode('utf-8'),'total_number':total_number})

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Price','Pages','Authors','Publication','ISBN','Edition','Edition Year','Tags','Total Books'])

    for obj in Book.objects.all():
        writer.writerow([obj.title, obj.price, obj.pages, obj.authors, obj.publication, obj.isbn, obj.edition, obj.edition_year,obj.tags, obj.total_books ])

    return response


# def export_excel(request):
#     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = 'attachment; filename="mydata.xlsx"'

#     workbook = openpyxl.Workbook()
#     worksheet = workbook.active
#     worksheet.title = 'My Data'

#     # Write header row
#     header = ['ID', 'Name', 'Email']
#     for col_num, column_title in enumerate(header, 1):
#         cell = worksheet.cell(row=1, column=col_num)
#         cell.value = column_title

#     # Write data rows
#     queryset = MyModel.objects.all().values_list('id', 'name', 'email')
#     for row_num, row in enumerate(queryset, 1):
#         for col_num, cell_value in enumerate(row, 1):
#             cell = worksheet.cell(row=row_num+1, column=col_num)
#             cell.value = cell_value

#     workbook.save(response)

#     return response

@login_required
def bookUpdate(request, bid):
    book_instance = get_object_or_404(Book, id=bid)
    stock_instance = get_object_or_404(BookStocks, book=bid)
    book_form = BookForm(instance=book_instance)
    stock_form = BookStockForm(instance=stock_instance)
    if request.method =='POST':
        
        book_form_submit = BookForm(request.POST or None, request.FILES, instance=book_instance)
        stock_form_submit = BookStockForm(request.POST or None, stock_instance)
        if book_form_submit.is_valid() and stock_form_submit.is_valid():
            book_form_submit.save()
            # stock_form_submit.save()
            return redirect('list_boook')
        else:
            pass
    return render(request, 'ModBookApp/update_book.html', {'form':book_form, 'book_stock_form':stock_form})


def searchBookTitle(request):
    query=request.GET.get('query')
    
    book_list = Book.objects.filter(title__icontains=query).all()
    # print(book_list.query)
    arr_list = []
    for item in book_list:
        arr_list.append({'title':item.title})

    return JsonResponse({'arr_list':arr_list})