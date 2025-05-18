from abc import ABC, abstractmethod
import random as rd

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao_realizada = transacao.registrar(conta)

        return transacao_realizada

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    @property
    def contas(self):
        return self._contas

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def data_nascimento(self):
        return self._data_nascimento

class Conta:
    _numeros_usados = []
    
    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        Conta._numeros_usados.append(numero)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, numero, cliente):
        if numero in cls._numeros_usados:
            while True:
                numero = rd.randint(0, 1000000)
                if numero not in cls._numeros_usados:
                    break
        
        return cls(numero, cliente)

class ContaCorrente(Conta):
    _numero_saques = 0

    def __init__(self, numero, cliente, limite=500.0, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        if self._saldo < valor:
            print("Saldo insuficiente para saque.")
            return False
        elif valor > self._limite:
            print("Valor excede o limite para saldo.")
            return False
        elif self._numero_saques >= self._limite_saques:
            print("Valor de numeros de saque excede o limite diario.")
            return False
        elif valor <= 0:
            print("Valor para saque deve ser maior que zero.")
            return False
        else:
            self._numero_saques += 1
            self._saldo = self._saldo - valor
            print("Saque realizado com sucesso!")
            return True  
        
    def depositar(self, valor):
        if valor <= 0:
            print("Valor para deposito deve ser maior que zero.")
            return False
        else:
            self._saldo = self._saldo + valor
            print("Deposito realizado com sucesso!")
            return True

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        if conta.depositar(self._valor):
            return f"Foi depositado R${self._valor: .2f} na conta numero {conta.numero}"
        
        return "A operacao de deposito nao foi concluida."

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        if conta.sacar(self._valor):
            return f"Foi sacado R${self._valor} da conta numero {conta.numero}"
        
        return "Operacao de saque nao foi concluida."

class Historico:
    def __init__(self):
        self._transacoes = []
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

    @property
    def transacoes(self):
        return self._transacoes