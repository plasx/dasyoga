from django.db import models


class Classes(models.Model):
    class = models.CharField(max_length=20)


class Instructor(models.Model):
    name = models.CharField(max_length=32)
    bio = models.TextField()
    photo = models.FilePathField(path="/img")
    hometown = models.CharField(max_length=32)
    philosophy = models.TextField()
    classes = models.ManyToManyField('Classes')
    experience = models.TextField()
    certifications = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

