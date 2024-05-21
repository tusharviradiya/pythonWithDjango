from django.shortcuts import render
from first_app.models import Student

# Create your views here.
def studentinfo(request):
    stud = Student.objects.all()
    print('myoutput', stud)
    return render(request, "enroll/studetails.html", {"stu": stud})