from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Final/index.html')

def detail(request):
    return render(request, 'Final/detailFlower.html')