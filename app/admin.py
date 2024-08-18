from django.contrib import admin
from .models import Question, choice
# Register your models here.

class choiceInline(admin.TabularInline):   #you can also use StackedInline instead of TabularInline
    model=choice
    extra =3
class QuestionView(admin.ModelAdmin):
# Controlling the order of the fields in a model
    # fields=["pub_date","question"]

#Splitting the fields in the different fieldset
    list_display=["question","pub_date", "was_published_recently"]
    fieldsets = (
        ("question Text", {"fields": ["question"],}),
        ("Date Info", {"fields": ["pub_date"]}),
    )
    inlines=[choiceInline]
    

# 

admin.site.register(Question, QuestionView)
# admin.site.register(choice)
