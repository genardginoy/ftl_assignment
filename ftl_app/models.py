from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	u_id = models.CharField(max_length=100)
	time_zone = models.CharField(max_length=50)


	def __str__(self):
		return "User {} ".format(self.user.username)


class ActivityPeriod(models.Model):
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='activity_period') 

	def __str__(self):
		return "User {} , start time : {} - end time : {}".format(self.user.username,self.start_time,self.end_time)

