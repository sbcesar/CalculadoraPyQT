from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
from pathlib import Path

import sys

# Subclass Calculadora to customize your application's main window
class Calculadora(QMainWindow):
    
    def __init__(self, *args, **kwargs):

        ruta = Path.cwd()

        super(Calculadora, self).__init__(*args, **kwargs)

        uic.loadUi(f"{ruta}/Calculadora.ui", self)

        self.setWindowTitle("Calculadora")
        

        
    

app = QApplication(sys.argv)

window = Calculadora()
window.show()

# Start the event loop.
app.exec()
