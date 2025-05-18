import random as rd
from classes import ContaCorrente, PessoaFisica, Saque, Deposito

def realizar_saque(clientes, cliente):
    if cliente == None:
        print("Falha ao recuperar informacoes sobre usuario... Por favor, verifique se vc ja selecionou um usuario.")
    else:
        conta_atual = None
        lista_contas(clientes, cliente.cpf)
        
        vetor_contas = cliente.contas

        if len(vetor_contas) > 0:
            numero = int(input("Digite o numero da conta escolhida para realizar o saque: "))

            for conta in vetor_contas:
                if conta.numero == numero:
                    conta_atual = conta
                    break
            
            print(f"Conta selecionada: {conta_atual.numero}")
            valor = float(input("Digite o valor a ser sacado: "))
            transacao = Saque(valor)
                
            #Salva a transacao registrada na variavel transacao_registrada
            transacao_registrada = cliente.realizar_transacao(conta_atual, transacao)

            #Adiciona a transacao de deposito no objeto historico da classe ContaCorrente
            conta_atual.historico.adicionar_transacao(transacao_registrada)
        else:
            print("Nenhuma conta foi encontrada no usuario com o cpf informado.")

def realizar_deposito(clientes, cliente):
    if cliente == None:
        print("Falha ao recuperar informacoes sobre usuario... Por favor, verifique se vc ja selecionou um usuario.")
    else:
        conta_atual = None
        lista_contas(clientes, cliente.cpf)
        
        vetor_contas = cliente.contas

        if len(vetor_contas) > 0:
            numero = int(input("Digite o numero da conta escolhida para realizar o deposito: "))

            for conta in vetor_contas:
                if conta.numero == numero:
                    conta_atual = conta
                    break
            
            print(f"Conta selecionada: {conta_atual.numero}")
            valor = float(input("Digite o valor a ser depositado: "))
            transacao = Deposito(valor)
                
            #Salva a transacao registrada na variavel transacao_registrada
            transacao_registrada = cliente.realizar_transacao(conta_atual, transacao)

            #Adiciona a transacao de deposito no objeto historico da classe ContaCorrente
            conta_atual.historico.adicionar_transacao(transacao_registrada)
        else:
            print("Nenhuma conta foi encontrada no usuario com o cpf informado.")

#verifica a existencia de contas no sistema bancario
def verifica_contas(contas):
    if len(contas) > 0:
        return True
     
    return False

#verifica a existencia de clientes no sistema bancario
def verifica_clientes(clientes):
    if len(clientes) > 0:
        return True
    
    return False

def ver_extrato(clientes, contas, cpf):
    conta_alvo = None
    cliente_alvo = filtra_clientes(clientes, cpf)

    if lista_contas(clientes, cpf):
        if len(cliente_alvo.contas) > 0:
            numero = int(input("Digite o numero da conta que vc quer ver o extrato: "))

            for conta in contas:
                if conta.numero == numero:
                    conta_alvo = conta
            
            if conta_alvo == None:
                print("Numero de conta informado foi digitado de maneria errada.")
            else:
                print("--------Extrato---------")
                for log in conta_alvo.historico.transacoes:
                    print(log)

                print(f"Seu saldo atual é de R${conta_alvo.saldo: .2f}")
                print("------------------------")
        else:
            print("Nenhuma conta foi encontrada no usuario com o cpf informado...")

def criar_conta(contas, clientes, cpf):
    #Cria uma lista de clientes com o cpf informado
    cliente_verificado = filtra_clientes(clientes, cpf)
    #Verifica se existe um cliente com o cpf informado no sistema bancario
    if cliente_verificado in clientes:
        numero = rd.randint(0, 1000000)
        nova_conta = ContaCorrente.nova_conta(numero, cliente_verificado)
        
        #Adiciona conta no objeto cliente_verificado e depois no vetor contas
        cliente_verificado.adicionar_conta(nova_conta)
        contas.append(nova_conta)

        print("Conta criada com sucesso!")
    else:
        print("Nao ha nenhum cliente na sessao atual do banco com esse cpf... Por favor, crie um novo usuario")

def criar_usuario(clientes):
    nome = input("Digite seu nome: ")
    data_de_nascimento = input("Digite sua data de nascimento no formato dd/mm/aaaa: ")
    cpf = input("Digite seu cpf: ")
    logradouro = input("Digite seu logradouro: ")
    bairro = input("Digite seu bairro: ")
    cidade = input("Digite a sua cidade: ")
    estado = input("Digite a sigla do seu estado: ")

    #Formatacao dos dados
    cpf = cpf.replace(".", "").replace("-", "")
    cidade_estado = cidade + "/" + estado
    endereco = [logradouro, bairro, cidade_estado]
    endereco = " - ".join(endereco)

    dic_clientes = {}

    #Adiciona os clientes em um dicionario
    for cliente in clientes:
        dic_clientes[cliente.cpf] = cliente.nome
    
    #Verifica se ja existe um cliente com o numero de cpf informado pelo usuario
    if cpf in dic_clientes:
        print("Um usuario com o mesmo numero de cpf informado ja existe no sistema.")
    else:    
        novo_cliente = PessoaFisica(endereco, cpf, nome, data_de_nascimento)
        clientes.append(novo_cliente)

        print("Novo usuario adicionado com sucesso!")

def filtra_clientes(clientes, cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
        
    return None

def lista_contas(clientes, cpf):
    cliente_alvo = filtra_clientes(clientes, cpf)

    if cliente_alvo == None:
        print("Nao foi possivel encontrar um usuario com esse numero de cpf...")
        return False
    else:
        for conta in cliente_alvo.contas:
            print(f"Numero da conta: {conta.numero}")
            print(f"Saldo da conta: R${conta.saldo: .2f}")
        
        return True

def mudar_usuario(clientes):
    cpf = input("Digite o cpf do usuario para o qual vc deseja mudar: ")
    cliente_alvo = filtra_clientes(clientes, cpf)

    print("Usuario trocado com sucesso!")

    return cliente_alvo