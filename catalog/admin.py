from django.contrib import admin
from .models import Autor, Genre, Book, BookInstance

# Register your models here.

#admin.site.register(Autor)
#admin.site.register(Genre)
#admin.site.register(Book)
#admin.site.register(BookInstance)

class AutorAdmin(admin.ModelAdmin):
    list_display=('sobrenome','nome','dataDeNascimento','dataDeMorte')
    fields = ['nome','sobrenome',('dataDeNascimento','dataDeMorte')] #filtros
    #fieldsets = ((None, {'fields': ('book','imprint','id')}))

admin.site.register(Autor, AutorAdmin)    

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    #list_display = ('nome')
    pass

class BookInstanceInline(admin.TabularInline):
    model=BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','display_genero')
    inlines = [BookInstanceInline]
    #pass

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    #list_display = ('id','display_book','data')
    #pass
    list_filter=('status','imprint','dataDeDevolucao')
    fieldsets = ((None, {
        'fields': ('book', 'id')}),
        ('Disponível', {'fields': ('status','dataDeDevolucao')}),
        )
