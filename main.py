from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QButtonGroup
import sys, os
import resources_rc
import zapretAPI as zapi
from updater import Updater
from zapretGUI import Ui_MainWindow
from filters import Ui_FiltersWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.updater = Updater()
        self.z_exec = zapi.Exec()
        self.z_service = zapi.Service()
        self.z_task = zapi.Task()

        self.pushButton_00.clicked.connect(self.install_zapret)
        if os.path.exists(self.updater.name):
            self.pushButton_00.setText('Обновить')
        else:
            self.pushButton_00.setText('Установить')

        self.filters_window = FiltersWindow(self)
        self.pushButton_02.clicked.connect(self.open_filters)

        self.pushButton_13.clicked.connect(self.start_exec)
        self.pushButton_14.clicked.connect(self.stop_exec)

        self.buttonGroup_11 = QButtonGroup()
        self.buttonGroup_11.addButton(self.radioButton_11)
        self.buttonGroup_11.addButton(self.radioButton_12)
        self.buttonGroup_11.addButton(self.radioButton_13)
        
        self.buttonGroup_11.buttonClicked.connect(self.on_radiobutton_toggled)

        self.show()

    def install_zapret(self):
        '''Install or update zapret software.'''
        self.pushButton_00.setEnabled(False)
        self.updater.get_zapret(self.updater.url, self.updater.name, True)
        self.pushButton_00.setText('Обновить')
        self.pushButton_00.setEnabled(True)

    def open_filters(self):
        '''Opens filters window.'''
        self.filters_window.exec()

    def on_radiobutton_toggled(self):
        '''Change push buttons functions depending on radio button selected.'''
        self.pushButton_11.clicked.disconnect()
        self.pushButton_12.clicked.disconnect()
        self.pushButton_13.clicked.disconnect()
        self.pushButton_14.clicked.disconnect()

        selected_button = self.buttonGroup_11.checkedButton()
        if selected_button == self.radioButton_12:
            self.pushButton_11.clicked.connect(self.create_service)
            self.pushButton_12.clicked.connect(self.delete_service)
            self.pushButton_13.clicked.connect(self.start_service)
            self.pushButton_14.clicked.connect(self.stop_service)
        elif selected_button == self.radioButton_13:
            self.pushButton_11.clicked.connect(self.create_task)
            self.pushButton_12.clicked.connect(self.delete_task)
            self.pushButton_13.clicked.connect(self.start_task)
            self.pushButton_14.clicked.connect(self.stop_task)
        else:
            self.pushButton_13.clicked.connect(self.start_exec)
            self.pushButton_14.clicked.connect(self.stop_exec)

    def start_exec(self):
        if self.filters_window.z_args:
            self.z_exec.start(self.filters_window.z_args)
            QtWidgets.QMessageBox.information(self, 'Info', 'zapret started!')
        else:
            QtWidgets.QMessageBox.information(self, 'Error', 'Add filters and try again!')

    def stop_exec(self):
        self.z_exec.stop()
        QtWidgets.QMessageBox.information(self, 'Info', 'zapret stopped!')

    def create_service(self):
        if self.filters_window.z_args:
            self.z_service.create(self.filters_window.z_args)
            QtWidgets.QMessageBox.information(self, 'Info', 'Service created!')
        else:
            QtWidgets.QMessageBox.information(self, 'Error', 'Add filters and try again!')

    def delete_service(self):
        self.z_service.delete()
        QtWidgets.QMessageBox.information(self, 'Info', 'Service deleted!')

    def start_service(self):
        self.z_service.start()
        QtWidgets.QMessageBox.information(self, 'Info', 'Service started!')

    def stop_service(self):
        self.z_service.stop()
        QtWidgets.QMessageBox.information(self, 'Info', 'Service stopped!')

    def create_task(self):
        if self.filters_window.z_args:
            self.z_task.create(self.filters_window.z_args)
            QtWidgets.QMessageBox.information(self, 'Info', 'Service created!')
        else:
            QtWidgets.QMessageBox.information(self, 'Error', 'Add filters and try again!')

    def delete_task(self):
        self.z_task.delete()
        QtWidgets.QMessageBox.information(self, 'Info', 'Task deleted!')

    def start_task(self):
        self.z_task.start()
        QtWidgets.QMessageBox.information(self, 'Info', 'Task started!')

    def stop_task(self):
        self.z_task.stop()
        QtWidgets.QMessageBox.information(self, 'Info', 'Task stopped!')


class FiltersWindow(QDialog, Ui_FiltersWindow):
    def __init__(self, master_window):
        super().__init__(master_window)
        self.setupUi(self)
        self.z_args = None
        
        self.comboBox.currentTextChanged.connect(self.fill_textedit)
        self.pushButton_3.clicked.connect(self.apply_filters)
        self.pushButton_4.clicked.connect(self.textEdit.clear)
        self.textEdit.textChanged.connect(self.apply_button_setEnabled)
    
    def showEvent(self, event):
        self.argparser = zapi.ArgParser()
        for strategy, path in self.argparser.strat_files.items():
            self.comboBox.addItem(strategy, path)
        super().showEvent(event)

    def fill_textedit(self, filename):
        raw_args = self.argparser.import_args(self.comboBox.currentData())
        self.textEdit.setPlainText(raw_args)

    def apply_filters(self):
        raw_args = self.textEdit.toPlainText()
        self.z_args = self.argparser.filter_args(raw_args)
        self.pushButton_3.setEnabled(False)

    def apply_button_setEnabled(self):
        self.pushButton_3.setEnabled(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setWindowIcon(QIcon(":/icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())