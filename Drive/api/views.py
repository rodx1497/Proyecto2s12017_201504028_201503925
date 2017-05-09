# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import Calendar
from serializers import CalendarSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.http import HttpResponse

# Create your views here.

	

class CalendarViewSet(viewsets.ModelViewSet):
	queryset=Calendar.objects.all()
	serializer_class=CalendarSerializer

	
class ListaEventos(APIView):
	def get(self,request,format=None):
		calendar=Calendar.objects.all()
		serializer=CalendarSerializer(calendar)
		return Response(serializer.data)
	def post(self,request,format=None):
		serializer=CalendarSerializer(data=request.DATA)
		if serializer.is_valid():
			return Response(serializer.data,status=status.HTTP_201_CREATED)
			pass
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DetallesEvento(APIView):
	def get_object(self,pk):
		try:
			return Calendar.objects.get(pk=pk)
			pass
		except Calendar.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		calendar=self.get_object(pk)
		serializer=CalendarSerializer(calendar)
		return Response(serializer.data)
	def put(self,request,pk,format=None):
		calendar=self.get_object(ok)
		serializer=CalendarSerializer(calendar,data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
			pass
	def delete(self,request,pk,format=None):
		calendar=self.get_object(pk)
		calendar.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)