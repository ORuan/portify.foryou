from django.db import models
from django.contrib.auth.models import User

class Experience(models.Model):
    _local = models.CharField(max_length=20, null=False)
    when_started = models.DateField(null=False)
    when_end = models.DateField(null=False)
    job = models.CharField(max_length=70, null=False)

class Skills(models.Model):
    skill_name = models.CharField(max_length=20, null=False)
    exp_time = models.PositiveIntegerField(null=False)

class Portify(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    link_github = models.URLField(max_length=150, null=False)
    link_linkedin = models.URLField(max_length=150, null=False)
    avatar = models.URLField(max_length=150, null=False)
    user_id  = models.ForeignKey(User, on_delete=models.CASCADE)
    experience_id = models.ForeignKey(Experience, on_delete=models.CASCADE, null=True)
    skills_id = models.ForeignKey(Skills, on_delete=models.CASCADE, null=True)
