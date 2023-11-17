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
    elif SchoolOPT == "2":
        word = [
    'Agatha Valcarenghi Concatto',
    'Alexandre Severino Dalpupo Filho',
    'Alice Fabro Borges',
    'Alice Pedrotti Montes de Oca',
    'Alice Schwingel Carlin',
    'Alice Alano Martins',
    'Alice Bonatto Rech',
    'Alice dos santos Boschetti',
    'Alice Kajururá',
    'Alice Maria Da Luz Garcia',
    'Alice Marini Martins',
    'Alice Oliva Steffens',
    'Alice Pissaia Casarotto',
    'Alice Soares Mondadori',
    'Alice Thomé Adamski',
    'Aline Sonego Gil',
    'Álvaro Guerrero do Nascimento',
    'Amanda Anezi',
    'Amanda Dal Paz Gauer',
    'Amanda de Abreu Bett',
    'Amanda Pianegonda Frassini',
    'Amanda Vitoria Gheno Rech',
    'Amanda Camara Eilert',
    'Amanda Vyctoria Zulian',
    'Ana Carolina da Silva Hoffmann',
    'Ana Carolina de Brito Polidoro',
    'Ana Carolina Koch',
    'Ana Carolina Krewer dos Santos',
    'Ana Carolina Porto Castro',
    'Ana Clara dos Santos da Cruz',
    'Ana Clara Fett',
    'Ana Julia Facchin Layser',
    'Ana Julia Pinto de Oliveira',
    'Ana Laura Facchin Layser',
    'Ana Laura Giachini',
    'Ana Liz Fabricio Pontoni',
    'Ana Carolina Carvalho Franco',
    'Ana Julia dos Santos Pigatto',
    'Ana Laura Goncalves Spiller',
    'Ana Luiza Menegat',
    'Andre Luis Santiago de Vasconcellos',
    'Angelina Bonatto Rech',
    'Angelo Corlatti Daboit',
    'Angelo Vicente Mattana',
    'Anne Larrat dos Santos Bertazzo',
    'Antonella Sierra de Farias',
    'Antonia Alessi Borella',
    'Antonia Luiza Sassi Lunkes',
    'Antônia Oliveira Gregio',
    'Antonietta Martins Betiol',
    'Antonio Bresolin Dal Bo',
    'Antonio Fantinel Chimello',
    'Antonio Provenci Becker',
    'Antony Pietro Pellin',
    'Arthur Adami Gaio',
    'Arthur Casagrande Adami',
    'Arthur Echer',
    'Arthur Giordano Laux',
    'Arthur Guilherme Pereira',
    'Arthur Santos',
    'Arthur Simionato de Oliveira',
    'Arthur Simonetto Maggi',
    'Arthur Tomazzoni',
    'Arthur Bellei Borges',
    'Arthur Borelli Ferreira',
    'Arthur Carpena Bellini',
    'Arthur Felipe Brum',
    'Arthur Gabriel Marques Lisboa',
    'Arthur Lazzaretti Rech',
    'Arthur Provensi Pistore',
    'Arthur Stecanela Carnino',
    'Arthur Swaisser Triches',
    'Artur Quadri Gettert',
    'Artur Casagrande Menegotto',
    'Augusto Bisinella Giaretta',
    'Augusto Corlatti Daboit',
    'Augusto Dall Agnol Oldra',
    'Augusto Sugari Reis',
    'Augusto Barbosa Antonello',
    'Augusto Brandão da Silva',
    'Augusto Fermiano de Oliveira',
    'Augusto Gavazzoni',
    'Augusto Lenz Gunsch',
    'Augusto Martini Rodolfo',
    'Augusto Trentin Halmann',
    'Augusto Vargas Bavaresco',
    'Aurora Oliva Steffens',
    'Aylon Antonio Pedron de Jesus',
    'Beatriz Toigo',
    'Benhur Garcia Pereira',
    'Benicio Dornelles Moscon',
    'Benjamin Colvara Carvalho',
    'Bernardo Carvalho Mezzomo',
    'Bernardo Gajko da Silva',
    'Bernardo Borges Pinto',
    'Bernardo Dalla Santa Silveira',
    'Bernardo dos Reis',
    'Bernardo Fernandes',
    'Bernardo Fortes Ballardin da Luz',
    'Bernardo Kreusch Bordin',
    'Bernardo Scopel Zuccolotto',
    'Bernardo Segala Lemos',
    'Bernardo Zaffonato Poloni',
    'Bianca Biondo da Luz',
    'Bianca Goulart Pletsch',
    'Bibiana Bisinella Giaretta',
    'Bruna Lima Pagnon',
    'Bruna Retore Frighetto',
    'Bruna Stuani Gelain',
    'Bruna Vens de Oliveira',
    'Bruno Meneghel Mendes',
    'Bruno Weber',
    'Caetano Caldart Andretta',
    'Caetano Cassanta Boschetti',
    'Caetano Debiasi',
    'Caetano Anezi',
    'Caio Provenci Becker',
    'Camila Cardoso',
    'Camila Zangalli',
    'Camille Munaretto',
    'Carla Zucco Nadin',
    'Carlos Eduardo Cardoso',
    'Carolina Bisinella Giaretta',
    'Carolina da Silva Zolet',
    'Carolina Antunes Menna Barreto',
    'Carolina da Costa Sobrero',
    'Carolina Petrin Welcomme',
    'Caroline Andreazza',
    'Caroline Triches Feijo',
    'Cassia Petrin Cardoso',
    'Cassio Henrique Pinto',
    'Cassio Kuse Miorelli',
    'Cassio Libino Monteiro',
    'Catarina Priori Omizzol',
    'Caua Moojen Heckendorf',
    'Cecilia Bearzi Boeno',
    'Cecilia Carraro Serafim',
    'Cecilia DAgnoluzzo Moretti',
    'Cecilia Jaroslav de Matos',
    'Cecilia Raphaelle Borges Teixeira',
    'Chiara Scopel Venturin',
    'Cibele Ferreira do Amaral',
    'Cibeli Borges Bresolin',
    'Clara Ceolin',
    'Claudiomir da SIlva Brum Junior',
    'Coordenação Manhã - SJB',
    'Cristiny Cevero Parige',
    'Daniela Carla Tomazzoni',
    'Daniela Won Miller Garbin',
    'Daniela Muceneeki Silveira',
    'Daniele Borges Bresolin',
    'Daniellen Melo da Silva',
    'Davi Miranda Corte',
    'Davi Terra Silva Dutra',
    'Davi Andreis dos Santos',
    'Davi Dutra Pereira',
    'Davi Gabriel Salgueiro dos Santos',
    'Davi Lucas Reolon',
    'Davi Martini Rocha',
    'Davi Miguel da Rosa Goncalves',
    'Davi Puton da Rosa',
    'Debora de Araujo Lesina',
    'Débora Kurmann Mota',
    'Deivid Souza Palhano',
    'Diana Gayeski Rosa',
    'Diego Grassi de Oliveira',
    'Edis Rafael Magnus Poles',
    'Eduan Heitor Wan Dall Constancio',
    'Eduarda de Abreu Bett',
    'Eduarda Feil Barp',
    'Eduarda Guizzo Formolo',
    'Eduarda Pagano Josende',
    'Eduarda de Oliveira',
    'Eduarda Oliveira Gregio',
    'Eduarda Seferin Scartazzini',
    'Eduardo Mendes Bolzan',
    'Eduardo Mussatto Berton',
    'Eduardo Rodolfo Tomazzoni',
    'Eduardo Santiago Bearzi',
    'Eduardo Zatti Lima',
    'Eduardo Antonio Pires Kuiava',
    'Eduardo Brisolara Machado',
    'Eduardo de Campos Lorenzi',
    'Eduardo Felipe Renosto',
    'Eduardo Marchioro de Vargas',
    'Eduardo Segala Macedo',
    'Eduardo Silvestri',
    'Eduardo Zanini Scherer',
    'Elisa Stapasolla',
    'Eloá Lazzari',
    'Emanuela Ferreira de Almeida',
    'Emanuele Susin Vieira',
    'Emily Ecco Gebert',
    'Emily Zotti Lutz',
    'Enzo Curvelo Kalinowski',
    'Julian Tessaro Lopes'
]

        time.sleep(0.9)
        request.tryes(wordlist=word, school="CSJB")
    elif SchoolOPT == "3":
        word = [
    'Alice Almeida Vilela',
    'Alice Bataglioni Tannus',
    'Alice Guimarães Morisugi',
    'Alice Marcelli Santos Vilela',
    'Alicia Macedo Santos',
    'Aline Goncalves de Souza',
    'Ana Carollyna Fernandes Correia',
    'Ana Eduarda Martins Ferreira',
    'Ana Flavia Oliveira Vilela',
    'Ana Helena Franco Mendes',
    'Ana Julia Lopes Correa',
    'Ana Laura Nunes Costa de Oliveira',
    'Ana Laura Nunes Franco',
    'Ana Leticia Naves Junqueira',
    'Ana Luiza Vieira de Mesquita',
    'Antonella Otoni Franco',
    'Antonella Vilela Feliciano',
    'Arthur Alves Mamede',
    'Arthur Fernandes Biazotto',
    'Arthur Vieira Souza',
    'Artur Martins Pereira',
    'Augusto Costa Mamede',
    'Augusto Krys Silva',
    'Bella Marques Vieira Rodrigues Da Cunha',
    'Benício Menegaz Silveira',
    'Bernardo Assuncao Franco Vilela',
    'Bruna Assuncao Junqueira de Souza',
    'Bruna Vilela Silva',
    'Calebe Pimenta Almeida Faria',
    'Camila Agrelli Vilela',
    'Carlos Eduardo Silva Vieira Terra',
    'Carolina Vilela Freitas',
    'Cauã Battisti Orsolin',
    'Daniel Flavio Oliveira Laurindo',
    'Davi Carneiro Gomes',
    'Davi de Camargos Riposati Gonçalves',
    'Davi Franco Ribeiro',
    'Davi Morais Palumino',
    'Davi Oliveira Castro Franco',
    'Davi Orsolin Vilela',
    'Davi Resende Macedo',
    'Davi Souto Alves',
    'Davi Vieira dos Reis',
    'Eduardo Vilela Freitas',
    'Eduardo Jorge Oliveira Costa',
    'Elisa Padua Gonçalves',
    'Eloa Silva Mendes',
    'Emanuel Macedo de Campos',
    'Enzo Gabriel Gouveia Almeida Fagundes',
    'Enzo Terra Junqueira',
    'Fabio Orsolin Neto',
    'Florença Rezende Junqueira',
    'Gabriel Arantes de Oliveira',
    'Gabriel Morais Palumino',
    'Gabriel Novais Lopes',
    'Gabriel Ribeiro Franco Cunha',
    'Gabriel Vilela Bortolotto',
    'Gabriela Agostinho Junqueira',
    'Gabriella Silva Salvino',
    'Gabrielly Aparecida Silva Teodoro',
    'Gabrielly Junqueira Moreira',
    'Gabryell Henrique Mendes Santos',
    'Geovana Teodoro Souza',
    'Geovana Vilela Macedo',
    'Geovanna Silva Salvino',
    'Gilmar Henrique Costa Fernandes',
    'Giovana Fernandes Souza Vilela',
    'Giovana Ferreira de Andrade',
    'Gisele Novais Lima',
    'Giselle Vieira Franco',
    'Giulianna Mendes Vieira Gomes',
    'Guilherme Augusto Krys Silva',
    'Guilherme Cavalli Mamede',
    'Guilherme Costa Franco',
    'Guilherme Eduardo Freitas Vinhais',
    'Guilherme Ferreira Silva',
    'Guilherme Guimarães Rabelo',
    'Guilherme Junio Nunes de Oliveira',
    'Guilherme Oliveira Gardim Amui',
    'Guilherme vilela Rezende',
    'Gustavo Agrelli Rezende',
    'Gustavo Amaral De Moura Abreu',
    'Gustavo Rodrigues Amaro',
    'Gustavo Rodrigues De Freitas Filho',
    'Heitor Arantes Lima Pelozo',
    'Heitor Ribeiro Alves',
    'Helena Almeida Vilela',
    'Helena Aparecida Vieira Silva',
    'Helena Assunção Rezende',
    'Helena Coelho Sanches',
    'Helena Gomes Silva Proença',
    'Helena Lins Persch De Lima',
    'Helena Naves Pita',
    'Helena Pádua Souza',
    'Helena Victória Gonçalves Maia',
    'Heloisa Agostinho De Oliveira',
    'Heloisa Marcon Santos',
    'Heloíse victoria Gonçalves Maia',
    'Hinata Pereira de Souza',
    'Ícaro Oliveira Almeida',
    'Julian Tessaro Lopes'
]

        time.sleep(0.9)
        request.tryes(wordlist=word, school="ENSA")
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
            tools.clear()
            prints.banner()
            print("")
            auth.delete(user=input(f"        {t.hashtag_yellow} {c.cyan('Insira o usuario a ser deletado: ')}"))
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
