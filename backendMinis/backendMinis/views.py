from django.http import HttpResponse

def test(request):
    print("test function is called from view")
    return HttpResponse("<h1> Hello this is index page </h1>")