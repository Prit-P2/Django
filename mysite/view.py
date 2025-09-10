from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    #return HttpResponse("Hello world")  
def about(request):
    
    a=request.POST.get('text','default')      
    b="" 
    p='''aeiou'''
    for char in a:
        if char not in p:
            b=b+char
    return HttpResponse(b)
        