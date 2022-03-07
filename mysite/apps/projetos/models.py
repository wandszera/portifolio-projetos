from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name= models.CharField('Nome', max_length=150)
    description= models.TextField('Descrição', blank=True, null=True)
    owner= models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

    def __str__(self):
        return self.name
    


class Projeto(models.Model):
    name = models.CharField('Nome do Projeto', max_length=150)
    description = models.TextField('Descrição do Projeto', blank=True, null=True)
    photo = models.ImageField('Imagem do Projeto', upload_to='fotos')
    category = models.ManyToManyField(Category)
    owner= models.ForeignKey(User, on_delete=models.CASCADE, related_name='projeto')

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['id']

    def __str__(self):
        return self.name
