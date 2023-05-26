from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import First

# Create your views here.
def wish(request):
    return HttpResponse("<h1>Hello Ganesh</h1")

def hello_view(request):
    return HttpResponse("<h2>Hello World</h2>")

def listview(request):
    person_list=First.objects.all()
    return render(request,'firstapp/personlist.html',{'person_list':person_list})
