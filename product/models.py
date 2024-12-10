from django.db import models

class Produtos(models.Model):

    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    data_atualizaçao = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.nome
    
