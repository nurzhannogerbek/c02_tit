from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'persons'
        ordering = ['id']
