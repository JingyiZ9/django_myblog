from django.shortcuts import render
from django.http import HttpResponse
from .models import Board


# Create your views here.

# receive a request as a parameter
# returns a response as a result
def home(request):
    #list all the objects in the Board
    boards = Board.objects.all()

    return render(request, 'home.html', {'boards':boards})