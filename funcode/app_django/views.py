from django.shortcuts import render
from django.shortcuts import render_to_response
from app_django.models import DataBase

# Create your views here.
def index(request):
    first_question = DataBase.objects.all()[0].question
    return render_to_response('index.html', {'question': first_question})

def judge(request):
    return request.GET['answer']
    
