from .models import Idea, Highlight
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import Idea_Serializer, Highlight_Serializer


class AddIdea(APIView):
    def post(self,request,*args,**kwargs):
        data = {}
        for key in request.data.keys():
            data[key] == request.data.get(key)
            if(request.data.get(key)==''):
                return Response({'Error': 'Incorrect Data'}, status = status.HTTP_400_BAD_REQUEST)

        title = data.pop('title')
        try:
            idea = Idea.objects.get(title=title)
            return Response({'Error': 'Idea already exists'},status=status.HTTP_400_BAD_REQUEST)
        except:
            idea = Idea.objects.create(title=title)
            idea.save()
            return Response(Idea_Serializer(idea), status=status.HTTP_201_CREATED)
    
    def get(self,request):
        model= Idea.objects.get(title=request.title)
        serializer = Idea_Serializer(model)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteIdea(APIView):
    def delete(self,request,*args,**kwargs):
        title = request.title
        idea = Idea.objects.filter(title=title)
        func = idea.delete()
        data = {}
        if func:
            data[status] = "Successfully deleted"
        else:
            data[status] = "Failed"
        return Response(data=data)

class GetIdeas(ListAPIView):
    queryset = Idea.objects.all()
    serializer_class=Idea_Serializer 


class AddHighlight(APIView):
    def post(self,request,*args,**kwargs):
        data = {}
        for key in request.data.keys():
            data[key] == request.data.get(key)
            if(request.data.get(key)==''):
                return Response({'Error': 'Incorrect Data'}, status = status.HTTP_400_BAD_REQUEST)
        idea = data.pop('idea')
        text = data.pop('title')
        
        idea_ = Idea.objects.get(title=idea.title)
        if(idea_!=None):
            highlight = Highlight.objects.create(text=text,idea=idea_)
            highlight.save()
            return Response(Highlight_Serializer(highlight),status=status.HTTP_201_CREATED)
            
        else:
            return Response({'Error': 'Idea already exists'},status=status.HTTP_400_BAD_REQUEST)
            #return Response(Idea_Serializer(idea), status=status.HTTP_201_CREATED)
    
    def get(self,request):
        model= Highlight.objects.get(text=request.text)
        serializer = Highlight_Serializer(model)
        return Response(serializer.data, status=status.HTTP_200_OK)
