from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.question
    def was_published_recently(self):
        now=timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_test=models.CharField(max_length=1000)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_test