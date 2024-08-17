from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question,choice
from django.db.models import F
from django.urls import reverse

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'result.html',{'question':question})



def vote(request, question_id):
    question =get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, choice.DoesNotExist):
        return render(request, 'detail.html', {"question":question, "error_message": "You didn't selected a choice"})
    else:
        selected_choice.votes =F('votes')+1
        selected_choice.save()
    return HttpResponseRedirect(reverse('app:results', args=(question_id,)))
    
