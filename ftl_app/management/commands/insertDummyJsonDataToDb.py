from django.contrib.auth.models import User
from ftl_app.models import ActivityPeriod
from ftl_app.models import Profile
from django.core.management.base import BaseCommand
import json
from datetime import datetime



class Command(BaseCommand):
	help = "Insert Json data to db"

	def add_arguments(self,parser):
		parser.add_argument('-json','--json_file',type=str)


	#changing string to date object
	def string_to_datetime(self,string_date_time):
		if string_date_time:
			datetime_object = datetime.strptime(string_date_time, '%b %d %Y %I:%M%p')
			return datetime_object

		return None

	def handle(self,*args,**kwargs):
		json_file = kwargs['json_file']

		try:

			with open(kwargs['json_file'], "r") as f:
				json_data = json.load(f)  #returns json object as dictionary
		
		except IOError as e:

			Print(e)
		
		if json_data['members']:
			for data in json_data['members']:

				try:
					#create user 
					user = User.objects.create_user(username=data.get('real_name',None),password="123")
				
				#get exception if there is duplicate entry
				except Exception as e:  
					user = None  
					print(e)

					
				if user:

					#save the id and tz to profile model related to user
					user.profile.u_id = data.get('id',None)
					user.profile.time_zone = data.get('tz',None)
					user.profile.save()

					
					if data['activity_periods']:

						#create activity periods belongs to each user 
						activity_pds = [ActivityPeriod(user=user,start_time=self.string_to_datetime(value.get('start_time',None)),end_time=self.string_to_datetime(value.get('end_time',None) )) for value in data['activity_periods'] ]
						user.activity_period.bulk_create(activity_pds)