from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# receive a request as a parameter
# returns a response as a result
def home(request):
    return HttpResponse('Hello, World!')
