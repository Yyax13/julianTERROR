import os
from yollor import *
import time as SurubaTemporal

frame1 = '|'
frame2 = '/'
frame3 = '-'
frame4 = "\ "

def start(texto, NV):
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(NV):
        clear()
        print(f"{c.cyan(texto)} - {c.yellow(frame1)}")
        SurubaTemporal.sleep(0.3)
        clear()
        print(f"{c.cyan(texto)} - {c.yellow(frame2)}")
        SurubaTemporal.sleep(0.3)
        clear()
        print(f"{c.cyan(texto)} - {c.yellow(frame3)}")
        SurubaTemporal.sleep(0.3)
        clear()
        print(f"{c.cyan(texto)} - {c.yellow(frame4)}")
        SurubaTemporal.sleep(0.3)
        clear()
