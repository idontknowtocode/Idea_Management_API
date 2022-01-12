from django.db import models
from uuid import uuid4

class Idea:
    id = models.UUIDField(primary_key=True, default=uuid4),
    active = models.BooleanField(defaut=True),
    title = models.CharField(max_length=200,null=False,blank=False)
    highlight = models.ForeignKey(Highlight, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return title

    @property
    def get_highlights(self):
        return Highlight.objects.filter(id = self.id)



class Highlight:
    id = models.UUIDField(primary_key=True, default=uuid4)
    active = models.BooleanField(default=True),
    text = models.TextField(max_length=1000,null=False,blank=False)

    def __str__(self):
        return text
