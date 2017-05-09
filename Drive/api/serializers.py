from rest_framework import serializers
from .models import Calendar
from .models import Login

"""
class CalendarSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Calendar
		fields=('usuario','password','year','month','dia','evento','direccion','descripcion','hora')
"""
class CalendarSerializer(serializers.ModelSerializer):
	class Meta:
		model=Calendar
		fields=('usuario','password','year','month','dia','evento','direccion','descripcion','hora')

class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model=Login
		fields=('usuario','password')

