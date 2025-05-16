import sys  # Importa el módulo sys para interactuar con el intérprete de Python.
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton  # Importa las clases necesarias de PyQt5.QtWidgets para la interfaz gráfica.
from PyQt5.QtCore import QTimer, QTime, Qt  # Importa las clases QTimer para crear un temporizador, QTime para manejar el tiempo, y Qt para constantes.

class Cronometro(QWidget):  # Define una clase llamada Cronometro que hereda de QWidget (la base para todos los objetos de interfaz de usuario).
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase padre (QWidget).
        self.setWindowTitle("Cronómetro")  # Establece el título de la ventana.
        self.setGeometry(100, 100, 200, 200)  # Establece la geometría de la ventana (posición x, posición y, ancho, alto). Aumentado para los botones.

        self.tiempo = QTime(0, 0, 0)  # Inicializa un objeto QTime con el tiempo inicial de 00:00:00.
        self.timer = QTimer(self)  # Crea una instancia de QTimer asociada a esta ventana.
        self.timer.timeout.connect(self.actualizar_tiempo)  # Conecta la señal 'timeout' del timer a la función 'actualizar_tiempo'.
        self.esta_corriendo = False  # Variable para rastrear si el cronómetro está corriendo o no.

        self.etiqueta_tiempo = QLabel("00:00:00", self)  # Crea una etiqueta QLabel para mostrar el tiempo, con texto inicial "00:00:00".
        self.etiqueta_tiempo.setAlignment(Qt.AlignCenter)  # Centra el texto dentro de la etiqueta.
        self.fuente = self.etiqueta_tiempo.font()  # Obtiene la fuente actual de la etiqueta.
        self.fuente.setPointSize(20)  # Establece el tamaño de la fuente a 20 puntos.
        self.etiqueta_tiempo.setFont(self.fuente)  # Aplica la nueva fuente a la etiqueta.

        self.boton_parar = QPushButton("Parar", self)  # Crea un botón para parar el cronómetro.
        self.boton_parar.clicked.connect(self.parar_cronometro)  # Conecta el clic del botón a la función parar_cronometro.

        self.boton_continuar = QPushButton("Continuar", self)  # Crea un botón para continuar el cronómetro.
        self.boton_continuar.clicked.connect(self.continuar_cronometro)  # Conecta el clic del botón a la función continuar_cronometro.

        layout = QVBoxLayout()  # Crea un diseño vertical para organizar los widgets.
        layout.addWidget(self.etiqueta_tiempo)  # Agrega la etiqueta de tiempo al diseño.
        layout.addWidget(self.boton_parar)  # Agrega el botón "Parar" al diseño.
        layout.addWidget(self.boton_continuar)  # Agrega el botón "Continuar" al diseño.
        self.setLayout(layout)  # Establece el diseño para la ventana.

        self.iniciar_cronometro()  # Llama a la función para iniciar el cronómetro al crear la ventana.

    def iniciar_cronometro(self):
        if not self.esta_corriendo:  # Verifica si el cronómetro no está corriendo actualmente.
            self.timer.start(1000)  # Inicia el timer para que emita la señal 'timeout' cada 1000 milisegundos (1 segundo).
            self.esta_corriendo = True  # Marca el cronómetro como corriendo.

    def parar_cronometro(self):
        if self.esta_corriendo:  # Verifica si el cronómetro está corriendo.
            self.timer.stop()  # Detiene el timer.
            self.esta_corriendo = False  # Marca el cronómetro como detenido.

    def continuar_cronometro(self):  # Función para continuar el cronómetro.
        if not self.esta_corriendo:  # Verifica si el cronómetro no está corriendo.
            self.timer.start(1000)  # Reanuda el timer.
            self.esta_corriendo = True  # Marca el cronómetro como corriendo.

    def actualizar_tiempo(self):
        self.tiempo = self.tiempo.addSecs(1)  # Incrementa el tiempo en 1 segundo.
        self.etiqueta_tiempo.setText(self.tiempo.toString("hh:mm:ss"))  # Actualiza el texto de la etiqueta con el nuevo tiempo formateado como "hh:mm:ss".

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Crea una instancia de la aplicación PyQt.
    cronometro = Cronometro()  # Crea una instancia de la clase Cronometro.
    cronometro.show()  # Muestra la ventana del cronómetro.
    sys.exit(app.exec_())  # Inicia el bucle de eventos de la aplicación, que mantiene la ventana abierta y responde a las interacciones del usuario.
