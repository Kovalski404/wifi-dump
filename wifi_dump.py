#/bin/bash
#Criado por Kovaslki404 

import os,time 
def banner():

    banner = '''
    ____        _____ __   _______  __
    \    \  _  /    /|  | |   __ _||  |
     \    \/ \/    / |  | |  |_    |  |
      \           /  |  | |  _ _|  |  | 
       \___/ \___/   |__| |__|     |__| DUMP

    '''
    print(banner)

def menu():
    while True:
        banner()
        print('Seja bem vindo ao Dumper_wifi\n\n')
        print('1-Coleta de wifis cadastrados\n2-Coleta de senha do wifi em texto\n3-Sair\n')
        resposta = input('escolha: ')
        if resposta == "1":
            co = input('Deseja criar o arquivo( y ou n)? ')
            if co == "y":
                os.system('netsh wlan show profile >> wifi_cadastrados.txt')
                print('Arquivo criado \'wifi_cadastrados.txt\'\n')
                cont = input("deseja continuar (y ou n)? ")
            
                if cont == "y":
                    pass
                else:
                    break
            if co == "n":
                print(os.system('netsh wlan show profile'))
                cont = input("deseja continuar (y ou n)? ")
                if cont == "y":
                    pass
                else:
                    break
                
        if resposta == "2":
            alvo = input('Digite o wifi que deseja descobrir a senha: ')
            arq = input('Deseja criar arquivo com resultado (y ou n) ?')
            
            if arq == "y": 
                os.system('netsh wlan show profiles name={} key=clear >> wifi_senhas.txt'.format(alvo))
                print('Arquivo criado \'wifi_senhas.txt\'\n')
                cont = input("deseja continuar (y ou n)? ")
            
                if cont == "y":
                    pass
                else:
                    break
            
            else:
                print(os.system('netsh wlan show profiles name={} key=clear'.format(alvo)))
                cont = input("deseja continuar (y ou n)? ")
                if cont == "y":
                    pass
                else:
                    break
        if resposta == "3":
            print("Saindo...")
            time.sleep(1)
            break

def main():
        menu()
if __name__ == "__main__":
    main()
