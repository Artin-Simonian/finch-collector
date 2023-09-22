from django.shortcuts import render

# Create your views here.

finches = [
    {'name': 'bobby', 'size': 'large', 'age': 4},
    {'name': 'Lily', 'size': 'medium', 'age': 2},
    {'name': 'Finchy', 'size': 'small', 'age': 1},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })
