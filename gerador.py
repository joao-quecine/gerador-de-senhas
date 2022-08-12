
from random import choice
from colorama import Fore
from PySimpleGUI import PySimpleGUI as sg
senha=[]

#layout
sg.theme('Black')
layout=[
    [sg.Text('digiteo numero de caracteres sua senha deve ter'), sg.Input(key='caracteres')],
    [sg.Checkbox('senha forte',key='senha forte')],
    [sg.Text(f'{senha}', key='xx')],
    [sg.Button('gerar')],

]

#janela
janela=sg.Window('gerador de senha',layout)
while True:
    eventos, valores= janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'gerar':
        for i in range(int(valores['caracteres'])):
            senha.append(choice('abcdefjhilmnopqrstuvwxyv1234567890'))
    senha=''.join(senha)
    janela['xx'].update(f'sua senha: {senha}')
    senha=[]
    

         



