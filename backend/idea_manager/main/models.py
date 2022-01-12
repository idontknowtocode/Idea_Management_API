from django.db import models
from uuid import uuid4

class Idea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4),
    active = models.BooleanField(default=True),
    title = models.CharField(max_length=200,null=False,blank=False)
    #highlight = models.ForeignKey(Highlight, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    

class Highlight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    active = models.BooleanField(default=True),
    text = models.TextField(max_length=1000,null=False,blank=False)
    idea = models.ForeignKey(Idea,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.text

    @property
    def get_idea(self):
        return self.idea.title






