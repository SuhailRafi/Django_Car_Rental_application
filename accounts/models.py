from django.db import models

#    def __str__(self):
#        return self.task

class UserRegistration (models.Model):
    UserName = models.CharField (max_length = 100)
    EmailAddress =models.EmailField (max_length = 50)
    Password =  models.charField (max_length = 50)

    def __str__(self):
        return self.UserName


class UserLogin (models.Model):
    UserName = models.charField (max_length = 100)
    Password = models.charField (max_length = 50)