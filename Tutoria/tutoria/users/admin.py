from django.contrib import admin
from users.models import Student
from users.models import Tutor
from users.models import BookingRecord


admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(BookingRecord)
