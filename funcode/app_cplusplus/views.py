import random
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from app_cplusplus.models import MCplusplus

def randquestionid():
    return int(random.uniform(0, len(MCplusplus.objects.all())))

nowquestionid = randquestionid()
# Create your views here.
def index(request):
    global nowquestionid
    question = MCplusplus.objects.all()[nowquestionid].question
    return render_to_response('index.html', {'question': question})

def judge(request):
    global nowquestionid
    answer = request.GET.get('answer', 'None')
    if answer == MCplusplus.objects.all()[nowquestionid].solution:
       nowquestionid = randquestionid()
    return index(request)