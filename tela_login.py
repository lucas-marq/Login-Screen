import PySimpleGUI as sg
# sg para facilitar na chamada do PySimpleGUI
from PySimpleGUI.PySimpleGUI import WIN_CLOSED

# Layout
sg.theme('Reddit')
linha = [
    [sg.Text('Usuário:'), sg.Input(key='usuario')],
    [sg.Text('Senha:'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Entrar')]
]
# janela
janela = sg.Window('Tela de Login', linha)

# ler os eventos
while True:
    events, values = janela.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == 'Entrar':
        if values['usuario'] == 'Lucas' and values['senha'] == 'zxFd4cAR@58':
            print('Bem vindo, Lucas')
