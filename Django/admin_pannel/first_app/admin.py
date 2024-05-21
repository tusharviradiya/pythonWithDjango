from django.contrib import admin
from first_app.models import Student
# Register your models here.

#when you want to one data to show put like this : 'id',
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuid', 'stuname', 'stuemail', 'stupass', 'comment')

# admin.site.register(Student, StudentAdmin)
