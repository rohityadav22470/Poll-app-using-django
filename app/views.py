from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,choice

# Create your views here.
def index(request):
    questions =Question.objects.order_by("-pub_date")[:5]
    q = {"questions": questions}
    return render(request, "index.html",q)

def detail(request, question_id):
    return HttpResponse('The question Id of the question is %s' %question_id)
 
def results(request, question_id):
    response ="You're looking at the result of question id %s"
    return HttpResponse(response %question_id)

def vote(request,question_id):
    return HttpResponse('You are voting on question %s' %question_id)
