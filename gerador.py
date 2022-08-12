
from ast import Try
from msilib.schema import ComboBox
from random import choice
from PySimpleGUI import PySimpleGUI as sg
senha=[]

#layout
sg.theme('Black')
layout=[
    [sg.Text('digite o numero de caracteres sua senha deve ter'), sg.Input(key='caracteres', size=(2,0))],
    [sg.Check('letras maiusculas', key='lm'),sg.Check('numeros', key='nm'), sg.Check('simbulos', key='sm')],
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
            if valores['lm']==True and valores['nm']==True and valores['sm']==True:
                for i in range(int(valores['caracteres'])):
                    senha.append(choice('abcdefjhilmnopqrstuvwxyvz1234567890ABCDEFGHIJKLMNWXYZOPQRSTUV@#*&%$!_-{.}'))
              
            elif valores['lm']==True and valores['nm']==False and valores['sm']==False:
                for i in range(int(valores['caracteres'])):
                    senha.append(choice('abcdefghijwxyvklmnopqrstuvABCDEFGHIJKLMNOPQRSTUVWXYV'))
            
            elif valores['lm']==True and valores['nm']==True and valores['sm']==False:
                for i in range(int(valores['caracteres'])):
                    senha.append(choice('abcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ1234567890'))
            
            elif valores['lm']==True and valores['sm']==True and valores['nm']==False:
                for i in range(int(valores['caracteres'])):
                    senha.append(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#*&%$!_-{.}'))
            
            elif valores['nm']==True and valores['lm']==False and valores['sm']==False:
                for i in range(int(valores['caracteres'])):
                    senha.append(choice('abcdefghijklmnopqrstuvwxyz1234567890'))
            
            elif valores['nm']==True and valores['lm']==False and valores['sm']==True:
                for i in range(int(valores['caracteres'])):
                    senha.append(choice('abcdefghijklmnopqrstuvwxyz1234567890@#*&%$!_-{.}'))

            elif valores['sm']==True and valores['lm']==False and valores['nm']==False:
                for i in range(int(valores['caracteres'])):
                    senha.append(choice('abcdefghijklmnopqrstuvwxyz@#*&%$!_-{.}'))
                
                         
            
            senha=''.join(senha)
            janela['xx'].update(f'sua senha: {senha}')
            senha=[]

        except ValueError:
            janela['xx'].update('insira um valor numerico entre 0 a 99')

            
            
    
       
         
    


         



