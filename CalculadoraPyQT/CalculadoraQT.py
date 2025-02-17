from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt
from PyQt6 import uic
from pathlib import Path

import sys
import math


# Subclass Calculadora to customize your application's main window
class Calculadora(QMainWindow):
    
    def __init__(self, *args, **kwargs):

        ruta = Path(__file__).parent

        super(Calculadora, self).__init__(*args, **kwargs)

        uic.loadUi(f"{ruta}/Calculadora.ui", self)

        self.setWindowTitle("Calculadora")
        self.setWindowIcon(QIcon(str(ruta / "calculadora.png")))


        # Conectar los botones
        self.conectarBotones()

        # Variables para almacenar el historial de operaciones
        self.historial = []
        self.operacion_actual = ""

    def conectarBotones(self):
        for i in range(0, 10):
            getattr(self, f"pushButton_{i}").clicked.connect(lambda _, num = i: self.agregar_texto(str(num)))

        # Operaciones
        self.pushButton_sum.clicked.connect(self.agregar_suma)
        self.pushButton_res.clicked.connect(self.agregar_resta)
        self.pushButton_mul.clicked.connect(self.agregar_multiplicacion)
        self.pushButton_div.clicked.connect(self.agregar_division)
        self.pushButton_par_izq.clicked.connect(self.agregar_par_izq)
        self.pushButton_par_der.clicked.connect(self.agregar_par_der)
        self.pushButton_punto.clicked.connect(self.agregar_punto)
        self.pushButton_porc.clicked.connect(self.agregar_porcentaje)
        self.pushButton_raiz.clicked.connect(self.raiz_cuadrada)

        # Funcionalidad
        self.pushButton_igual.clicked.connect(self.evaluar_expresion)
        self.pushButton_clear.clicked.connect(self.limpiar_pantalla)
        self.pushButton_del.clicked.connect(self.borrar_ultimo)
        self.pushButton_hist.clicked.connect(self.mostrar_historial)
        self.pushButton_ce.clicked.connect(self.borrar_historial)

    def crear_manejador_numero(self, num):
        def manejador():
            self.agregar_texto(str(num))
        return manejador

    def agregar_suma(self):
        self.agregar_texto("+")

    def agregar_resta(self):
        self.agregar_texto("-")

    def agregar_multiplicacion(self):
        self.agregar_texto("*")

    def agregar_division(self):
        self.agregar_texto("/")

    def agregar_par_izq(self):
        self.agregar_texto("(")

    def agregar_par_der(self):
        self.agregar_texto(")")

    def agregar_punto(self):
        self.agregar_texto(".")

    def agregar_porcentaje(self):
        self.agregar_texto("%")

    def raiz_cuadrada(self):
        try:
            numero = float(self.operacion_actual)  # Convierte la expresión actual en número
            if numero < 0:
                QMessageBox.critical(self, "Error", "No se puede calcular la raíz de un número negativo.", QMessageBox.StandardButton.Ok)
            else:
                resultado = math.sqrt(numero)
                self.historial.append(f"√{numero} = {resultado}")  # Agregar al historial
                self.label.setText(str(resultado))
                self.operacion_actual = str(resultado)
        except ValueError:
            QMessageBox.critical(self, "Error", "Expresión no válida para calcular la raíz cuadrada.", QMessageBox.StandardButton.Ok)

    # Agrega numeros y operadores al QLabel
    def agregar_texto(self, texto):
        self.operacion_actual += texto
        self.label.setText(self.operacion_actual)
    
    # Limpia la pantalla actual
    def limpiar_pantalla(self):
        self.operacion_actual = ""
        self.label.setText("")
    
    def borrar_ultimo(self):
        self.operacion_actual = self.operacion_actual[:-1]
        self.label.setText(self.operacion_actual)
    
    def evaluar_expresion(self):
        try:
            resultado = eval(self.operacion_actual)  # Evalúa la expresión matemática
            self.historial.append(f"{self.operacion_actual} = {resultado}")  # Guarda en historial
            self.label.setText(str(resultado))
            self.operacion_actual = str(resultado)
        except Exception:
            QMessageBox.critical(self, "Error", "Expresión no válida", QMessageBox.StandardButton.Ok)
            self.limpiar_pantalla()

    
    def mostrar_historial(self):
        historial_window = Historial(self.historial)
        historial_window.exec()
    
    def borrar_historial(self):
        self.historial.clear()
        QMessageBox.information(self, "Historial", "El historial ha sido borrado.", QMessageBox.StandardButton.Ok)

        
class Historial(QDialog):
    def __init__(self, historial, *args, **kwargs):
        super(Historial, self).__init__(*args, **kwargs)

        ruta = Path(__file__).parent
        uic.loadUi(f"{ruta}/Historial.ui", self)  # Cargar el diseño de Qt Designer

        self.setWindowTitle("Historial")
        self.setWindowIcon(QIcon(str(ruta / "calculadora.png")))


        # Acceder al QTableWidget desde el archivo .ui
        self.historial_table = self.findChild(QTableWidget, "tableWidget")

        # Ajustar columnas automáticamente
        self.historial_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        header_item_1 = QTableWidgetItem("ID")
        header_item_2 = QTableWidgetItem("Operacion")
        header_item_3 = QTableWidgetItem("Resultado")

        self.historial_table.setHorizontalHeaderItem(0, header_item_1)
        self.historial_table.setHorizontalHeaderItem(1, header_item_2)
        self.historial_table.setHorizontalHeaderItem(2, header_item_3)

        # Llenar tabla con historial
        self.cargar_historial(historial)

    def cargar_historial(self, historial):
        self.historial_table.setRowCount(len(historial))  
        for i, entrada in enumerate(historial):
            if "=" in entrada:
                operacion, resultado = entrada.split("=")
                # Crear y centrar los items
                id_item = QTableWidgetItem(str(i + 1))
                operacion_item = QTableWidgetItem(operacion.strip())
                resultado_item = QTableWidgetItem(resultado.strip())
                
                # Centrar el texto
                id_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                operacion_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                resultado_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                
                # Establecer los elementos en las celdas
                self.historial_table.setItem(i, 0, id_item)  
                self.historial_table.setItem(i, 1, operacion_item)  
                self.historial_table.setItem(i, 2, resultado_item) 

   
    

app = QApplication(sys.argv)

window = Calculadora()
window.show()

# Start the event loop.
app.exec()
