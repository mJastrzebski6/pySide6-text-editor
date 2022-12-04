from PySide6.QtCore import Qt, QSize
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QColorDialog, QToolBar, QStatusBar, QFileDialog, QTextEdit, QFontComboBox
from PySide6.QtGui import QAction, QIcon, QFont
from PySide6 import QtGui

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Edytor tekstu - nowy dokument")
        self.fileOpened = False

        appIcon = QIcon("Icons/icons8-window.png")
        self.setWindowIcon(appIcon)

        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolBar = QToolBar('Menu główne')
        toolBar.setIconSize(QSize(32, 32))
        toolBar.setContextMenuPolicy(Qt.PreventContextMenu)
        self.addToolBar(toolBar)

        self.openFileButton = QAction(QIcon("Icons/icons8-opened-folder-32.png"), '&Otwórz', self)
        self.openFileButton.setStatusTip('Otwórz plik')
        self.openFileButton.triggered.connect(self.openFile)
        toolBar.addAction(self.openFileButton)

        self.newFileButton = QAction(QIcon("Icons/icons8-add-file-32.png"), '&Stwórz', self)
        self.newFileButton.setStatusTip('Stwórz plik')
        self.newFileButton.triggered.connect(self.createFile)
        toolBar.addAction(self.newFileButton)

        self.saveFileButton = QAction(QIcon("Icons/icons8-check-file-32.png"), '&Zapisz', self)
        self.saveFileButton.setStatusTip('Zapisz plik')
        self.saveFileButton.triggered.connect(self.saveFile)
        toolBar.addAction(self.saveFileButton)

        toolBar.addSeparator()

        self.boldTextButton = QAction(QIcon("Icons/icons8-bold-32.png"), '&Pogrub', self)
        self.boldTextButton.setStatusTip('Pogrub tekst')
        self.boldTextButton.triggered.connect(self.boldText)
        toolBar.addAction(self.boldTextButton)
        self.boldTextButton.setCheckable(True)

        self.italicTextButton = QAction(QIcon("Icons/icons8-italic-32.png"), '&Pochyl', self)
        self.italicTextButton.setStatusTip('Pochyl tekst')
        self.italicTextButton.triggered.connect(self.italicText)
        toolBar.addAction(self.italicTextButton)
        self.italicTextButton.setCheckable(True)

        self.underlineTextButton = QAction(QIcon("Icons/icons8-underline-32.png"), '&Podkreść', self)
        self.underlineTextButton.setStatusTip('Podkreśl tekst')
        self.underlineTextButton.triggered.connect(self.underlineText)
        toolBar.addAction(self.underlineTextButton)
        self.underlineTextButton.setCheckable(True)

        toolBar.addSeparator()

        self.textToLeftButton = QAction(QIcon("Icons/icons8-align-left-32.png"), '&Tekst do lewej', self)
        self.textToLeftButton.setStatusTip('Tekst do lewej')
        self.textToLeftButton.triggered.connect(self.textToLeft)
        toolBar.addAction(self.textToLeftButton)
        self.textToLeftButton.setCheckable(True)
        #.textToLeftButton.setChecked(True)

        self.textToCenterButton = QAction(QIcon("Icons/icons8-align-center-32.png"), '&Centruj tekst', self)
        self.textToCenterButton.setStatusTip('Centruj tekst')
        self.textToCenterButton.triggered.connect(self.textToCenter)
        toolBar.addAction(self.textToCenterButton)
        self.textToCenterButton.setCheckable(True)

        self.textToRightButton = QAction(QIcon("Icons/icons8-align-right-32.png"), '&Tekst do prawej', self)
        self.textToRightButton.setStatusTip('Tekst do prawej')
        self.textToRightButton.triggered.connect(self.textToRight)
        toolBar.addAction(self.textToRightButton)
        self.textToRightButton.setCheckable(True)

        self.justifyTextButton = QAction(QIcon("Icons/icons8-align-justify-32.png"), '&Wyjustuj tekst', self)
        self.justifyTextButton.setStatusTip('Wyjustuj tekst')
        self.justifyTextButton.triggered.connect(self.textJustify)
        toolBar.addAction(self.justifyTextButton)
        self.justifyTextButton.setCheckable(True)

        toolBar.addSeparator()

        self.textColorButton = QAction(QIcon("Icons/icons8-text-color-32.png"), '&Zmień kolor tekstu', self)
        self.textColorButton.setStatusTip('Zmień kolor tekstu')
        self.textColorButton.triggered.connect(self.changeFontColor)
        toolBar.addAction(self.textColorButton)

        self.colorRect = QLabel("")
        self.colorRect.setFixedSize(32, 32)
        self.colorRect.setStyleSheet("background-color: #000000")
        toolBar.addWidget(self.colorRect)

        toolBar.addSeparator()

        self.fontCombobox = QFontComboBox()
        self.fontCombobox.setFixedHeight(32)
        self.fontCombobox.currentFontChanged.connect(self.changeFont)
        toolBar.addWidget(self.fontCombobox)


        self.setStatusBar(QStatusBar(self))

        self.allLayout = QVBoxLayout()
        self.textEdit = QTextEdit("")
        font = QtGui.QFont()
        font.setPointSize(16)

        self.textEdit.setFont(font)

        self.allLayout.setContentsMargins(20, 20, 20, 20)
        self.allLayout.setSpacing(20)
        #self.textLabel.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.allLayout.addWidget(self.textEdit)
        self.allWidget = QWidget()
        self.allWidget.setLayout(self.allLayout)

        self.setMinimumSize(750, 200)
        self.setCentralWidget(self.allWidget)

    def toolBarButtonClick(self, s):
        print('Click', s)

    def openFile(self):
        print("open file")
        fname = QFileDialog.getOpenFileName(self, "Open File", 'c:\\', "Text files (*.txt)")
        print(fname[0])
        if fname[0] == "":
            return
        file = open(fname[0], "r")
        self.textEdit.setHtml(file.read())

        file.close()
        self.fileOpened = True
        self.path = fname[0]
        self.setWindowTitle("Edytor tekstu - " + self.path)


    def saveFile(self):
        print("save file")
        if not self.fileOpened:
            self.createFile()
            return

        file = open(self.path, "w")
        file.write(self.textEdit.toHtml())
        file.close()

    def createFile(self):
        print("create file")
        filename = QFileDialog.getSaveFileName(self, "Save File", 'c:\\', "Text files (*.txt)")
        file = open(filename[0], "x")
        file.write(self.textEdit.toHtml())
        file.close()
        self.fileOpened = True
        self.path = filename[0]
        self.setWindowTitle("Edytor tekstu - " + self.path)

    def boldText(self):
        print("text bolded")
        if self.textEdit.fontWeight() != 700:
            self.textEdit.setFontWeight(QFont.Bold)
            return
        self.textEdit.setFontWeight(QFont.Normal)


    def italicText(self):
        print("text italic")
        if self.textEdit.fontItalic():
            self.textEdit.setFontItalic(False)
            return

        self.textEdit.setFontItalic(True)

    def underlineText(self):
        print("text underlined")
        if self.textEdit.fontUnderline():
            self.textEdit.setFontUnderline(False)
            return

        self.textEdit.setFontUnderline(True)

    def textToLeft(self):
        print("text to left")
        self.textToCenterButton.setChecked(False)
        self.textToRightButton.setChecked(False)
        self.justifyTextButton.setChecked(False)
        self.textEdit.setAlignment(Qt.AlignLeft)

    def textToCenter(self):
        print("text to center")
        self.textToLeftButton.setChecked(False)
        self.textToRightButton.setChecked(False)
        self.justifyTextButton.setChecked(False)
        self.textEdit.setAlignment(Qt.AlignCenter)

    def textToRight(self):
        print("text to right")
        self.textToLeftButton.setChecked(False)
        self.textToCenterButton.setChecked(False)
        self.justifyTextButton.setChecked(False)
        self.textEdit.setAlignment(Qt.AlignRight)

    def textJustify(self):
        print("text justify")
        self.textToLeftButton.setChecked(False)
        self.textToCenterButton.setChecked(False)
        self.textToRightButton.setChecked(False)
        self.textEdit.setAlignment(Qt.AlignJustify)

    def changeFontColor(self):
        print("change font color")
        color = QColorDialog.getColor()
        if color == QtGui.QColor():
            return

        self.colorRect.setStyleSheet("background-color:" + color.name())
        self.textEdit.setTextColor(color.name())

    def changeFont(self):
        print("change font")
        fontname = self.fontCombobox.currentFont().family()
        self.textEdit.setFontFamily(fontname)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()


