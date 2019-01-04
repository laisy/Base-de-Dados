import os.path
import os

def criarGer():
    id = raw_input('Digite o ID do Gerente: \n')
    id = str('g' + id)
    try:
        with open('%s.txt' %id, 'r') as f:
            print "Esse ID ja possui uma conta! \n"
    except IOError:
        senha = raw_input('Digite a senha do Gerente: \n')
        arq = open('%s.txt' %id, 'w')
        arq.write(str(senha +'\n'))
        arq.close()
        print "Conta criada com Sucesso! \n"

def criarFunc():
    id = raw_input('Digite o ID do Funcionario: \n')
    id = str('f' + id)
    try:
        with open('%s.txt' %id, 'r') as f:
            print "Esse ID ja possui uma conta! \n"
    except IOError:
        senha = raw_input('Digite a senha do Funcionario: \n')
        arq = open('%s.txt' %id, 'w')
        arq.write(str(senha +'\n'))
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

def escreverValor(valor):
    arq = open('%s.txt' %id, 'a')
    arq.write(str(valor))
    arq.close()

def printMenu():
    print ('1 - Criar Conta\n')
    print ('2 - Login\n')
    print ('3 - Encerrar\n')
    opcao = int(raw_input())
    return opcao

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
            print 2
        if op2 == 3:
            print 3
        if op2 == 4:
            print 4
        if op2 == 5:
            print 5
        if op2 == 6:
            print 6
        if op2 == 7:
            print 7

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
            print 1
        if op2 == 2:
            print 2
        if op2 == 3:
            print 3
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
        if id[0] == 'g':
            try:
                with open('%s.txt' %id, 'r') as f:
                    subGer()
            except IOError:
                print "Esse ID ainda nao esta Cadastrado! \n"
        if id[0] == 'f':
            try:
                with open('%s.txt' %id, 'r') as f:
                    subFunc()
            except IOError:
                print "Esse ID ainda nao esta Cadastrado! \n"

    op = printMenu()

print ('Volte Sempre')
