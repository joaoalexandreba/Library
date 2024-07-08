from django.shortcuts import render
from catalog.models import Autor, Book, BookInstance, Genre
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'
    queryset = Book.objects.filter(titulo__icontains='dados') # Get 5 books containing the title war
    template_name = 'templates/listaDelivros.html'

    def get_queryset(self):
        return Book.objects.filter(titulo__icontains='dados') # Get 5 books containing the title war
   
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

# Create your views here.
def index(request):

    numeroDeLivros = Book.objects.all().count() #contar o número de livros
    numeroDeCopias = BookInstance.objects.all().count() #contar o número de instancias dos livros
    numeroDeAutores = Autor.objects.all().count()#contar o número de autores
    generos = Genre.objects.count()
    contarLivrosKeyword = Book.objects.filter(titulo_icontains='dados').count()


    context = {
        'Número de livros': numeroDeLivros,
        'Número de cópias': numeroDeCopias,
        'Número de Autores': numeroDeAutores,
        'Generos': generos,
        'contarLivros': contarLivrosKeyword,
    }

    return render(request, 'index.html', context=context)