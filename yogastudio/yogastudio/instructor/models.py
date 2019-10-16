from django.db import models


class Class(models.Model):
    yogaclass = models.CharField(max_length=20, primary_key=True)
    description = models.TextField()

    def __str__(self):
        return self.yogaclass


class Instructor(models.Model):
    name = models.CharField(max_length=32)
    bio = models.TextField()
    photo = models.FilePathField(path="/img")
    hometown = models.CharField(max_length=32)
    philosophy = models.TextField()
    classes = models.ManyToManyField('Class')
    experience = models.TextField()
    certifications = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name





