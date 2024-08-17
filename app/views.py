from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question,choice

# Create your views here.
def index(request):
    questions =Question.objects.order_by("-pub_date")[:5]
    q = {"questions": questions}
    return render(request, "index.html",q)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Id does not exist.")
    # question=get_object_or_404(Question, pk=question_id)...this is the shortcut for try and except 
    return render(request,"detail.html", {"question":question})
 


def results(request, question_id):
    response ="You're looking at the result of question id %s"
    return HttpResponse(response %question_id)



def vote(request,question_id):
    return HttpResponse('You are voting on question %s' %question_id)
