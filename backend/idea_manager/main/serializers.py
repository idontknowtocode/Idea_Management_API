from rest_framework import serializers, status
from .models import Idea, Highlight

class Highlight_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = '__all__'

class Idea_Serializer(serializers.ModelSerializer):
    highlight = Highlight_Serializer(read_only=True,many=True)

    class Meta:
        model = Idea
        fields = '__all__'


