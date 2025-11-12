from leitura import Leitura
from sensor import Sensor
from usuario import Bolsista, Analista

sensores = []
leituras = []
usuarios = []


def cadastrar_usuario():
    print("\nMENU - CADASTRO\n")
    nome = input("Nome: ")
    login = input("Login: ")
    senha = input("Senha: ")

    print("\nMENU - TIPO DE USUARIO\n")
    print("1 - Bolsista")
    print("2 - Analista")
    tipo = input("\nTipo de cadastro: ")

    for usuario in usuarios:
        if usuario.get_login() == login:
            print("\nLogin ja utilizado, tente novamente\n")
            return

    if tipo == "1":
        usuario = Bolsista(nome, login, senha)
    elif tipo == "2":
        usuario = Analista(nome, login, senha)
    else:
        print("\ntente novamente\n")
        return

    usuarios.append(usuario)
    print(f"\nCadastrado com sucesso\n")


def fazer_login():
    print("\nMENU - LOGIN\n")
    login = input("Login: ")
    senha = input("Senha: ")

    for usuario in usuarios:
        if usuario.get_login() == login and usuario.get_senha() == senha:
            print(f"\nBem vindo: {usuario.nome}")
            return usuario

    print("\nLogin ou senha incorreta\n")
    return False

def cadastrar_sensor():
    print("\nMENU - SENSOR")
    print("\nSensores disponíveis para cadastro:\n")
    print("1 - Temperatura do solo")
    print("2 - Temperatura do ar")
    print("3 - Umidade do ar")
    print("4 - Umidade do solo")
    print("5 - Salinidade")
    print("6 - Radiação solar")

    opcao = input("\nEscolha uma opcao: ")

    id_novo = len(sensores) + 1

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

    localizacao = input("Local do sensor: ")

    sensor_novo = Sensor(id_novo, tipo, unidade, localizacao)
    sensores.append(sensor_novo)
    print("\nSensor cadastrado: \n")
    print(sensor_novo)


def coletar_dados():
    if len(sensores) == 0:
        print("\nNenhum sensor cadastrado para coleta de dados")
        return

    for sensor in sensores:
        valor = sensor.gerar_leitura()
        cadastrar_leitura = Leitura(valor, sensor)
        leituras.append(cadastrar_leitura)

    print(f"\nTotal de dados coletados: {len(sensores)}")


def mostrar_leituras():
    if len(sensores) == 0:
        print("\nNenhum sensor cadastrado para mostrar leituras")
        return

    if len(leituras) == 0:
        print("\nNenhum dado coletado para mostrar leituras")
        return

    for leitura in leituras:
        print(leitura)

    print(f"\nTotal de leituras: {len(leituras)}")


def filtrar_leitura():
    if len(sensores) == 0:
        print("\nNenhum sensor cadastrado para filtrar leitura")
        return

    if len(leituras) == 0:
        print("\nNenhum dado coletado para filtrar leituras")
        return

    tipos = []

    for sensor in sensores:
        if sensor.tipo not in tipos:
            tipos.append(sensor.tipo)

    print("\nFiltrar leituras por tipo do sensor:\n")

    numero = 1
    for tipo in tipos:
        print(f"{numero}. {tipo}")
        numero = numero + 1

    escolha = int(input("\nEscolha a leitura que deseja filtrar: "))
    tipo_escolhido = tipos[escolha - 1]

    print(f"\nLEITURAS: {tipo_escolhido}\n")
    total = 0
    for leitura in leituras:
        if leitura.tipo == tipo_escolhido:
            print(leitura)
            total = total + 1

    print(f"\nTotal: {total} leituras\n")

def pedecoco():
    print("\nMONITORAMENTO IoT - PÉ DE COCO\n")

def menu_principal(usuario_logado):
    op = 99
    while op != 0:
        print("\nMENU - IoT\n")

        if usuario_logado.cadastrar_sensor():
            print("1. Cadastrar sensor")
        print("2. Coletar dados")
        print("3. Todas leituras")
        print("4. Filtrar leituras por sensor")
        print("0. Sair")

        op = int(input("\nEscolha uma opção: "))

        if op == 1:
            if usuario_logado.cadastrar_sensor():
                cadastrar_sensor()
            else:
                print("\nVocê não tem permissão para cadastrar sensores\n")

        elif op == 2:
            coletar_dados()
        elif op == 3:
            mostrar_leituras()
        elif op == 4:
            filtrar_leitura()
        elif op == 0:
            print("\nMONITORAMENTO IoT - PÉ DE COCO\n")
        else:
            print("\nTente novamente")

def menu():
    op = 99
    while op != 0:
        print("1 - Cadastro")
        print("2 - Login")
        print("0 - Sair")

        op = int(input("\nEscolha uma opção: "))

        if op == 1:
            cadastrar_usuario()
        elif op == 2:
            usuario_logado = fazer_login()
            if usuario_logado != False:
                menu_principal(usuario_logado)
        elif op == 0:
            print("Volte sempre para cuidar dos coco")

pedecoco()
menu()