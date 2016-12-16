from django.shortcuts import render

def english_project(request):
    return render(request, 'blog/english_project.html', {})

# Create your views here.
