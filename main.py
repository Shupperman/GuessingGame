import sys # Allows us to interact with our system
import random # Allows us to interect with random numbers and choices
from PySide6 import QtCore, QtWidgets, QtGui # Qt libraries needed to make GUI


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__() # Calls the QtWidgets.QWidget constructor (parent constructor)

        self.right = ["You Guessed Right!!", "That number is correct!!", "Guessed Right!!"]
        self.wrong = ["Broke Bitch", "Dumbass", "Not Correct..."]
        self.improper = ["Invalid Input"]
        
        # Labels
        self.titleText = QtWidgets.QLabel("Guess A Number 1 Through 10", alignment=QtCore.Qt.AlignCenter) # Creates a label that is center aligned
        self.outputText = QtWidgets.QLabel("Output Text", alignment=QtCore.Qt.AlignCenter) # Creates a label that is center aligned
        
        # Buttons
        self.button = QtWidgets.QPushButton("Guess Number") # Creates a button that says click me
        
        # Entry Boxes
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.titleText) # Adds the label to the widget
        self.layout.addWidget(self.button) # Adds the button to the widget
        self.layout.addWidget(self.outputText) # Adds the label to the widget

        self.button.clicked.connect(self.magic) # Runs the command (function) called magic

    @QtCore.Slot()
    def magic(self):
        self.outputText.setText(random.choice(self.right))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())