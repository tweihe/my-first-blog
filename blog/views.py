from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import EssayMaker

def english_project(request):

    if request.method == 'POST':
        form = EssayMaker(request.POST)

        if form.is_valid():
            length = form.cleaned_data['length']
#            request.session['length'] = length
            complexity = form.cleaned_data['complexity']
#            request.session['complexity'] = complexity

            return HttpResponseRedirect('/essay/')

    else:
        form = EssayMaker()



    return render(request, 'blog/english_project.html', {'form': form})

def essay(request):
    length = request.session.get('length')
    complexity = request.session.get('complexity')
    context = {'length': length, 'complexity' : complexity}
    return render(request, 'blog/essay.html', {})

# Create your views here.
