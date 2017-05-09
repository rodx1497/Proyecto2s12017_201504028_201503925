# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Calendar (models.Model):
	
	usuario=models.CharField(max_length=200)
	password=models.TextField(max_length=200)
	year=models.TextField(max_length=200)
	month=models.TextField(max_length=200)
	dia=models.TextField(max_length=200)
	evento=models.TextField(max_length=200)
	direccion=models.TextField(max_length=200)
	descripcion=models.TextField(max_length=200)
	hora=models.TextField(max_length=200)
	
	def __unicode__(self):
		return self.usuario

class Login (models.Model):
	usuario=models.CharField(max_length=200)
	password=models.TextField(max_length=200)
	