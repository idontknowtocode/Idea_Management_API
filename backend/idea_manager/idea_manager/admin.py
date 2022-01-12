from django.contrib import admin
from django.conf import settings
from .models import Highlight , Idea

@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Highlight
        fields = '__all__'


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_filter=['active']
    search_fields=['title']
    class Meta:
        model = Idea
        fields = '__all__'

admin.site.register(Idea,IdeaAdmin)
admin.site.register(Highlight,HighlightAdmin)