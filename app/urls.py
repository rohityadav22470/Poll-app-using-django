from django.urls import path,include
from . import views

app_name ="app"
urlpatterns = [
    path('',views.index,name='index'),
    path("<int:question_id>/",views.detail, name='detail'),
    path("<int:question_id>/result/",views.results,name='results'),
    path('<int:question_id>/result/vote/',views.vote, name="vote")
]
