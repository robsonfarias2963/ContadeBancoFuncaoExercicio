import textwrap

def menu():
    print(textwrap.dedent("""
        -------------MENU---------
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Nova conta
        [lc] Listar contas
        [nu] Novo usuário
        [q] Sair
    """))
    return input("Escolha uma opção: ")


def depositar(saldo,valor,extrato):
    if valor > 0 :
        saldo+=valor
        extrato+=f"Depósito:\tR${valor:.2f}\n"
        print("\nDepósito realizado com sucesso.")
    else :
        print("\nOperação falhou, o valor informado é inválido.")
    return saldo,extrato


def sacar(saldo,valor,extrato,numero_saques,limite_para_saque,limite):
    if numero_saques >= limite_para_saque :
        print(f"Sem sucesso na operação, número máximo de saques ({limite_para_saque}) já realizado.")
        return saldo,extrato,numero_saques
    if valor > saldo :
        print("Saldo insuficiente. Saldo disponível: R$",saldo)
    elif valor > limite :
        print("Valor excede o limite permitido de R$",limite)
    elif valor > 0 :
        saldo-=valor
        extrato+=f"Saque:\tR${valor:.2f}\n"
        numero_saques+=1
        print("Saque realizado com sucesso.")
    else :
        print("Valor informado não é válido.")
    return saldo,extrato,numero_saques


def mostrar_extrato(extrato,saldo):
    print("Extrato dos movimentos:")
    print(extrato)
    print(f'Saldo atual: R${saldo:.2f}')


def novo_usuario(usuarios):
    cpf=input("Informe um CPF válido: ")
    if any(usuario['cpf']==cpf for usuario in usuarios):
        print("Já existe um usuário com esse CPF.")
        return
    nome=input("Informe um nome de usuário: ")
    data_nascimento=input("Informe uma data de nascimento: ")
    endereco=input("Informe um endereço: ")

    novo_usuario={"cpf" : cpf,"nome" : nome,"data_nascimento" : data_nascimento,"endereco" : endereco}
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")


def listar_contas(contas):
    for conta in contas:
        print(
            f"Agência: {conta['agencia']}, Número da conta: {conta['numero_conta']}, Usuários: {len(conta['usuarios'])}")


def nova_conta(agencia,contas,usuarios):
    if not usuarios:
        print("Não há usuários cadastrados para vincular a uma nova conta.")
        return
    numero_conta=len(contas)+1
    contas.append({"agencia" : agencia,"numero_conta" : numero_conta,"usuarios" : usuarios})
    print("Conta criada com sucesso!")


def main():
    saldo=0
    extrato=''
    numero_saques=0
    limite_para_saque=3
    limite=500
    usuarios=[]
    contas=[]
    agencia='0001'

    while True:
        opcao=menu()
        if opcao=='d':
            valor=float(input("Digite um valor para depósito: "))
            saldo,extrato=depositar(saldo,valor,extrato)
        elif opcao=='s':
            valor=float(input("Informe o valor para saque: "))
            saldo,extrato,numero_saques=sacar(saldo,valor,extrato,numero_saques,limite_para_saque,limite)
        elif opcao=='e':
            mostrar_extrato(extrato,saldo)
        elif opcao=='nu':
            novo_usuario(usuarios)
        elif opcao=='nc':
            nova_conta(agencia,contas,usuarios)
        elif opcao=='lc':
            listar_contas(contas)
        elif opcao=='q':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__=="__main__":
    main()
