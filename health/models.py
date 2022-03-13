from django.conf import settings
from django.db import models


class Symptom(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class Submission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='submissions',
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    verdict = models.CharField(max_length=255, null=True, blank=True)


class UserSymptom(models.Model):
    submisson = models.ForeignKey(Submission,
                                  related_name='symptoms',
                                  on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptom,
                                related_name='user_symptons',
                                on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
