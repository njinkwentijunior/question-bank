from django.contrib import admin
from .models import Category, Tag, Question, Exam

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Exam)
