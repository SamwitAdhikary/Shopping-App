from django.shortcuts import render, HttpResponse

# Create your views here.
def blogIndex(request):
    return HttpResponse('This is blog page')