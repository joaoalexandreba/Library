from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class MyModelName(models.Model):
    """uma classe típica"""
    myFieldName = models.CharField(max_length=40, help_text='Primeiro Nome')

#MetaDados
class Meta(models.Model):
    ordering = ['-myFieldName']

    def get_absolute_url(self):
        """REtorna a url para acessar uma instância específica de MyModelName"""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        #String para representar o objeto MyModelName (no site Admin)
        return self.myFieldName
    
class Genre(models.Model):
    '''Modelo que representa o genero do livro.'''
    name=models.TextField(max_length=200, help_text='Digite o gênero do Livro(ex: ficção ciêntífica)' )

    def __str__(self):
        '''String for representing the Model object'''
        return self.name

class Book(models.Model):
    titulo=models.TextField('Titulo', max_length=200,help_text='Digite o título do Livro' )
    #tipo primitivo que permite estar vinculado a vários objetos
    #Com o on_delete=models.SET_NULL, null=True, conseguimos manter a integridade da referência dos dados
    autor=models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True, help_text='Digite o autor do livro')
    resumo=models.TextField('Resumo',max_length=1000, help_text='Digite o resumo do Livro em 1.000 caracteres')
    isbn=models.CharField('ISBN',max_length=13, help_text='Número ISBN do livro')
    # um gênero pode mais de um livro
    # e um livro pode ter múltiplos gêneros
    # por isso vamos usar o ManyToManyField
    genero=models.ManyToManyField(Genre, help_text='Digite o gênero do livro')

    def display_genero(self):
        return ', '.join(genero.name for genero in self.genero.all()[:3])
    display_genero.short_description = 'Gênero'


    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        """Retorna a url para acessar os detalhes gravados na instancia da classe Book"""
        return reverse('detalhe-do-livro', args=[str(self.id)])

class BookInstance(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    book=models.ForeignKey('Book', on_delete=models.SET_NULL, null=True,help_text='')
    dataDeDevolucao=models.DateField(null=False)

#detalhes da versão do livro
    imprint = models.CharField(max_length=300, null=True)

    LOAN_STATUS=(
        ('m', 'Em manutenção'),
        ('e', 'Emprestado'),
        ('d', 'Disponível'),
        ('r', 'Reservado'),
    )
    status=models.CharField(
        max_length=1,
        choices= LOAN_STATUS,
        blank= True,
        default='m',
        help_text='Disponibilidade do livro',
        )
    
    

    class Meta:
        ordering = ['-dataDeDevolucao']
    
    def __str__(self):
        #string que representa uma instância do modelo
        return f'{self.id} ({self.book.titulo})'

class Autor(models.Model):
    nome=models.CharField('Nome',max_length=100)
    sobrenome=models.CharField('Sobrenome',max_length=100)
    #blank=True indica que o campo pode ficar em branco
    dataDeNascimento=models.DateField('Data de Nascimento',null=True,blank=True)
    dataDeMorte=models.DateField('Data de Morte',null=True,blank=True)
    # outros campos e métodos
    class Meta:
        ordering=['sobrenome', 'nome']#ordenação dos dados por nome e sobrenome

    def get_absolute_url(self):
        """Retorna a url para acessar os detalhes gravados na instancia da classe Autor"""
        return reverse('informações-do-autor', args=[str(self.id)])
    def __str__(self):
        return '{} ({})'.format(self.sobrenome, self.nome) 



