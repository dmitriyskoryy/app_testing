from django.contrib import admin
from .models import SetTests, NameTest, Question, Answer

#
# class AnswerInline(admin.TabularInline):
#     model = Answer
#     extra = 3
#
#
class NameTestAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("settest",)}  # если нужно в админке генерировать slug
    list_display = ('settest', 'title',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('nametest', 'text',)

#     fieldsets = [
#         (None, {'fields': ['text', 'order']}),
#     ]
    # inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(SetTests)
admin.site.register(NameTest, NameTestAdmin)
admin.site.register(Answer, AnswerAdmin)
