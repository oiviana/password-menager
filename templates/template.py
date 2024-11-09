import sys, os

sys.path.append(os.path.abspath(os.curdir))

from model.password import Password
from views.password_views import FernetHasher

action = input('Digite 1 para salvar uma nova senha ou 2 para visualizar uma senha salva: ')

match action:
    case '1':
        if len(Password.get()) == 0:
            key, path = FernetHasher.create_key(archive=True)
            print('Chave criada com sucesso. Guarde-a com cuidado!')
            print(f'Chave: {key.decode("utf-8")}')
            if path:
                print('Chave salva no arquivo, lembre-se de remover o arquivo após o transferir de local')
                print(f'Caminho: {path}')

        else:
            key = input('Digite sua chave usada para criptografia, use sempre a mesma chave: ')

        domain = input('Domínio: ')
        password = input('Senha: ')
        fernet_user = FernetHasher(key)
        p1 = Password(domain=domain, password=fernet_user.encrypt(password).decode('utf-8'))
        p1.save()   

    case '2':
        domain = input('Domínio: ')
        key = input('Key: ')
        fernet_user = FernetHasher(key)
        data = Password.get()

        for i in data:
            if domain in i['domain']:
                password = fernet_user.decrypt(i['password'])
                
        if password:
            print(f'Sua senha: {password}')

        else:
            print('Nenhuma senha encontrada para esse domínio :(')