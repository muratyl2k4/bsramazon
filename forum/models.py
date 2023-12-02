from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    Category = models.CharField(max_length=500)    

    def __str__(self):
        return self.Category

class Subject(models.Model):
    User = models.ForeignKey(User , null=True , blank=True,on_delete=models.SET_NULL)
    Subject_Category = models.ForeignKey(Category , null=True , blank=True , on_delete=models.SET_NULL)
    Title = models.CharField(max_length=500)
    Text = models.TextField()
    DateTime = models.DateTimeField(auto_now=True)
    Closed = models.BooleanField(default=False)
    Deleted = models.BooleanField(default=False)

    def count_comments(self):
        return Answer.objects.filter(Subject = self.id).count()   

class Answer(models.Model):
    User = models.ForeignKey(User , null=True , blank=True,on_delete=models.SET_NULL)
    Subject = models.ForeignKey(Subject , on_delete=models.CASCADE)
    # If reply to another answer
    Replied_To = models.ForeignKey('self' , null=True ,blank=True, on_delete=models.SET_NULL)
    
    Text = models.TextField()
    DateTime = models.DateTimeField(auto_now=True)
    Verified_Answer = models.BooleanField(default=False)
    Deleted = models.BooleanField(default=False)
    