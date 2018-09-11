from django.db import models

# Create your models here.
from django.db  import models
from datetime import timedelta
from django.db  import  models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField()

def was_published_recently(self):
    return self.publish_data >= timedelta.now() - timedelta(days=1)
    def __str__(self):              #回显输入的内容
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, models.CASCADE)

    def __str__(self):
        return self.choice_text