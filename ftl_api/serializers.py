from rest_framework import serializers
from django.contrib.auth.models import User
from ftl_app.models import Profile,ActivityPeriod




class ActivityPeriodSerializer(serializers.ModelSerializer):
	start_time = serializers.DateTimeField(format='%b %d %Y %I:%M%p',read_only=True)
	end_time = serializers.DateTimeField(format='%b %d %Y %I:%M%p',read_only=True)
	class Meta:
		model = ActivityPeriod
		fields = ['start_time','end_time']



class UserSerializer(serializers.ModelSerializer):
	real_name = serializers.ReadOnlyField(source="username")
	id = serializers.ReadOnlyField(source="profile.u_id")
	tz = serializers.ReadOnlyField(source="profile.time_zone")
	activity_periods = ActivityPeriodSerializer(many=True, read_only=True,source="activity_period")



	class Meta:
		model = User
		fields = ['real_name','id','tz','activity_periods']