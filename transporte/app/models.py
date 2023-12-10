from this import d
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    telefone_principal = models.CharField(max_length=11)
    telefone_opcional = models.CharField(max_length=11, blank=True)
    # email = models.EmailField(max_length=100, unique=True)
    # senha = models.CharField(max_length=128)
    datansc = models.DateField()
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class GovernAgency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=11)
    # email = models.EmailField(max_length=100, unique=True)
    # senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class Service(models.Model):
    descricao = models.CharField(max_length=200)
    
    def __str__(self):
        id = str(self.id)
        return id

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=11)
    # email = models.EmailField(max_length=100, unique=True)
    # senha = models.CharField(max_length=128)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class TypeFeedback(models.Model):
    descricao = models.CharField(max_length=200)
    
    def __str__(self):
        id = str(self.id)
        return id

class Feedback(models.Model):
    tipo = models.ForeignKey(TypeFeedback, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    org = models.ForeignKey(GovernAgency, on_delete=models.CASCADE)
    observacao = models.TextField()
    data_reclamacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    class Status(models.IntegerChoices):
        NEW = 0
        PENDING = 1
        COMPLETE = 2
        CANCELLED = 99
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)

class FBCompany(models.Model):
    reclamacao = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Company, on_delete=models.CASCADE)
    