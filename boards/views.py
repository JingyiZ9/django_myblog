from django.shortcuts import render
from django.http import HttpResponse
from .models import Board


# Create your views here.

# receive a request as a parameter
# returns a response as a result
def home(request):
    #list all the objects in the Board
    boards = Board.objects.all()
    #create an empty list to store the board names
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)