#coding:utf-8

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    content = models.TextField( )
    
    def __unicode__(self):
    	return self.name


