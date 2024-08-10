from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def tab1(request):
    return render(request, 'tab1.html')

def tab2(request):
    return render(request, 'tab2.html')

def tab3(request):
    return render(request, 'tab3.html')
