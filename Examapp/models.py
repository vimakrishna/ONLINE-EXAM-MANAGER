from django.db import models

class QuestionDb(models.Model):


    question = models.CharField(max_length=100)

    option_A = models.CharField(max_length=50)

    option_B = models.CharField(max_length=50)

    option_C = models.CharField(max_length=50)

    option_D = models.CharField(max_length=50)

    correct_answer = models.CharField(max_length=50)

    def __str__(self):
        return self.question



