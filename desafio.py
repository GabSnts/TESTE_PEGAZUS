#DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo ,
#aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta,
#e a realização das operações de saque e deposito do saldo da conta

import psycopg2
import random

class DataDb:
    def __init__(self) -> None:
        self.connection = psycopg2.connect(database="banco", user="postgres", host="localhost", password="postgres", port="5432")
        self.cursor = self.connection.cursor()
        self.cursor.execute("ROLLBACK")
   
    def create_table(self, table, description):
        self.cursor.execute(f'CREATE TABLE {table} ({description})')
        self.connection.commit()

    def select_table(self, query, value):
        if type(value) == tuple:
            self.cursor.execute(query, value)
        else:    
            self.cursor.execute(query, (value,))
        return self.cursor.fetchall()[0][0]

    def update_table(self, query, values):
        self.cursor.execute(query, values)
        self.connection.commit()
            
    def insert_table(self, table, values):
        self.cursor.execute(f'INSERT INTO {table} (conta, nome, cpf, saldo) VALUES (%s, %s, %s, %s)', values)
        self.connection.commit()

    def close_connection(self):
        self.connection.close()
        self.cursor.close()

class ContaBancaria:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.conta = f'{random.randint(100000, 999999)}-{random.randint(0, 9)}'
        self.saldo = 0
        self.table = "conta_bancaria"
        self.datadb = DataDb()

    def create_table(self):
        return self.datadb.create_table(self.table, "id SERIAL PRIMARY KEY, conta VARCHAR(20), nome VARCHAR(255), cpf VARCHAR(11), saldo FLOAT")

    def insert_table(self):
        return self.datadb.insert_table(self.table, (self.conta, self.nome, self.cpf, self.saldo))
    
    def get_conta(self, cpf):
        return self.datadb.select_table(f'SELECT conta FROM {self.table} WHERE cpf = %s', cpf)
    
    def get_saldo(self, conta = None, cpf = None):
        self.conta = self.get_conta(cpf)
        return self.datadb.select_table(f'SELECT saldo FROM {self.table} WHERE conta = %s OR cpf = %s', (conta, cpf))

    def update_saldo(self, valor, conta = None, cpf = None):
        return self.datadb.update_table(f'UPDATE {self.table} SET saldo = %s WHERE conta = %s OR cpf = %s', (valor, conta, cpf))
        
    def depositar(self, valor):
        self.saldo = self.get_saldo(self.conta, self.cpf)

        if valor > 0:
            self.saldo += valor
            self.update_saldo(self.saldo, self.conta, self.cpf)

            return print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            return print("Valor de depósito inválido.")

    def sacar(self, valor):
        self.saldo = self.get_saldo(self.conta, self.cpf)

        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.update_saldo(self.saldo, self.conta, self.cpf)

            return print(f"Saque de R${valor} realizado com sucesso.")
        else:
            return print("Saldo insuficiente ou valor de saque inválido.")

    def consultar_saldo(self):
        self.conta = self.get_conta(self.cpf)
        self.saldo = self.get_saldo(self.conta, self.cpf)
        return print(f"Saldo da conta {self.conta}: R${self.saldo}")

    def __str__(self):
        return f"Conta {self.conta} - Nome: {self.nome}, CPF: {self.cpf}, Saldo: R${self.saldo}"

recurso = input("Qual recurso deseja acessar? (Criar Conta Bancária, Consultar Saldo, Depósito ou Saque): ")
nome = input("Informe o nome do titular da conta: ")
cpf = input("Informe o CPF do titular da conta: ")
conta = ContaBancaria(nome, cpf)
check_deposito = None

try:
    conta.create_table()
except:
    pass

if recurso == "Criar Conta Bancária":
    check_deposito = (input("Deseja realizar um depósito inicial? (Sim/Não) ")).upper()
    conta.insert_table()
    print(conta)

if recurso == "Depósito" or check_deposito == "SIM":
    deposito = float(input("Informe o valor do depósito: "))
    conta.depositar(deposito)
    print(conta)

if recurso == "Saque":
    saque = float(input("Informe o valor do saque: "))
    conta.sacar(saque)

if recurso == "Consultar Saldo":
    conta.consultar_saldo()


