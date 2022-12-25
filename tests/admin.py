from django.contrib import admin
from .models import SetTests, NameTest, Question, Answer



class NameTestAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("settest",)}  # если нужно в админке генерировать slug
    list_display = ('settest', 'title',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('nametest', 'text',)



admin.site.register(Question, QuestionAdmin)
admin.site.register(SetTests)
admin.site.register(NameTest, NameTestAdmin)
admin.site.register(Answer, AnswerAdmin)
