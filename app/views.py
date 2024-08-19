from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question,choice
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
# def index(request):
#     questions =Question.objects.order_by("-pub_date")[:5]
#     q = {"questions": questions}
#     return render(request, "index.html",q)


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question Id does not exist.")
#     # question=get_object_or_404(Question, pk=question_id)...this is the shortcut for try and except 
#     return render(request,"detail.html", {"question":question})
 


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'result.html',{'question':question})


class IndexView(generic.ListView):
    template_name="index.html"
    context_object_name= "questions"
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")
class DetailView(generic.DetailView):
    template_name = "detail.html"
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
    
  
class ResultView(generic.DetailView):
    model = Question
    template_name="result.html"


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
    
    # User auth
def login(request):
     
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        person=request.POST["first_name"]
        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "USERNAME ALREADY EXISTS. WRITE ANOTHER")
            return redirect(request, "register.html")
        
        user=User.objects.create(
            username=username,
            first_name=person
            )
        
        user.set_password(password) #for encrypted password
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect(request,"login.html")
    return render(request,"register.html")
