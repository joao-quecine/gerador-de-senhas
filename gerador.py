
from random import choice
from colorama import Fore
from PySimpleGUI import PySimpleGUI as sg
senha=[]

#layout
sg.theme('Reddid')
layout=[
    [sg.Text('digiteo numero de caracteres sua senha deve ter'), sg.Input(key='caracteres')],
    [sg.Text(f'{senha}')],
    [sg.Button('gerar')],

]

#janela
janela=sg.Window('gerador de senha',layout)
while True:
    eventos, valores= janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'gerar':
        for i in valores['caracteres']:
            for i in range(2):
                senha.append(choice('adfg'))




