from .import views
from django.urls import path


urlpatterns = [
    path('', views.borrowBookList, name='borrow_list'),
    path('add_borrow_book/', views.addBorrowBook, name='add_borrow_book'),
    path('return_book/<int:id>/', views.returnBorrowBook, name='return_borrow_book'), 
    path('add_student/', views.addNewStudent, name='add_new_student'),
    path('student_list/', views.studentList, name='student_list'),
    path('student_card/<int:sid>', views.studentCard, name='student_card'),
]



