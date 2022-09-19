
#Pesquisei muito e esse foi o maximo que consegui fazer :(   


clientes = []
endereco = []

def cadastro():
    
    while True:
        print ('[Forneça as informações do usuário!]')
        
        dados = {} #Dicionário que será passado todos os dias para a lista 'clientes'
        dados['nomeComp'] = (input('Nome: '))
        dados['senha'] = input('Senha: ')
        
        #1-e-mail
        dados['email'] = input('E-mail: ')
        lista = {i['email']: i for i in clientes} 
        while dados ['email'] in lista:
            dados ['email'] = input ('[E-mail em uso, tente novamente!] E-mail: ')
            
        #2 login
        dados['login'] = input('Login: ')
        lista = {i['login']: i for i in clientes}
        while dados ['login'] in lista:
            dados ['login'] = input ('[Login em uso, tente novamente!] Login: ') 
            
        #2 telefone
        dados['telefone'] = int(input('Telefone: '))
        lista = {i['telefone']: i for i in clientes}
        while dados ['telefone'] in lista:
            dados ['telefone'] = input ('[Telefone em uso, tente novamente!] Telefone: ') 
            
        clientes.append(dados)
        
        print('[Cadastro concluído!')


def endereco():
    
    while True:
        
        print('[Forneça um login de usuário!]')
        lista = {i['login']: i for i in clientes}
        pesq = input('Login: ')
        
        if pesq in lista:
            print('[Forneça o endereço de entrega:]')
            
            destino = {}
            destino['id'] = pesq
            destino['estado'] = input('Estado: ')
            destino['cidade'] = input('Cidade: ')
            destino['rua'] = input('Rua: ')
            destino['numero'] = input('Número: ')
            destino['cep'] = input('CEP: ')
            endereco.append(destino)
            
        else:
            print('')
            print('[Usuário não encontrado!]')
            print('')
            
        opcao = input('Deseja inserir outro endereço? (S/N): ').strip().lower()
        if(opcao == 'N'):
            menu()
            break
              
def Dados():
    
    while True:
        print('[Forneça os dados de Login]')
        
        lista = {i['login']: i for i in clientes}
        lista2 = {i['id']: i for i in endereco}
        
        pesq = input('Login: ')
        
        if pesq in lista and pesq not in lista2:
            
            print(f'Dados do cliente [{pesq.upper()}]: {lista[pesq]}')
            print('')
            print('Endereço não cadastrado') 
            print('')
            
        elif pesq in lista and pesq in lista2:
            
            print('')
            print(f'Dados do cliente [{pesq.upper()}]: {lista[pesq]}')
            print('')
            print(f'Endereço do cliente [{pesq.upper()}]:') 
            print('') 
            resultado = list(filter(lambda item: item['id'] == pesq, endereco))
            
            for i in resultado:
                print(i)
            print ('')
            
        else:
            print('')
            print('[Usuário não encontrado]')
            print('')
            menu()
            break
            
def clientes():
    
    while True:
        print('')
        print('[Usuários Cadastrados: ]')
        print('')
        
        for i in clientes: 
            
            print('Nome', i['nomeComp'], 'Login:', i['login'])
            
        print('')
        
        opcao = input('Deseja conferir os dados? (S/N): ').strip().lower()
        if (opcao == "N"):
            menu()
            break
        
     
def menu():
    
    print('************')
    print('[1] Cadastrar novo usuário')
    print('[2] Cadastrar endereço de entrega')
    print('[3] Mostrar dados cadastrados')
    print('[0] Sair')
    print('************')
    
menu()

while True:
    
    x = int(input('Escolha > [1] [2] [3] [0]:'))
    
    if x == 1:
        cadastro()
    elif x == 2:
        endereco()
    elif x == 3:
        dados()
    else:
        print('')
        print('[Logout]')
        print('')
        break
    gi