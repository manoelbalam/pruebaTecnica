from django.db import models

class User(models.Model):
    UserAccess = models.CharField("UserAccess", max_length=50)
    PassAccess = models.CharField("PassAccess", max_length=50)
    TokenAccess = models.CharField("TokenAccess", max_length=240)
    ExpirationAccess = models.DateField("ExpirationAccess")

    def __str__(self):
        return self.name