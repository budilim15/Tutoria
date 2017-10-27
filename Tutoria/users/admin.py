from django.contrib import admin
from users.models import UserProfile,Student, Tutor, BookingRecord, BlackOut, Timeslot

admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(BookingRecord)
admin.site.register(BlackOut)
admin.site.register(Timeslot)
