from django.db import models
from taggit.managers import TaggableManager

   
class Student(models.Model):
    username = models.CharField(max_length = 100, primary_key=True)
    password = models.CharField(max_length = 50)
    name = models.CharField(max_length = 100,default = 'null')
    emailAddress = models.EmailField(default = 'null@null.com')
    #avatar = models.ImageField()
    phoneNumber = models.CharField(max_length = 12)
    walletBalance = models.IntegerField()

class Tutor(models.Model):
    username = models.CharField(max_length = 100, primary_key=True)
    password = models.CharField(max_length = 50)
    name = models.CharField(max_length = 100,default = 'null')
    emailAddress = models.EmailField(default = 'null@null.com')
    #avatar = models.ImageField()
    phoneNumber = models.CharField(max_length = 12)
    walletBalance = models.IntegerField()
    subjectTag = TaggableManager()
    shortIntro = models.TextField()
    hourlyRate = models.IntegerField()
    blackedOutTime = models.DurationField()
    isContracted = models.BooleanField()
    

class BookingRecord(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    tutor = models.ForeignKey(Tutor,on_delete=models.CASCADE,null=True)
    sessionTime = models.DateTimeField()
    bookingTime = models.DateTimeField()
    status = models.CharField(max_length = 15)
    fee = models.IntegerField()
    subject = models.CharField(max_length = 8)
    venue = models.TextField()

        

    