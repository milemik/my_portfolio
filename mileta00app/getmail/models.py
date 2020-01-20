from django.db import models

class MailInfo(models.Model):
    web = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)

    def __str__(self):
        self.web
