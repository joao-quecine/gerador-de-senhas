
from ast import Try
from random import choice
from colorama import Fore
from PySimpleGUI import PySimpleGUI as sg
senha=[]

#layout
sg.theme('Black')
layout=[
    [sg.Text('digite o numero de caracteres sua senha deve ter'), sg.Input(key='caracteres', size=(2,0))],
    [sg.Checkbox('senha forte',key='forte')],
    [sg.Text('sua senha: ', key='xx')],
    [sg.Button('gerar')],

]

#janela
janela=sg.Window('gerador de senha',layout)
while True:
    eventos, valores= janela.read()
    if eventos == sg.WIN_CLOSED:
        break

    if eventos == 'gerar':
        try:
            for i in range(int(valores['caracteres'])):
             senha.append(choice('abcdefjhilmnopqrstuvwxyv1234567890'))
            senha=''.join(senha)
            janela['xx'].update(f'sua senha: {senha}')
            senha=[]

        except ValueError:
            janela['xx'].update('insira um valor numerico entre 0 a 99')

            
            
    
       
         
    


         



