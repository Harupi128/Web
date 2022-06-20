from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
def top(request):
    context = {'name': '晴喜'}
    return render(request, 'myprofile/top.html', context)

def resume(request):
    return render(request, 'myprofile/resume.html')