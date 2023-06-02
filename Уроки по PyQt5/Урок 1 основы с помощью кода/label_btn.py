import sys  # Для получения информации о системе

from PyQt5 import QtWidgets  # Для создания виджетов
from PyQt5.QtWidgets import QApplication, QMainWindow
# QApplication - создание одного главного окна приложения
# QMainWindow - создание фреймов


def hello():
    "display hello world"
    print("Hello world")


def main():
    app = QApplication(sys.argv)  # Создание приложения.
    # В аргументах sys.argv - Информация о системе
    window = QMainWindow()  # Создание окна
    window.setWindowTitle("Простая программа")  # Установка название окна
    window.setGeometry(300, 250, 400, 500)  # Установка размер окна
    # 300 - смещение по х, 250 - смещение по у,
    # 400 - ширина окна, 500 - Длина окна

    main_text = QtWidgets.QLabel(window, text="Hello world")  # Создание метки
    # с текстом Hello world
    main_text.setText("Привет мир")  # Изменение текста метки на Привет мир
    main_text.move(300, 100)  # Установка расположения метки
    main_text.adjustSize()  # размеры выделенные для метки == размерам метки

    btn = QtWidgets.QPushButton(window)  # Создание кнопки
    btn.move(70, 150)  # Установка расположения кнопки
    btn.setText("Я был прав, но не счастлив,\
                разбуди меня огнем, может стать,\
                попытаться , может сном")  # Изменение текста кнопки
    btn.setFixedWidth(600)  # Ширина выделенная для метки == 600
    btn.clicked.connect(hello)  # Привязка функции к нажатию кнопки
    window.show()  # Отобразить окошко
    sys.exit(app.exec_())  # Устранение ошибок при выходе


main()
