import os

def clear():
 os.system('cls' if os.name == 'nt' else 'clear')

def pip(package):
 clear()
 os.system(f'pip install {package} -q')
 clear()

pip("yollor")
from yollor import *
pip("openpyxl")
pip("mysqlclient")
import mysql.connector
import openpyxl
import time
pip('requests')
import requests

fullURL = input(f"{t.hashtag_blue} {c.purple('Insert the full url, or press enter to use default url: ')}")

if fullURL:
    url = f"{fullURL}"  
    dados_login = {
        'pma_username': 'yyax',
        'pma_password': 'yyax'
    }

    resposta = requests.post(url, data=dados_login)

    if resposta.status_code == 200:
        print(f"{c.green('Login bem-sucedido, iniciando busca')}")
    else:
        print(f"{c.red('Falha no login. Status code:')} ", c.red(resposta.status_code))
        print(resposta.text) 
else:
    url = f"http://192.168.5.1/phpmyadmin"  
    dados_login = {
        'pma_username': 'root',
        'pma_password': 'root'
    }

    resposta = requests.post(url, data=dados_login)

    if resposta.status_code == 200:
        print(f"{c.green('Login bem-sucedido, iniciando busca')}")
    else:
        print(f"{c.red('Falha no login. Status code:')} ", c.red(resposta.status_code))
        print(resposta.text) 

def do_excel(user, local, name):
    conn = mysql.connector.connect(
    host=f"{local}",
    user=f"{user}",
    password=f"{user}",
    database="portal"
    )


    cursor = conn.cursor()

    cursor.execute("SELECT * FROM liberacao")

    results = cursor.fetchall()

    wb = openpyxl.Workbook()

    ws = wb.active

    for row in results:
    ws.append(row)

    wb.save(f"{name}.xlsx")

    cursor.close()
    conn.close()

do_excel("yyax", "localhost", "liberacao")
do_excel("root", "192.168.5.1", "liberacao_root")
do_excel("yyax", "127.0.0.1", "liberacao1")