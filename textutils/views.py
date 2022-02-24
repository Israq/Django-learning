#I have created this site
from django.http  import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse("hello israq");
def excercise(request):
    return HttpResponse('''<h1>Israq</h1> ,<a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7" >django code with harry </a>''');
def index(request):
    params = {'name':'israq', 'place':'ctg'}
    return render(request, 'index.html', params)
    #return HttpResponse('''<a href="newlineremove" >This is a link</a>''');
def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    return HttpResponse("removepunc");
def capitalizefirst(request):
    return HttpResponse("Capfirst");
def newlineremove(request):
    return HttpResponse("newlineremove");
def spaceremove(request):
    return HttpResponse("spaceremove");
def charcount(request):
    return HttpResponse("charcount");