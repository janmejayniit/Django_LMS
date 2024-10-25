from .import views
from django.urls import path


urlpatterns = [
    path('add_student/', views.addNewStudent, name='add_new_student'),
    path('student_list/', views.studentList, name='student_list'),
    path('student_card/<int:sid>', views.studentCard, name='student_card'),
]



