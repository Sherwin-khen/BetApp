from django.db import models

# Create your models here.
class Bet(models.Model):
    betting = models.CharField()
    payment = models.CharField(_(""), max_length=50)