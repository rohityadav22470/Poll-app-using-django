from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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

# @login_required
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
# def login(request):
#     if request.method=="POST":
#         username=request.POST.get("username")
#         password=request.POST.get("password")
#         if User.objects.filter(username=username).exists():



#     return render(request,"login.html")

def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        person=request.POST.get("first_name")
        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "USERNAME ALREADY EXISTS. WRITE ANOTHER")
            return redirect("/register/")
        user=User.objects.create_user(
            username=username,
            first_name=person
            )
        user.set_password(password) #for encrypted password
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect("/login/")
    return render(request,"register.html")


# jhhj
# def register(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         email=request.POST['email']
#         pass1=request.POST['password']
#         pass2=request.POST['password1']
#         if pass1==pass2:
#             if  User.objects.filter(email=email).exists():
#                 messages.info(request,'Email already Used')
#                 return redirect('register')
#             elif  User.objects.filter(username=username).exists():
#                 messages.info(request,'username already exists')
#                 return redirect('register')
#             else:
#                 user= User.objects.create_user(username= username, email=email, password=pass1)
#                 user.save()
#                 return redirect('login')
#     else:
#         messages.info(request, 'Password not same.')
#         return redirect('register')
    
#     return render(request, 'register.html')

# # for new login
def login_page(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)

        # if request.POST['register']:
        #     return redirect('register')
        if user is not None:
            auth.login(request, user)
            person=User.objects.filter(username=username)
            print(person)
            return render(request,'index.html', {"username": person})
        else:
            messages.info(request, "INVALID CREDENTIALS!!!")
            return redirect('login')

    return render(request,'login.html')

# # for logout functionality
def logout(request):
    auth.logout(request)
    return redirect('/')