from django.http import HttpResponse

# methods
def home(request):
    return HttpResponse("You are at home page.")

def about(request):
    return HttpResponse("You are at about page.")

def contact(request):
    return HttpResponse("You are at contact page.")