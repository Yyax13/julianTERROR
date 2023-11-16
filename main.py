from misc import update
update.pip(package="yollor") 
from yollor import *
from misc import loading, update, tools, request, prints, auth
import time

def main():
    tools.clear()
    prints.banner()
    SchoolOPT = input(f"""
        {t.tagn1_yellow} {c.cyan('Colégio Nossa Senhora das Neves')} - {c.yellow('Ibaiti')}
        {t.tagn2_yellow} {c.cyan('Colégio São João Batista')} - {c.yellow('Caxias do Sul')}
        {t.tagn3_yellow} {c.cyan('Colégio Nossa Senhora Aparecida')} - {c.yellow('Prata')}

        {t.quest_yellow} {c.cyan('Selecione uma')} {c.yellow('escola')}{c.cyan(':')} """)

    if SchoolOPT == "1":
        world = [
        "Lucimara Araujo Bueno Thomaz"
        "João Pedro Garcia Santos",
        "João Miguel de Oliveira Gurpian Camargo",
        "João Pedro Serial Kulas",
        "João Vitor Ribeiro Momoli",
        "Kauan Candido Valle",
        "Laura Pereira",
        "Lívia Francisco de Oliveira",
        "Luana Beatriz Schott",
        "Luana da Silva de Andrade",
        "Luanna Machado de Souza",
        "Maria Eduarda Bernardes da Silva",
        "Mariah Luísa Galvão Roque",
        "Mateus de Carvalho Castro",
        "Murilo Antonio Fernandes de Freitas",
        "Naara Martins da Cruz",
        "Pedro Ribeiro de Melo Ferreira",
        "Rafaela Oliveira Morales",
        "Andressa Keuren da Silva Anhaia",
        "Julia Y. Bueno",
        "Maria Dolores",
        "Ana Julia de Paula",
        "Ana Julia Fróes dos Santos Sousa",
        "Ana Laura de Lima Marinho",
        "Ana Leticia Ravanhol Watfe",
        "Ana Maria Faria Siqueira de Oliveira",
        "Antonio Luciano Magalhães Santos",
        "Beatriz Carnasciali Gonzalez",
        "Bruno Ferreira de Lima",
        "Eduardo Henrique Elpidio Pereira",
        "Fabiana Siqueira Negri de Faria",
        "Fernanda Siqueira Negri de Faria",
        "Gabriel de Mello Louzano",
        "Gabriel Luiz Machado",
        "Gabriela de Faria Jorge",
        "Ígor Gonçalves de Freitas",
        "Isabela Mochon Lorente Silva",
        "Izadora da Silva Gines",
        "João Pedro Garcia Santos",
        "João Miguel de Oliveira Gurpian Camargo",
        "João Pedro Serial Kulas",
        "João Vitor Ribeiro Momoli",
        "Kauan Candido Valle",
        "Laura Pereira",
        "Lívia Francisco de Oliveira",
        "Luana Beatriz Schott",
        "Luana da Silva de Andrade",
        "Luanna Machado de Souza",
        "Maria Eduarda Bernardes da Silva",
        "Mariah Luísa Galvão Roque",
        "Mateus de Carvalho Castro",
        "Murilo Antonio Fernandes de Freitas",
        "Naara Martins da Cruz",
        "Pedro Ribeiro de Melo Ferreira",
        "Rafaela Oliveira Morales"
    ]
        time.sleep(0.9)
        request.tryes(wordlist=world, school="CNSN")
    else:
        print(f"{c.red('Favor digitar um número referente a uma opção')}")
        time.sleep(1)
        print(f"{c.yellow('Reiniciando')}")
        time.sleep(1.2)
        tools.reset()

def adm():
    tools.clear()
    prints.banner()
    if input("Deseja abrir o app com GUI (s/n)? ").lower() == 's':
        tools.open("adm")
    else:
        tools.clear()
        prints.banner()
        AdmOPT = input(f"""
        {t.tagn1_yellow} {c.cyan('Criar usuario')}
        {t.tagn2_yellow} {c.cyan('Deletar usuario')}
        {t.tagn3_yellow} {c.cyan('Ver usuarios')}
        {t.tagn4_yellow} {c.cyan('Mudar uma senha')}
            
        {t.quest_yellow} {c.cyan('Selecione uma')} {c.yellow('opção')}{c.cyan(':')} """)
        if AdmOPT == '1':
            tools.clear()
            prints.banner()
            print("")
            usuario_cadastro = input(f"        {t.hashtag_yellow} {c.cyan('Insira o usuario: ')}")
            tools.clear()
            prints.banner()
            print("")
            pass_cadastro = input(f"        {t.hashtag_yellow} {c.cyan('Insira a senha: ')}")
            auth.newUser(user=usuario_cadastro, password=pass_cadastro)
        elif AdmOPT == '2':
            auth.delete(user=input(f"{t.hashtag_yellow} {c.cyan('Insira o usuario a ser deletado: ')}"))
        elif AdmOPT == '3':
            users_list = auth.get_user_data_list()
            tools.clear()
            prints.banner()
            print("")
            for usr in users_list:
                login = c.yellow(usr[0])
                password = c.yellow(usr[1])
                print(f"        {t.hashtag_yellow} {c.cyan(f'User: {login}')} | {c.cyan(f'Password: {password}')}")
                time.sleep(0.2)
            print("")
        elif AdmOPT == '4':
            tools.clear()
            prints.banner()
            print("")
            usuario2change = input(f"        {t.hashtag_yellow} {c.cyan('Insira o usuario: ')}")
            tools.clear()
            prints.banner()
            print("")
            passChanged = input(f"        {t.hashtag_yellow} {c.cyan('Insira a nova senha: ')}")
            auth.change_password(user=usuario2change, new_password=passChanged)
        else:
            print(c.yellow("Erro, selecione uma opção valida. reiniciando"))
            time.sleep(1.5)
            tools.reset()
if __name__ == "__main__":
    auth.create()
    tools.clear()
    prints.banner()
    print("")
    usuario = input(f"""    {t.quest_yellow} {c.cyan('Insira seu usuario: ')}""")
    senha = input(f"""    {t.quest_yellow} {c.cyan('Insira sua senha: ')}""")
    autenticar = auth.check(usuario, senha)
    if autenticar == "Yes":
        main()
    elif autenticar == "No":
        print(c.yellow("CREDENCIAIS INVALIDAS"))
        time.sleep(2)
        tools.sair()
    elif autenticar == "ADM":
        adm()
    else:
        print(c.yellow('ERRO DURANTE AUTH. REINICIANDO'))
        time.sleep(2)
        tools.reset()
