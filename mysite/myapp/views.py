from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def index(request) :
    return HttpResponse("<H1>Welcome to homepage</H1>")
def show_datetime(request) :
    now = datetime.datetime.now()
    my_html = "<H1>It is %s.</H1>" % now
    return HttpResponse(my_html)