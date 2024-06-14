from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from bboard.models import Bb
# Create your views here.
from django.http import HttpResponse
import requests

def index(request):
    template = loader.get_template('bboard/index.html')
    req = requests.get('https://jsonplaceholder.typicode.com/todos/').json()
    res = req[0]
    # qwe = str(res)
    context = {'res': res}
    return HttpResponse(template.render(context, request))
    # return HttpResponse(str(res))