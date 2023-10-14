from django.contrib import admin
from .models import *

class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'question_phrase')

admin.site.register(Questions, QuestionModelAdmin)
admin.site.register(Possibilities)
admin.site.register(Replies)
admin.site.register(Matches)
