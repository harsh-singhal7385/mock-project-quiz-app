from django.db import models

# Create your models here.
class LeaderBoard(models.Model):
    index = models.AutoField(primary_key = True)
    subject_name = models.CharField(max_length=300, null=True)
    user_name = models.CharField(max_length=300, null=True)
    category = models.CharField(max_length=300, null=True)
    quiz_time = models.IntegerField(null=True)
    score = models.CharField(max_length=300, null=True)
    maxscore = models.CharField(max_length=300, null=True)
    datetime = models.DateTimeField(auto_now_add = True)
    # desc = models.TextField(null=True, blank=False)
    
    def __str__(self):
        return self.subject_name + "_" + self.maxscore


class ScoreCard(models.Model):
    index = models.AutoField(primary_key = True)
    subject_name = models.CharField(max_length=300, null=True)
    score = models.CharField(max_length=300, null=True)
    maxscore = models.CharField(max_length=300, null=True)
    result = models.CharField(max_length=300, null=True)
    datetime = models.DateTimeField(auto_now_add = True)
    # desc = models.TextField(null=True, blank=False)
    
    def __str__(self):
        return self.subject_name + "_" + self.score
