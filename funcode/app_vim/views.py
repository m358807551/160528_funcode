import random
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from app_vim.models import Mvim
from PyQt4.QtCore import *

def randquestionid():
    return int(random.uniform(0, len(Mvim.objects.all())))

nowquestionid = randquestionid()
nQuestionSum = len(Mvim.objects.all())
nAnswerSum = 1 
nRightSum = 0

# Create your views here.
def index(request):
    global nowquestionid
    global nAnswerSum
    global nQuestionSum
    global nRightSum
    question = Mvim.objects.all()[nowquestionid].question
    return render_to_response('index.html', {'app':'vim',
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
    solution = QString(Mvim.objects.all()[nowquestionid].solution)
    solution = solution.replace(QRegExp('\s'), '')
    if answer == solution:
        nowquestionid = randquestionid()
        nRightSum += 1
    return index(request)
