import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt

class SecondPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Добавьте элементы интерфейса для второй страницы здесь
        list_widget = QListWidget(self)
        list_widget.setStyleSheet("color: black; border-radius: 10px; font-size: 15px;")
        list_widget.resize(100, 300)
        list_widget.move(200, 50)
        list_widget.setSpacing(3)

        words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'indianry', 'jackfruit']
        for word in words:
            item = QListWidgetItem(word)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)  # Установка флага Qt.ItemIsUserCheckable
            item.setCheckState(Qt.Unchecked)  # Установка начального состояния флажка
            list_widget.addItem(item)

        list_widget = QListWidget(self)
        list_widget.setStyleSheet("color: black; border-radius: 10px; font-size: 15px;")
        list_widget.resize(100, 300)
        list_widget.move(350, 50)
        list_widget.setSpacing(3)

        # Заполнение списка словами
        words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'indianry', 'jackfruit']
        for word in words:
            item = QListWidgetItem(word)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)  # Установка флага Qt.ItemIsUserCheckable
            item.setCheckState(Qt.Unchecked)  # Установка начального состояния флажка
            list_widget.addItem(item)


        list_widget = QListWidget(self)
        list_widget.setStyleSheet("color: black; border-radius: 10px; font-size: 15px;")
        list_widget.resize(100, 300)
        list_widget.move(500, 50)
        list_widget.setSpacing(3)

        # Заполнение списка словами
        words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'indianry', 'jackfruit']
        for word in words:
            item = QListWidgetItem(word)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)  # Установка флага Qt.ItemIsUserCheckable
            item.setCheckState(Qt.Unchecked)  # Установка начального состояния флажка
            list_widget.addItem(item)

        list_widget = QListWidget(self)
        list_widget.setStyleSheet("color: black; border-radius: 10px; font-size: 15px;")
        list_widget.resize(100, 300)
        list_widget.move(650, 50)
        list_widget.setSpacing(3)

        # Заполнение списка словами
        words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'indianry', 'jackfruit']
        for word in words:
            item = QListWidgetItem(word)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)  # Установка флага Qt.ItemIsUserCheckable
            item.setCheckState(Qt.Unchecked)  # Установка начального состояния флажка
            list_widget.addItem(item)

        # Добавьте кнопку для возврата на первую страницу
        button = QPushButton('Back', self)
        button.setStyleSheet("background-color: red; color: white; border-radius: 10px; font-size: 15px;")
        button.resize(100, 32)
        button.move(50, 380)
        button.clicked.connect(self.showFirstPage)

        self.setGeometry(100, 100, 800, 480)
        self.setWindowTitle('Poe Friend')

    def showFirstPage(self):
        self.hide()
        widget.show()

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Добавьте элементы интерфейса для первой страницы здесь
        button1 = QPushButton('Exit', self)
        button1.setStyleSheet("background-color: red; color: white; border-radius: 10px; font-size: 15px;")
        button1.resize(100, 32)
        button1.move(50, 50)

        button2 = QPushButton('Start', self)
        button2.setStyleSheet("background-color: red; color: white; border-radius: 10px; font-size: 15px;")
        button2.resize(100, 32)
        button2.move(50, 100)

        button3 = QPushButton('Settings', self)
        button3.setStyleSheet("background-color: red; color: white; border-radius: 10px; font-size: 15px;")
        button3.resize(100, 32)
        button3.move(50, 150)

        button4 = QPushButton('Coord 1', self)
        button4.setStyleSheet("background-color: red; color: white; border-radius: 10px; font-size: 15px;")
        button4.resize(100, 32)
        button4.move(50, 200)

        button5 = QPushButton('Coord 2', self)
        button5.setStyleSheet("background-color: red; color: white; border-radius: 10px; font-size: 15px;")
        button5.resize(100, 32)
        button5.move(50, 250)

        # Добавьте кнопку для переключения на вторую страницу
        button6 = QPushButton('Second Page', self)
        button6.setStyleSheet("background-color: red; color: white; border-radius: 10px; font-size: 15px;")
        button6.resize(100, 32)
        button6.move(50, 380)
        button6.clicked.connect(self.showSecondPage)

        # Добавьте список на первую страницу
        list_widget = QListWidget(self)
        list_widget.setStyleSheet("color: black; border-radius: 10px; font-size: 15px;")
        list_widget.resize(100, 300)
        list_widget.move(200, 50)
        list_widget.setSpacing(3)

        # Заполнение списка словами
        words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'indianry', 'jackfruit']
        for word in words:
            item = QListWidgetItem(word)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)  # Установка флага Qt.ItemIsUserCheckable
            item.setCheckState(Qt.Unchecked)  # Установка начального состояния флажка
            list_widget.addItem(item)

        list_widget = QListWidget(self)
        list_widget.setStyleSheet("color: black; border-radius: 10px; font-size: 15px;")
        list_widget.resize(100, 300)
        list_widget.move(350, 50)
        list_widget.setSpacing(3)

        # Заполнение списка словами
        words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'indianry', 'jackfruit']
        for word in words:
            item = QListWidgetItem(word)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)  # Установка флага Qt.ItemIsUserCheckable
            item.setCheckState(Qt.Unchecked)  # Установка начального состояния флажка
            list_widget.addItem(item)


        list_widget = QListWidget(self)
        list_widget.setStyleSheet("color: black; border-radius: 10px; font-size: 15px;")
        list_widget.resize(100, 300)
        list_widget.move(500, 50)
        list_widget.setSpacing(3)

        # Заполнение списка словами
        words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'indianry', 'jackfruit']
        for word in words:
            item = QListWidgetItem(word)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)  # Установка флага Qt.ItemIsUserCheckable
            item.setCheckState(Qt.Unchecked)  # Установка начального состояния флажка
            list_widget.addItem(item)

        list_widget = QListWidget(self)
        list_widget.setStyleSheet("color: black; border-radius: 10px; font-size: 15px;")
        list_widget.resize(100, 300)
        list_widget.move(650, 50)
        list_widget.setSpacing(3)

        # Заполнение списка словами
        words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'indianry', 'jackfruit']
        for word in words:
            item = QListWidgetItem(word)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)  # Установка флага Qt.ItemIsUserCheckable
            item.setCheckState(Qt.Unchecked)  # Установка начального состояния флажка
            list_widget.addItem(item)

        self.secondPage = SecondPage()
        self.secondPage.hide()

        self.setGeometry(100, 100, 800, 480)
        self.setWindowTitle('Poe Friend')

    def showSecondPage(self):
        self.hide()
        self.secondPage.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())