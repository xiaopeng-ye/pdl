from PyQt5.QtWidgets import QFileDialog
from src.gui.ventana_ui import *

route = None


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Botones
        self.BBuscar.clicked.connect(self.openFileNameDialog)
        self.BCancelar.clicked.connect(self.close)
        self.BAceptar.clicked.connect(self.save)

        # Guardar
        # self.BOk.clicked.connect(self.saveFileDialog)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                              "All Files (*);;Python Files (*.py)", options=options)
        if file:
            # print(fileName)
            self.textEdit.setPlainText(file)
            global route
            route = file

    def save(self):
        # Pasar la ruta del fichero
        text = self.textEdit.toPlainText()
        if text == '':
            print('Error, fichero no especificado', file=sys.stderr)
        else:
            print(text)
            self.close()

    # def openFileNamesDialog(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
    #                                             "All Files (*);;Python Files (*.py)", options=options)
    #     if files:
    #         print(files)

    # def saveFileDialog(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
    #                                               "All Files (*);;Text Files (*.txt)", options=options)
    #     if fileName:
    #         print(fileName)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
