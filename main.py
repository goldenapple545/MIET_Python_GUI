#!/usr/bin/python3

import PySimpleGUI as sg

if __name__ == '__main__':
    # Создаем список элементов для первой вкладки
    tab1_layout = [
        [sg.Text('Input time:')],
        [sg.Input(key='-INPUT-')],
        [sg.Button('Convert')],
        [sg.Button('Reset', key='-RESET-')]
    ]
    # Создаем список элементов для второй вкладки
    tab2_layout = [
        [sg.Text('Choose convert to:')],
        [sg.Combo(['Seconds in minutes', 'Minutes in hours', 'Hours in days'], key='-OPTION-', default_value='Seconds in minutes')],
        [sg.Button('Choose')],
        [sg.Button('Reset', key='-RESET-')]
    ]
    # Создаем список элементов для третьей вкладки
    tab3_layout = [
        [sg.Text('Result:', size=(15, 1), justification='center')],
        [sg.Text(size=(40, 1), key='-RESULT-')]
    ]
    # Создаем вкладки
    tab_group_layout = [
        [sg.Tab('Time', tab1_layout, key='-TAB1-'), sg.Tab('Format', tab2_layout),
         sg.Tab('Result', tab3_layout, key='-TAB3-')]
    ]
    # Создаем окно приложения
    layout = [[sg.TabGroup(tab_group_layout)]]
    window = sg.Window('Time Converter', layout)

    # Обработка событий
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Convert':
            if values['-OPTION-'] == 'Seconds in minutes':
                result = int(values['-INPUT-']) // 60
            elif values['-OPTION-'] == 'Minutes in hours':
                result = int(values['-INPUT-']) // 60
            elif values['-OPTION-'] == 'Hours in days':
                result = int(values['-INPUT-']) // 24
            window['-RESULT-'].update(f'Time: {result}')
            window['-TAB3-'].select()
        elif event == 'Choose':
            window['-TAB1-'].select()
        elif event == '-RESET-':
            window['-RESULT-'].update(value='')
            window.write_event_value('-INPUT-', '')
            window['-INPUT-'].update(value='')
    window.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
