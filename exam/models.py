from django.db import models
from django.contrib.auth import get_user_model

class Question(models.Model):
    CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    )

    text = models.CharField(max_length=1023)
    image = models.ImageField(upload_to='question/question_image')
    choice_1 = models.CharField(max_length=511)
    choice_2 = models.CharField(max_length=511)
    choice_3 = models.CharField(max_length=511)
    choice_4 = models.CharField(max_length=511)
    answer = models.CharField(max_length=1, choices=CHOICES)
    question_maker = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:10:] + "  |  " + self.question_maker

