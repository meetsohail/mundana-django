from django.shortcuts import render


def index(request):
    return render(request, 'frontend/pages/home.html')


def category(request):
    return render(request, 'frontend/pages/category.html')
