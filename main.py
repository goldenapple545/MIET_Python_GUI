#!/usr/bin/python3

# Приложение "Конвертер времени". Первая вкладка "Время" содержит две
# кнопки: "Конвертировать" и "Сбросить", а также окно ввода текста для
# ввода времени в секундах. Вторая вкладка "Формат" содержит две кнопки:
# "Выбрать" и "Сбросить", и выпадающий список из 3 опций: "Секунды в
# минуты", "Минуты в часы", "Часы в дни". Третья вкладка "Результат"
# содержит результат обработки введенного текста из "Время" с учетом
# опции, выбранной на "Формат". Формулы для работы с опциями: "Секунды
# в минуты" - время / 60, "Минуты в часы" - время / 60, "Часы в дни" - время /
# 24

import PySimpleGUI as sg

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Создаем список элементов для первой вкладки
    tab1_layout = [
        [sg.Text('Input time(sec):')],
        [sg.Input(key='-INPUT-')],
        [sg.Button('Convert')],
        [sg.Button('Reset')]
    ]
    # Создаем список элементов для второй вкладки
    tab2_layout = [
        [sg.Text('Choose convert to:')],
        [sg.Combo(['Seconds in minutes', 'Minutes in hours', 'Hours in days'], key='-OPTION-')],
        [sg.Button('Choose')],
        [sg.Button('Reset')]
    ]
    # Создаем список элементов для третьей вкладки
    tab3_layout = [
        [sg.Text('Result:', size=(15, 1), justification='center')],
        [sg.Text(size=(40, 1), key='-RESULT-')]
    ]
    # Создаем вкладки
    tab_group_layout = [
        [sg.Tab('Time', tab1_layout), sg.Tab('Format', tab2_layout),
         sg.Tab('Result', tab3_layout)]
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
            elif values['-OPTION-'] == 'Символы':
                result = len(values['-INPUT-'])
            elif values['-OPTION-'] == 'Строки':
                result = len(values['-INPUT-'].split('\n'))
            window['-RESULT-'].update(f'Количество: {result}')
    window.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
