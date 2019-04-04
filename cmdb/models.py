from django.db import models


# Create your models here.

class auth_user(models.Model):
    print("models的类型",type(models.Model))
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    last_login = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'auth_user'