
from ast import Try
from msilib.schema import ComboBox
from random import choice
from PySimpleGUI import PySimpleGUI as sg



#   declarando as variaveis
senha=[]
senha_final=[]


#   layout da janela
sg.theme('Black')
layout=[
    [sg.Text('digite o numero de caracteres que sua senha deve ter'), sg.Input(key='caracteres', size=(2,0))],
    [sg.Check('letras', key='l'),sg.Check('letras maiusculas', key='lm'),sg.Check('numeros', key='nm'), sg.Check('simbolos', key='sm')],
    [sg.Text('sua senha: ', key='xx')],
    [sg.Button('gerar')],
]


#   criando sistema de atualizaçao de tela
janela=sg.Window('gerador de senha',layout, element_justification='c')
while True:
    eventos, valores= janela.read(timeout=6)
    if eventos == sg.WIN_CLOSED:
        break

    if eventos == 'gerar':
        try:
            if  valores['lm']== True:
                senha.append('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            if valores['nm']==True:
                senha.append('12345678901234567890')
            if valores['sm']==True:
                senha.append('@#$%&*"()^?/_-@#$%&*"()^?/_-')
            if valores['l']==True:
                senha.append('abcdefghijklmnopqrstuvwxyz')

            
            senha=''.join(senha)
            senha=[x for x in senha]
            
            for i in range(int(valores['caracteres'])):
                senha_final.append(choice(senha))
            
            senha_final=''.join(senha_final)
            janela['xx'].update(f'sua senha: {senha_final}')
            senha=[]
            senha_final=[]


        #  tratando erros
        except ValueError or IndexError:
            janela['xx'].update('insira um valor numerico entre 0 a 99')



            
    

            
            
    
       
         
    


         



