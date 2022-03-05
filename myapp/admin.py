from django.contrib import admin
from .models import Article, Coment
# Register your models here.


class ComentInline(admin.TabularInline):
    model = Coment
    extra = 0 # new
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ComentInline,
    ]

admin.site.register(Article,ArticleAdmin)
admin.site.register(Coment)