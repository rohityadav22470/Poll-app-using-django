from django.urls import path,include
from . import views

app_name ="app"
urlpatterns = [
    # path('',views.index,name='index'),
    # path("<int:question_id>/",views.detail, name='detail'),
    # path("<int:question_id>/result/",views.results,name='results'),
    path('',views.IndexView.as_view(),name='index'),
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("<int:pk>/",views.DetailView.as_view(), name='detail'),
    path("<int:pk>/result/",views.ResultView.as_view(),name='results'),
    path('<int:question_id>/result/vote/',views.vote, name="vote")
]
