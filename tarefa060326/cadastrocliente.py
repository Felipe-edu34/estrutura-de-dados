cliente = {}

def cadastrar_cliente():
    nome = input("digite o nome do cliente:")
    cpf = input("digite o cpf do cliente:")
    numero = input("digite o numero do cliente:")
    cliente[cpf] = { nome, numero}

    print("cliente cadastrado com sucesso!")
    print("Nome:", nome)
    print("CPF:", cpf)
    print("Número:",numero)


cadastrar = input("deseja cadastrar um cliente? (s/n):")


while cadastrar == "s" or cadastrar == "S":
    cadastrar_cliente()
    cadastrar = input("deseja cadastrar um cliente? (s/n):")


