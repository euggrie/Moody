from datetime import datetime
import sys
from PyQt4 import QtGui, QtCore
from anybar import AnyBar


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 400, 300)
        self.setWindowTitle("Moody")
        self.setWindowIcon(QtGui.QIcon('smiley.png'))
        QtGui.QApplication.setStyle("plastique")

        self.home()
        self.raise_()

    def home(self):
        today = QtGui.QLabel("How do you feel?", self)
        today.move(150, 25)

        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        btn.resize(btn.minimumSizeHint())
        btn.move(300, 250)

        btn1 = QtGui.QPushButton("Sad", self)
        btn1.clicked.connect(self.red)
        btn1.resize(btn.minimumSizeHint())
        btn1.move(200, 70)

        btn2 = QtGui.QPushButton("Nervous", self)
        btn2.clicked.connect(self.orange)
        btn2.resize(btn.minimumSizeHint())
        btn2.move(110, 70)

        btn3 = QtGui.QPushButton("Anxious", self)
        btn3.clicked.connect(self.yellow)
        btn3.resize(btn.minimumSizeHint())
        btn3.move(200, 100)

        btn4 = QtGui.QPushButton("Calm", self)
        btn4.clicked.connect(self.green)
        btn4.resize(btn.minimumSizeHint())
        btn4.move(110, 100)

        btn5 = QtGui.QPushButton("Hopeful", self)
        btn5.clicked.connect(self.cyan)
        btn5.resize(btn.minimumSizeHint())
        btn5.move(200, 130)

        btn6 = QtGui.QPushButton("Happy", self)
        btn6.clicked.connect(self.blue)
        btn6.resize(btn.minimumSizeHint())
        btn6.move(110, 130)

        btn7 = QtGui.QPushButton("Nostalgic", self)
        btn7.clicked.connect(self.purple)
        btn7.resize(btn.minimumSizeHint())
        btn7.move(200, 160)

        btn8 = QtGui.QPushButton("Despair", self)
        btn8.clicked.connect(self.black)
        btn8.resize(btn.minimumSizeHint())
        btn8.move(110, 160)

        self.show()

    def red(self):
        AnyBar().change('red', text='Mood = Sad')
        date = datetime.now()
        print(date)

    def orange(self):
        AnyBar().change('orange', text='Mood = Nervous')

    def yellow(self):
        AnyBar().change('yellow', text='Mood = Anxious')
        reply = QtGui.QMessageBox.information(self, "", "Why don't you try some breathing exercises?")

    def green(self):
        AnyBar().change('green', text='Mood = Calm')

    def cyan(self):
        AnyBar().change('cyan', text='Mood = Hopeful')

    def blue(self):
        AnyBar().change('blue', text='Mood = Happy')

    def purple(self):
        AnyBar().change('purple', text='Mood = Nostalgic')
        reply = QtGui.QMessageBox.information(self, "", "Why don't you try listening to Darwin?")

    def black(self):
        AnyBar().change('black', text='Mood = Despair')
        reply = QtGui.QMessageBox.information(self, "",
                                              "Stop what you are doing, have a relaxing tea and watch some cat videos")


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
