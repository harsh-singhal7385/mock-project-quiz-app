from django.db import models


# Create your models here.
class AddQuiz(models.Model):
    # quizId = models.CharField(max_length=200, null=False, primary_key=True)
    subject_name = models.CharField(max_length=300, null=True)
    instructor_name = models.CharField(max_length=300, null=True)
    category = models.CharField(max_length=300, null=True)
    quiz_time = models.IntegerField(null=True)
    date = models.DateField()
    # desc = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.subject_name


class Question(models.Model):
    quizId = models.ForeignKey(
        AddQuiz, default=None, null=False, blank=False, on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True)
    option_a = models.TextField(null=True, blank=False)
    option_b = models.TextField(null=True, blank=False)
    option_c = models.TextField(null=True, blank=False)
    option_d = models.TextField(null=True, blank=False)
    marks = models.IntegerField(null=True)
    answer = models.CharField(max_length=1, null=True)

    def __str__(self):
        return str(self.quizId)
