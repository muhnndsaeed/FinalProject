from django.db import models
from django.contrib.auth.models import User

# Create your models here.


'''
this class for profile to record the information
'''
class Profile(models.Model):
    image=models.URLField()
    name= models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    abstract = models.TextField()
    experience = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

'''
this class for Blog Confused about the title and description
'''
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
'''
this class for Consultation Confused about the title and description
'''
class Consultation(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


'''
this class to write comments in Blogs
'''
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
'''
this class to wraite comments in Consultations
'''
class ConComment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    consultation = models.ForeignKey(Consultation,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)












