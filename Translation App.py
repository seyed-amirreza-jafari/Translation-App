from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QPushButton, QTextEdit, QComboBox
from PyQt5 import uic
import sys
import googletrans
import textblob
import pyttsx3

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi('Translation_App.ui', self)

        self.input = self.findChild(QTextEdit, 'Input')
        self.output = self.findChild(QLabel, 'Output')
        self.translate_button = self.findChild(QPushButton, 'Translate_Button')
        self.input_language = self.findChild(QComboBox, 'Input_Language')
        self.output_language = self.findChild(QComboBox, 'Output_Language')

        self.languages = googletrans.LANGUAGES
        self.languages_value = self.languages.values()
#        self.languages_value = [language.capitalize() for language in self.languages_value]

        self.input_language.addItems(self.languages_value)
        self.input_language.setCurrentText('english')
        self.output_language.addItems(self.languages_value)
        self.output_language.setCurrentText('persian')
        self.output_language.removeItem(self.input_language.currentIndex())

        self.translate_button.clicked.connect(self.translate)

        self.show()

    def translate(self):
        try:
            for key, value in self.languages.items():
                if value == self.input_language.currentText():
                    input_key = key
            for key, value in self.languages.items():
                if value == self.output_language.currentText():
                    output_key = key

            words = textblob.TextBlob(self.input.toPlainText())
            words = words.translate(from_lang = input_key, to = output_key)

            self.output.setText(str(words))

            engine = pyttsx3.init()
            engine.say(words)
            engine.runAndWait()

        except Exception as E:
            QMessageBox.about(self, 'Translator', str(E))

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
