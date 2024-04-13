from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    print("test function is called from view")
    date = datetime.datetime.now()
    return HttpResponse("<h1> Hello this is index page </h1>")

def about(request):
    # return HttpResponse("<h1> This is about page</h1>")
    return render(request,"about.html",{})