import PySimpleGUI as sg
from random import choice
sg.theme('Topanga')

layout = [
    [sg.Text('Gerador de Senhas', font='Calibri 15')],
    [sg.Text('Escolha as caracteristicas da tua Senha aqui:', font='Calibri 10')],
    [sg.InputCombo(('Letras e Números ', 'Letras (M/m) e Números ', 'Somente números '), key='scn', font='any 8'), sg.Button('Gerar', font='Calibri 10'), sg.Button('Exit', font='Calibri 10')],

          ]

window = sg.Window('Gerador de Senhas.', layout, no_titlebar=True, alpha_channel=.8, grab_anywhere=True)
event = window.read()

while True:
    event, values = window.read()
    if event == 'Gerar':
        if values['scn'] == 'Letras e Números ':
            saida_senha_padrao = []
            for n in range(0, 10):
                senha_padrao = choice(
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'x', 'z'])
                saida_senha_padrao.append(str(senha_padrao))
            saida1 = ''.join(saida_senha_padrao)
            sg.popup_quick_message(saida1, background_color='black')

        elif values['scn'] == 'Letras (M/m) e Números ':
            saida_senha_mm = []
            for n in range(0, 10):
                senha_padrao = choice(
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'x', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z'])
                saida_senha_mm.append(str(senha_padrao))
            saida2 = ''.join(saida_senha_mm)
            sg.popup_quick_message(saida2, background_color='black')

        elif values['scn'] == 'Somente números ':
            saida_senha_sn = []
            for n in range(0, 10):
                senha_padrao = choice(
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
                saida_senha_sn.append(str(senha_padrao))
            saida3 = ''.join(saida_senha_sn)
            sg.popup_quick_message(saida3, background_color='black')
    if event == 'Exit':
        break