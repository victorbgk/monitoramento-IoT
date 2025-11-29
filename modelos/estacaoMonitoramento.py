from leitura import Leitura
from sensor import Sensor
from usuario import Bolsista
from usuario import Analista
from dao import BolsistaDAO

dao = BolsistaDAO("pessoas.db")

lista_sensores = []
lista_leituras = []
lista_usuarios = []

print("\nMONITORAMENTO IoT - PÉ DE COCO\n")

def cadastrar_usuario():

    print("\nMENU - CADASTRO\n")

    nome = input("Nome: ")
    login = input("Login: ")
    senha = input("Senha: ")

    for usuario in lista_usuarios:

        if usuario.get_login() == login:

            print("\nlogin ta sendo utilizado, coloque outro\n")

            return

    print("\nMENU - TIPO DE USUARIO\n")

    print("1 - Bolsista")
    print("2 - Analista")

    opcao = input("\ntipo de cadastro: ")

    if opcao == "1":

        novo_usuario = Bolsista(nome, login, senha)

    elif opcao == "2":

        novo_usuario = Analista(nome, login, senha)

    else:

        print("\ntente novamente\n")

        return

    lista_usuarios.append(novo_usuario)

    print(f"\nCadastrado com sucesso\n")

def fazer_login():

    print("\nMENU - LOGIN\n")

    login = input("Login: ")
    senha = input("Senha: ")

    for usuario in lista_usuarios:

        if usuario.get_login() == login and usuario.get_senha() == senha:

            print(f"\nbem vindo: {usuario.nome}")

            return usuario

    print("\nlogin ou senha errada\n")

    return False

def cadastrar_sensor():

    print("\nMENU - SENSOR")

    print("\nSensores disponíveis para cadastrar:\n")

    print("1 - Temperatura do solo")
    print("2 - Temperatura do ar")
    print("3 - Umidade do ar")
    print("4 - Umidade do solo")
    print("5 - Salinidade")
    print("6 - Radiação solar")

    opcao = input("\nescolha um: ")

    id_novo_sensor = len(lista_sensores) + 1

    if opcao == "1":
        tipo = "temperatura do solo"
        unidade = "C"

    elif opcao == "2":
        tipo = "temperatura do ar"
        unidade = "C"

    elif opcao == "3":
        tipo = "umidade do ar"
        unidade = "%"

    elif opcao == "4":
        tipo = "umidade do solo"
        unidade = "%"

    elif opcao == "5":
        tipo = "salinidade"
        unidade = "dS/m"

    elif opcao == "6":
        tipo = "radiacao solar"
        unidade = "W/m2"

    else:

        return

    localizacao = input("\nlocal onde o sensor vai coletar e mostrar dados: ")

    novo_sensor = Sensor(id_novo_sensor, tipo, unidade, localizacao)

    lista_sensores.append(novo_sensor)

    print("\nnovo sensor cadastrado:\n")

    print(novo_sensor.exibir_cadastro())

def coletar_dados():

    if len(lista_sensores) == 0:

        print("\nnenhum sensor cadastrado para coleta de dados")

        return

    for dados_sensor in lista_sensores:

        valor = dados_sensor.gerar_leitura()

        nova_leitura = Leitura(valor, dados_sensor)

        lista_leituras.append(nova_leitura)

    print(f"\nTotal de dados coletados: {len(lista_sensores)}")

def mostrar_leituras():
    if len(lista_sensores) == 0:
        print("\nnenhum sensor cadastrado para mostrar leituras")

        return

    if len(lista_leituras) == 0:
        print("\nnenhum dado coletado para mostrar leituras")

        return

    for leitura in lista_leituras:

        print(leitura.exibir_leitura())

    print(f"\ntotal de leituras: {len(lista_leituras)}")


def filtrar_leitura():
    if len(lista_sensores) == 0:
        print("\nnenhum sensor cadastrado para filtrar leitura")

        return

    if len(lista_leituras) == 0:
        print("\nnenhum dado coletado para filtrar leituras")

        return

    tipos = []

    for dados_sensor in lista_sensores:

        if dados_sensor.tipo not in tipos:

            tipos.append(dados_sensor.tipo)

    print("\nfiltrar leituras por tipo do sensor:\n")

    numero = 1

    for tipo in tipos:

        print(f"{numero}. {tipo}")

        numero = numero + 1

    escolha = int(input("\nescolha a leitura que deseja filtrar: "))

    tipo_escolhido = tipos[escolha - 1]

    print(f"\nsensor filtrado: {tipo_escolhido}\n")

    total = 0

    for leitura in lista_leituras:

        if leitura.dados_sensor.tipo == tipo_escolhido:

            print(leitura.exibir_leitura())

            total = total + 1

    print(f"\nfiltragens totais: {total}\n")



    print("\nMONITORAMENTO IoT - PÉ DE COCO\n")

def menu_principal(usuario_logado):

    opcao = 99

    while opcao != 0:

        print("\nMENU - IoT\n")

        if usuario_logado.cadastrar_sensor():

            print("1. Cadastrar sensor")

        print("2. Coletar dados")
        print("3. Todas leituras")
        print("4. Filtrar leituras por sensor")
        print("0. Sair")

        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:

            if usuario_logado.cadastrar_sensor():

                cadastrar_sensor()
            else:

                print("\nvoce não tem permissão para cadastrar sensores\n")

        elif opcao == 2:
            coletar_dados()
        elif opcao == 3:
            mostrar_leituras()
        elif opcao == 4:
            filtrar_leitura()
        elif opcao == 0:
            print("\nMONITORAMENTO IoT - PÉ DE COCO\n")
        else:
            print("\nTente novamente")

def menu():
    opcao = 99
    while opcao != 0:

        print("1 - Cadastro")
        print("2 - Login")
        print("0 - Sair")

        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            usuario = fazer_login()
            if usuario != False:
                menu_principal(usuario)
        elif opcao == 0:
            print("")
        else:
            print("\nTente novamente\n")

menu()