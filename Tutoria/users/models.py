from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save



"""class Post(models.Model):
	title = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()
	
#	def __str__(self):
#		return self.title
"""



"""class Student(models.Model):
	username = models.CharField(max_length = 16)
	password = models.CharField(max_length = 50)
	name = models.CharField(max_length = 100, default='')
	emailAddress = models.EmailField(default = 'example@example.com')
	#avatar = models.ImageField()
	phoneNumber = models.CharField(max_length = 12,default='')
	walletBalance = models.IntegerField(default=0)
	def __str__(self):
		return self.username

"""
class UserProfile(models.Model):
	username = models.OneToOneField(User, primary_key=True)
	name = models.CharField(max_length = 100, default='')
	emailAddress = models.EmailField(default = 'example@example.com')
	#avatar = models.ImageField()
	phoneNumber = models.CharField(max_length = 12,default='')
	walletBalance = models.IntegerField(default=0)
	isStudent = models.BooleanField(default=False)
	isTutor = models.BooleanField(default=False)
	
	def __str__(self):
		return str(self.username)


class Student(models.Model):
	username = models.OneToOneField(UserProfile, primary_key=True)
	def __str__(self):
		return str(self.username)
	
class Tutor(models.Model):
	username = models.OneToOneField(UserProfile, primary_key=True)
	subjectTag = TaggableManager()
	shortIntro = models.TextField()
	hourlyRate = models.IntegerField()
	blackedOutTime = models.DurationField()
	isContracted = models.BooleanField()
	def __str__(self):
		return str(self.username)
 

class BookingRecord(models.Model):
	student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
	tutor = models.ForeignKey(Tutor,on_delete=models.CASCADE,null=True)
	sessionTime = models.DateTimeField()
	bookingTime = models.DateTimeField()
	status =(
        ('CANCELLED', 'CANCELLED'),
        ('ENDED', 'ENDED'),
        ('SCHEDULED', 'SCHEDULED'),
        ('RUNNING', 'RUNNING'),
    )
	fee = models.IntegerField()
	subject = models.CharField(max_length = 8)
	venue = models.TextField()
	def __str__(self):
		return str(self.sessionTime + " " + self.student + " " + self.tutor)

class BlackOut(models.Model):
	tutor=models.ForeignKey(Tutor,on_delete=models.CASCADE,null=True)
	date=models.DateTimeField()
	class Meta:
		unique_together = ('tutor' , 'date')
	#def __str__(self):
	#	return str(Meta)
	
class Timeslot(models.Model):
	tutor=models.ForeignKey(Tutor,on_delete=models.CASCADE,null=True)
	date=models.DateTimeField()
	class Meta:
		unique_together = ('tutor' , 'date')
	#def __str__(self):
	#	return str(Meta.unique_together)
		
def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile=UserProfile.objects.create(username=kwargs['instance'])
        
post_save.connect(create_profile, sender=User)
    