import util

def main():
    clientes = []
    contas = []
    usuario_atual = None

    print(
        '''
-----Bem vindo ao Banco Dio!--------
[s] = Saque
[d] = Deposito
[e] = Extrato
[u] = Criar novo usuario
[c] = Criar nova conta
[mu] = Mudar de usuario
[q] = Sair
------------------------------------
        '''
    )
    
    print("** Vc nao esta logado como nenhum usuario. **")
    operacao = input("Digite que operacao vc deseja realizar: ")
    operacao = operacao.casefold()

    while operacao != "q":
        match operacao:
            case "s":
                util.realizar_saque(clientes, usuario_atual)
            case "d":
                util.realizar_deposito(clientes, usuario_atual)
            case "e":
                cpf_inicial = input("Por favor, insira seu cpf: ")
                cpf_inicial = cpf_inicial.replace(".", "").replace("-", "")
                util.ver_extrato(clientes, contas, cpf_inicial)
            case "u":
                util.criar_usuario(clientes)
            case "c":
                cpf_inicial = input("Por favor, insira seu cpf: ")
                cpf_inicial = cpf_inicial.replace(".", "").replace("-", "")
                util.criar_conta(contas, clientes, cpf_inicial)
            case "mu":
                usuario_atual = util.mudar_usuario(clientes)
            case "q":
                break
            case _:
                print("Operacao invalida, tente novamente.")
        
        print(
        '''
-----Bem vindo ao Banco Dio!--------
[s] = Saque
[d] = Deposito
[e] = Extrato
[u] = Criar novo usuario
[c] = Criar nova conta
[mu] = Mudar de usuario
[q] = Sair
------------------------------------
        '''
    )
             
        if usuario_atual == None:
            print("** Vc nao esta logado como nenhum usuario. **")
        else:
            print(f"** Vc esta acessando o sistema como o usuario: {usuario_atual.nome} **")

        operacao = input("Digite que operacao vc deseja realizar: ")
        operacao = operacao.casefold()

if __name__ == "__main__":
    main()