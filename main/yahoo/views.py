from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import CommoditiesForm

from .yahoo_call import YahooCall
from .gpt_call import OpenAi


# Create your views here
def index(request):
    if request.method == 'POST':
        form = CommoditiesForm(request.POST)
        if form.is_valid():
            # calls 
            # bla bla
            return None
    else:
        form = CommoditiesForm()

    return render(request, 'index.html', {form:form})
