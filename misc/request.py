import random as r
import time
import random
from yollor import *
from misc import prints
from misc import tools
from misc import loading

def tryes(target, wordlist):
    pwd = {
    'Aline Talita de Carvalho': {
        'login': 'aline.cnsn2',
        'senha': 'bvh77*'
    },
    'Ana Carla Rodrigues': {
        'login': 'anacarla.cnsn',
        'senha': 'rvq87*'
    },
    'Andressa Cristiane de Almeida': {
        'login': 'andressa.cnsn',
        'senha': 'kru66*'
    },
    'Bernadete Fatima da Silva Alves': {
        'login': 'bernadete.cnsn',
        'senha': 'owc73*'
    },
    'Darli Darli Justina Oss Emer': {
        'login': 'darli.cnsn',
        'senha': 'abl17'
    },
    'Delma Anastacia Baby Fadel dos Santos': {
        'login': 'delma.cnsn2',
        'senha': 'esr43*'
    },
    'Edina de Fatima Nunes Moreira': {
        'login': 'edina.cnsn',
        'senha': 'wja86*'
    },
    'Edineia de Jesus Viana': {
        'login': 'edineia.cnsn',
        'senha': 'zrn22*'
    },
    'Eniceia Candido de Carvalho Langner': {
        'login': 'eniceia.cnsn',
        'senha': 'qbe43*'
    },
    'Fabiana Santa Rosa': {
        'login': 'fabiana.cnsn2',
        'senha': 'mju53*'
    },
    'Gabriele Aparecida Constantino': {
        'login': 'gabriele.cnsn',
        'senha': 'byh63*'
    },
    'Gustavo Bahls Raimundo': {
        'login': 'gustavo2.cnsn',
        'senha': 'jhj53*'
    },
    'Graciane Reimao de Melo': {
        'login': 'graciane.cnsn',
        'senha': 'drs46*'
    },
    'Helen Patricia Marinho': {
        'login': 'helen.cnsn',
        'senha': 'urq36*'
    },
    'Ismael Stella Alves': {
        'login': 'ismael.cnsn',
        'senha': 'skx42*'
    },
    'Julio Wenceslau Macowski': {
        'login': 'julio.cnsn',
        'senha': 'dxe19*'
    },
    'Leila Candido de Bonfim Torres': {
        'login': 'leila.cnsn',
        'senha': 'jtm21*'
    },
    'Liliana Chamorro': {
        'login': 'liliana.cnsn',
        'senha': 'idb90*'
    },
    'Lucia Regina de Oliveira Dib': {
        'login': 'lucia.cnsn2',
        'senha': 'exh22*'
    },
    'Luciana Moreira de Souza': {
        'login': 'lucianamoreira.cnsn',
        'senha': 'xfe87*'
    },
    'Lucimara Araujo Bueno Thomaz': {
        'login': 'lucimara.cnsn2',
        'senha': 'ovi63'
    },
    'Marcia Cristina Carneiro': {
        'login': 'marcia.cnsn2',
        'senha': 'idw57*'
    },
    'Marcos Andre da Costa': {
        'login': 'marcos.cnsn',
        'senha': 'xnu63*'
    },
    'Miriam Silva Souza': {
        'login': 'miriam.cnsn',
        'senha': 'dki53'
    },
    'Polyana Maria Mendes Pinto': {
        'login': 'polyana.cnsn',
        'senha': 'cfp69*'
    },
    'Raquel Teles Klemiant': {
        'login': 'raquel.cnsn2',
        'senha': 'jsw54*'
    },
    'Sandra Francieli Godoy': {
        'login': 'sandragodoy.cnsn',
        'senha': 'dpr72*'
    },
    'Selma Maria Santana': {
        'login': 'selma.cnsn',
        'senha': 'jbx39*'
    },
    'Suelen Oliveira Dantas Costa': {
        'login': 'suellen.cnsn',
        'senha': 'ahc46*'
    },
    'Tatiane Batista Candido': {
        'login': 'tatianecandido.cnsn',
        'senha': 'vyz48*'
    },
    'Tiago Fernandes Viana': {
        'login': 'tiago.cnsn',
        'senha': 'ijq66*'
    },
    'Vanessa Frata': {
        'login': 'vanessa.cnsn',
        'senha': 'pya89*'
    },
    'Vanilda Tavares de Lima': {
        'login': 'vanilda.cnsn2',
        'senha': 'vih87'
    },
    'Vivian Cristine Ribeiro Cerqueira': {
        'login': 'vivian.cnsn',
        'senha': 'cyf43*'
    },
    'Wallacee Guerra Assunção': {
        'login': 'wallacee.cnsn',
        'senha': 'nyk14*'
    },
    'Marcia Henares Mello': {
        'login': 'marciamelo.cnsn',
        'senha': 'melo'
    },
    'Marcia Melo': {
        'login': 'marciamelo',
        'senha': 'yyax13'
    },
    'João Batista Marques': {
        'login': 'joao',
        'senha': 'jbmjr'
    },
    'Guilherme Angelino Lopes Paulino': {
        'login': 'guilhermealp.cnsn',
        'senha': 'cvp29*'
    },
    'Fabiane Moreira dos Santos Avelar': {
        'login': 'fabiane.cnsn',
        'senha': 'czn95*'
    },
    'Angélica Carla da Rosa': {
        'login': 'angelicarosa.cnsn',
        'senha': '150322'
    },
    'Andressa Keuren da Silva Anhaia': {
        'login': 'andressakeuren.cnsn',
        'senha': 'wbt66*'
    },
    'Julia Y. Bueno': {
        'login': 'julia',
        'senha': 'juliayb'
    },
    'Maria Dolores': {
        'login': 'maria.cnsn',
        'senha': 'dcj68*'
    }
}

    while True:
        tr = r.choice(wordlist)
        if tr in pwd:
            print(f"""{c.green('Encontrado super-usuario.')} {c.yellow('Iniciando dict attack em https://positivoon.com.br/#/solucao/gerenciar-usuarios')}""")
            time.sleep(2.4)
            loading.start('Procurando semi-users e privilegios', 9)
            user = random.choice(list(pwd.keys()))
            login = pwd[user]['login']
            passwd = pwd[user]['senha']
            print(f"""{c.cyan('Encontrado.')} {c.yellow('Acesse o positivo on:')}
{c.cyan(login)} {c.yellow('|')} {c.cyan(passwd)}""")  
            break
        else:
            tools.clear()
            prints.banner()
            print(c.blue(f'NonRoot - {tr}. Tentando novamente'))
            time.sleep(1.63480912)
