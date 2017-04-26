from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
class Departamento(models.Model):

    codigo = models.IntegerField
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'


class Cantina(models.Model):

    nome = models.CharField('Cantina', max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cantina'
        verbose_name_plural = 'Cantinas'


class Solicitacao(models.Model):

    usuario = models.CharField('Solicitante', max_length=100)
    departamento = models.ManyToManyField(Departamento, blank=True)
    cantina = models.ManyToManyField(Cantina, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.usuario

    def get_absolute_url(self):
        return reverse('server_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Solicitacao'
        verbose_name_plural = 'Solicitacoes'

