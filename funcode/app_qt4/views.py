import random
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from app_qt4.models import Mqt4
from PyQt4.QtCore import *

def randquestionid():
    return int(random.uniform(0, len(Mqt4.objects.all())))

nowquestionid = randquestionid()
nQuestionSum = len(Mqt4.objects.all())
nAnswerSum = 1 
nRightSum = 0

# Create your views here.
def index(request):
    global nowquestionid
    global nAnswerSum
    global nQuestionSum
    global nRightSum
    question = Mqt4.objects.all()[nowquestionid].question
    return render_to_response('index.html', {'app':'qt4',
        'question': question,
        'nQuestionSum': nQuestionSum,
        'nAnswerSum': nAnswerSum,
        'nRightSum': nRightSum,
        'fRightPercent':1.0*nRightSum/nAnswerSum})

def judge(request):
    global nowquestionid
    global nAnswerSum
    global nQuestionSum
    global nRightSum
    nAnswerSum += 1
    answer = QString(request.GET.get('answer', 'None'))
    answer = answer.replace(QRegExp('\s'), '')
    solution = QString(Mqt4.objects.all()[nowquestionid].solution)
    solution = solution.replace(QRegExp('\s'), '')
    if answer == solution:
        nowquestionid = randquestionid()
        nRightSum += 1
    return index(request)
