#conding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from .models import Course
from .forms import CourseForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import *
import datetime

def add(request):
	if request.method == "GET":
		form = CourseForm()
		return render_to_response("add.html",{"form":form},context_instance=RequestContext(request))
	if request.method == "POST":
		'''
		form = CourseForm(request.POST)
		form.save()
		'''
		b = Course(name=request.POST['name'],title=request.POST['title'],content=request.POST['content'])
		b.save()
		form = CourseForm(instance=b)
		return redirect("/base1")
		'''
		return render_to_response("add.html",{"from":form,"b":b},context_instance=RequestContext(request))
		'''
	
def test(request,offset):
	offset = int(offset)
	dt = datetime.datetime.now()
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)
def base1(request):
	b = Course.objects.all().order_by("-id")
	if request.method == "GET":
		if request.user.is_authenticated():
			return render_to_response("base1.html",{'name':request.user.username,"b":b},context_instance=RequestContext(request))
		else:
			return render_to_response("base1.html",{"b":b},context_instance=RequestContext(request))
	'''
	b = Course.objects.all().order_by("-id")
	return render_to_response("base1.html",{"b":b},context_instance=RequestContext(request))
	'''
	'''
	form = CourseForm()
	if request.method == "GET":
		return render_to_response('base1.html',{'form':form},context_instance=RequestContext(request))
		
	
	if request.method == "POST":
		a = Course.objects.create(name=request.POST['name'],title=request.POST['title'],content=request.POST['content'])
		form = CourseForm(instance=a)
		b = Course.objects.all().order_by("-id")
		return render_to_response("base1.html",{"a":a,"form":form,"b":b},context_instance=RequestContext(request))
	'''
	
def register(request):
        form = UserCreationForm()
        if request.method == 'GET':
                return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))
        if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                        form.save()
                        new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
                        login(request, new_user)
                        return redirect("/base1")
                return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))


def home(request):
	if request.method == "GET":
		return render_to_response("home.html",{},context_instance=RequestContext(request))
	if request.method == "POST":
		form = CourseForm()
		a = Course.objects.create(name=request.POST,title=request.POST,content=request.POST)
		return render_to_response("home.html",{'a':a,'form':form},context_instance=RequestContext(request))



'''
def home(request):
	all = Course.objects.all().order_by("-id")
	
	f = CourseForm()
	print f
	return render_to_response("home.html",{"all":all,'f':f},context_instance=RequestContext(request))

'''
s3=0

def hello(request,d1,s2):
	global s3
	d = {}
	d['d1'] = d1
	d['s2'] = s2
	s3 += 1
	d['s3'] = s3
	if  request.method == "POST":
		a = CourseForm(request.POST)
		if a.is_valid():
			a.save()

	return redirect("/index")
    #return HttpResponse("Hello %s world %s" % (d1,s2))
def delete(request,id):
    a =  Course.objects.get(id=id)
    a.delete()
    return redirect("/index")

def edit(request,id):
    a =  Course.objects.get(id=id)
    form = CourseForm(instance=a)   
    return render_to_response("edit.html",
    	{"form":form,"a":a},context_instance=RequestContext(request))

def edit_save(request,id):
    a =  Course.objects.get(id=id)    
    a1 = CourseForm(request.POST,instance=a)
    if a1.is_valid(): 
          a1.save()
    return redirect("/index")
