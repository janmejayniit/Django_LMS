from django.db import models
from datetime import date, timedelta
from ModStudentApp.models import Student

# Create your models here.

class BookBorrow(models.Model):
    from ModBookApp.models import Book
    class FineFeeReasons(models.TextChoices):
        DELAY = 'Delay In Return'
        LOSS = 'Book Loss'
        DAMAAGE = 'Damage Book'

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(default=date.today)
    return_day = models.IntegerField(default=7)
    return_date = models.DateField(blank=True, null=True)
    fine_fee = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    reason_for_fine=models.CharField(max_length=50, choices=FineFeeReasons.choices, blank=True, null=True)

    def booksubmitdate(self):
        return self.issue_date + timedelta(days=self.return_day) 

    returnning_book_day = property(booksubmitdate)

    def brrowReturnStatus(self):
        flag = None
        
        if self.return_date is None: 
            if date.today()>self.returnning_book_day:
                flag = 'Fine'
            else:
                flag = 'Pending'
        else: 
            if self.returnning_book_day==self.return_date:
                flag = 'On Time Submit'
            elif self.returnning_book_day>self.return_date:
                flag = 'Early Submit'
            else:
                flag = 'Late Submit'
        return flag
    
    return_book_flag = property(brrowReturnStatus)