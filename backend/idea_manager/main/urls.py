from django.urls import path
from . import views

urlpatterns= [
    path('addidea/',views.AddIdea.as_view(),name='add-idea'),
    path('',views.GetIdeas.as_view(),name='ideas'),
]