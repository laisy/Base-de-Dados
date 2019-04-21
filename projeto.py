import os.path
import os
import matplotlib.pyplot as plt

def criarGer():
    id = raw_input('Digite o ID do Gerente: \n')
    id = str('g' + id)
    try:
        with open('%s.txt' %id, 'r') as f:
            print "Esse ID ja possui uma conta!\n"
    except IOError:
        senha = raw_input('Digite a senha do Gerente: \n')
        arq = open('%s.txt' %id, 'w')
        arq.write(str(senha+'\n'))
        arq.close()
        print "Conta criada com Sucesso!\n"

def criarFunc():
    id = raw_input('Digite o ID do Funcionario: \n')
    id = str('f' + id)
    try:
        with open('%s.txt' %id, 'r') as f:
            print "Esse ID ja possui uma conta! \n"
    except IOError:
        senha = raw_input('Digite a senha do Funcionario: \n')
        arq = open('%s.txt' %id, 'w')
        arq.write(str(senha + '\n'))
        arq.close()
        print "Conta criada com Sucesso! \n"

def encerrarConta():
    id = raw_input('Digite o ID do funcionario que deseja Encerrar a conta: \n')
    try:
        with open('%s.txt' %id, 'r') as f:
            print '\n'
        os.remove('%s.txt' %id)
        print "Conta Encerrada! \n"
    except IOError:
        print 'Conta nao Encontrada! \n'

def printMenu():
    print ('1 - Criar Conta\n')
    print ('2 - Login\n')
    print ('3 - Encerrar\n')
    opcao = int(raw_input())
    return opcao

def carry1():
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)
    lista = []
    arquivo = open("vgsales.csv", "r")
    for k in arquivo.readlines():
        k = k.split(",")
        lista.append(k)

    genero = []
    media = []
    ano = int(input("Digite o ano: "))
    for k in lista:
        if k[3] == str(ano):
            genero.append(k[4])
            media.append(float(k[10][0:(len(k[10]))-1]))

        fig = plt.figure()
        ax1 = plt.subplot2grid((1,1), (0,0))

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.bar(genero, media)
    plt.xlabel("Genero")
    plt.ylabel("Media Global")
    plt.title("Media x Genero, ano %d" %ano)
    plt.show()

def carry2():
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    lista = []
    arquivo = open("vgsales.csv", "r")
    for k in arquivo.readlines():
        k = k.split(",")
        lista.append(k)

    genero = input("digite o genero")
    ano = input("digite o ano")
    empresas = []
    publicacoes = []

    for k in lista:
        if k[3] == str(ano) and k[4] == genero:
            flag = True
            for i in empresas:
                if i[0] == k[5]:
                    flag = False

            if flag:
                empresas.append([k[5], 1])
            else:
                for i in empresas:
                    if (i[0] == k[5]):
                        i[1] += 1

    empresas.sort(key = lambda k:k[1], reverse = True)

    publicacoes = [empresas[k][1] for k in range(10)]
    empresa = [empresas[k][0] for k in range(10)]
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))

    print(publicacoes)
    print(empresa)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.barh(empresa, publicacoes)
    plt.xlabel("Publicacoes")
    plt.ylabel("Empresas")
    plt.title("Empresas x Publicacoes, ano %d, genero %s" %(int(ano), genero))
    plt.show()

def carry3():
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    lista = []
    arquivo = open("vgsales.csv", "r")
    for k in arquivo.readlines():
        k = k.split(",")
        lista.append(k)
    genero = input()
    locais = [["NA", 0], ["EU", 0], ["JP", 0], ["Outros", 0], ["Global", 0]]
    media = []
    count = 0

    for k in lista:
        if k[4] == genero:
            locais[0][1] += float(k[6])
            locais[1][1] += float(k[7])
            locais[2][1] += float(k[8])
            locais[3][1] += float(k[9])
            locais[4][1] += float(k[10][0:len(k[10])])
            count += 1

    for l in locais:
        l[1] = l[1]/count

    locais.sort(key = lambda k:k[1], reverse = True)
    media = [locais[k][1] for k in range(len(locais))]
    loc = [locais[k][0] for k in range(len(locais))]
    print(media)
    print(loc)
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    cores = ['b', 'r', 'm', 'k', 'c']
    plt.pie(media, labels = loc, colors= cores, shadow= True, autopct= "%1.1f%%")
    plt.title("Locais x Media, genero %s" %(genero))
    plt.show()

def carry4():
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    lista = []
    arquivo = open("vgsales.csv", "r")
    arquivo.readline()
    for k in arquivo.readlines():
        k = k.split(",")
        lista.append(k)

        vendas = []
        ano1 = input("digite o ano1 ")
        ano2 = input("digite o ano2 ")
        genero = input("digite o genero ")

        for k in lista:
            if(k[3] <= ano2 and k[3] >= ano1 and k[4] == genero):
                desconhecido = True
                for v in vendas:
                    if k[3] == v[1]:
                        desconhecido = False
                        v[0] += float(k[10][0:len(k[10])-1])
                        v[2] += 1
                        break

                if desconhecido:
                    vendas.append([float(k[10][0:len(k[10])-1]), int(k[3]), 1])

    for v in vendas:
        v[0] = float(v[0])/v[2]

    vendas.sort(key = lambda k:k[1])
    media = [vendas[k][0] for k in range(0, len(vendas))]
    ano = [vendas[k][1] for k in range(len(vendas))]

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.plot(ano, media)
    plt.xlabel("Ano")
    plt.ylabel("Media")
    plt.title("Media x Ano, Genero %s, intervalo %d a %d" %(genero, int(ano1), int(ano2)))
    plt.show()

def carry5():
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    lista = []
    arquivo = open("vgsales.csv", "r")
    arquivo.readline()
    for k in arquivo.readlines():
        k = k.split(",")
        lista.append(k)

    vendas = []
    generos = []
    ano1 = (input("Digite o ano 1 \n"))
    ano2 = (input("Digite o ano 2 \n"))
    anos = [[str(k), []] for k in range(int(ano1), (int(ano2)+1))]
    for k in lista:
        for ano in anos:
            if(k[3] == ano[0]):
                tem = False
                for g in ano[1]:
                    if k[4] == g[0]:
                        tem = True
                        g[1] += 1
                        break
                if tem == False:
                    ano[1].append([k[4], 1])

    anos.sort(key = lambda k:k[0][0])
    generos = [anos[0][1][k][0] for k in range(0, len(anos[0][1]))]
    ano = [int(anos[k][0]) for k in range(len(anos))]
    valores = [int(anos[0][1][k][1]) for k in range(0, len(anos[0][1]))]

    action = []
    roleplay = []
    for year in anos:
        for genero in year[1]:
            if genero[0] == 'Action':
                action.append(genero[1])
            elif genero[0] == 'Role-Playing':
                roleplay.append(genero[1])

            fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    print(ano)
    print(action)

    ax1.plot(ano, action)
    ax1.plot(ano, roleplay)
    plt.xlabel("Ano")
    plt.ylabel("genero")
    plt.show()

def subGer():
    print ('\n')
    print ('1 - Demitir um Funcionario\n')
    print ('-------------PESQUISAS------------------\n')
    print ('2 - Media global de vendas por genero de jogos que foram lancados em um determinado ano\n')
    print ('3 - Quais as 10 empresas que mais publicaram em um determinado ano, usando um determinado genero\n')
    print ('4 - Media de vendas de acordo com um determinado genero dos jogos vendidos em NA, EU, JP, Outros e global\n')
    print ('5 - Media das Vendas globais por ano, baseadas em um determinado intervalo de anos e um genero\n')
    print ('6 - Quantidade de jogos de acordo com os X maiores genero num intervalo de anos\n')
    print ('7 - Relacao Top X de jogos, vendas NA e vendas EU\n')
    print ('8 - Top X empresas que menos ou mais produziram jogos por generos\n')
    print ('9 - Retornar Menu Principal\n')
    print ('10 - Encerrar\n')
    op2 = int(raw_input())
    while(op2 != 10):
        if op2 == 1:
            encerrarConta()
        if op2 == 2:
            carry1()
        if op2 == 3:
            carry2()
        if op2 == 4:
            carry3()
        if op2 == 5:
            carry4()
        if op2 == 6:
            carry5()
        if op2 == 7:
            print 7
        if op2 == 8:
            print 8
        if op2 == 9:
            return
        op2 = int(raw_input('Digite uma opcao do Menu: '))
    print ('Volte Sempre')
    exit(0)

def subFunc():
    print ('\n')
    print ('---------------PESQUISAS----------------\n')
    print ('1 - Media global de vendas por genero de jogos que foram lancados em um determinado ano\n')
    print ('2 - Quais as 10 empresas que mais publicaram em um determinado ano, usando um determinado genero\n')
    print ('3 - Media das Vendas globais por ano, baseadas em um determinado intervalo de anos e um genero\n')
    print ('4 - Relacao Top X de jogos, vendas NA e vendas EU\n')
    print ('5 - Retornar Menu Principal\n')
    print ('6 - Encerrar\n')
    op2 = int(raw_input())
    while(op2 != 6):
        if op2 == 1:
            carry1()
        if op2 == 2:
            carry2()
        if op2 == 3:
            carry4()
        if op2 == 4:
            print 4
        if op2 == 5:
            return
        op2 = int(raw_input('Digite uma opcao do Menu: '))
    print ('Volte Sempre')
    exit(0)

def menuCriar():
    print '1 - Gerente\n'
    print '2 - Funcionario\n'
    print '3 - Retornar Menu Principal\n'
    print '4 - Sair\n'
    esc = int(raw_input())
    while(esc != 4):
        if esc == 1:
            criarGer()
        if esc == 2:
            criarFunc()
        if esc == 3:
            return
    return esc

print ('Bem Vindo \n')
op = printMenu()
while (op != 3):
    if op == 1:
        menuCriar()
    if op == 2:
        id = raw_input('Digite o ID do funcionario: \n')
        senha = raw_input('Digite a senha: \n')
        if id[0] == 'g':
            try:
                with open('%s.txt' %id, 'r') as f:
                    senha1 = f.readline()
                    print 'senha1', senha1
                    if senha == senha1:
                        print 'senha', senha
                        subGer()
                    else:
                        print 'Senha Incorreta!'
            except IOError:
                print "Esse ID ainda nao esta Cadastrado! \n"
        if id[0] == 'f':
            try:
                with open('%s.txt' %id, 'r') as f:
                    senha2 = f.readline()
                    if senha == senha2:
                        subFunc()
                    else:
                        print 'Senha Incorreta!'
            except IOError:
                print "Esse ID ainda nao esta Cadastrado! \n"
        else:
            print 'Funcionario Inesistente!\n'

    op = printMenu()

print ('Volte Sempre')
