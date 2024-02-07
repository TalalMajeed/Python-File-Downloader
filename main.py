from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import threading
import os
from pathlib import Path
from urllib.parse import urlparse

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 798)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.mainGroup.setMinimumSize(QtCore.QSize(500, 500))
        self.mainGroup.setMaximumSize(QtCore.QSize(800, 600))
        self.mainGroup.setStyleSheet("font-family: \"Century Gothic\";\n"
"background-color: \"white\";")
        self.mainGroup.setTitle("")
        self.mainGroup.setObjectName("mainGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.mainGroup)
        self.label.setStyleSheet("font-size: 30px;\n"
"font-weight: 800;\n"
"color: rgb(15, 123, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.groupBox = QtWidgets.QGroupBox(self.mainGroup)
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(140, 0))
        self.label_2.setStyleSheet("font-size: 18px;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.linkInput = QtWidgets.QLineEdit(self.groupBox)
        self.linkInput.setStyleSheet("border: 1px solid rgb(15, 123, 255);\n"
"font-size: 20px;\n"
"padding: 5px 10px 5px 10px;")
        self.linkInput.setObjectName("linkInput")
        self.horizontalLayout.addWidget(self.linkInput)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.mainGroup)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setMinimumSize(QtCore.QSize(140, 0))
        self.label_4.setStyleSheet("font-size: 18px;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.fileOutput = QtWidgets.QLineEdit(self.groupBox_2)
        self.fileOutput.setStyleSheet("border: 1px solid rgb(15, 123, 255);\n"
"font-size: 20px;\n"
"padding: 5px 10px 5px 10px;")
        self.fileOutput.setObjectName("fileOutput")
        self.horizontalLayout_3.addWidget(self.fileOutput)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.mainGroup)
        self.groupBox_4.setStyleSheet("")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.StartButton = QtWidgets.QPushButton(self.groupBox_4)
        self.StartButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(15, 123, 255);\n"
"color: white;\n"
"font-family: \"Century Gothic\";\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"outline: none;\n"
"border: 1px solid  rgb(15, 123, 255);\n"
"padding: 10px;\n"
"margin-right: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: white;\n"
"color: rgb(15, 123, 255);\n"
"}")
        self.StartButton.setObjectName("StartButton")
        self.horizontalLayout_5.addWidget(self.StartButton)
        self.PauseButton = QtWidgets.QPushButton(self.groupBox_4)
        self.PauseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PauseButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(15, 123, 255);\n"
"color: white;\n"
"font-family: \"Century Gothic\";\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"outline: none;\n"
"border: 1px solid  rgb(15, 123, 255);\n"
"padding: 10px;\n"
"margin-left: 5px;\n"
"margin-right: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: white;\n"
"color: rgb(15, 123, 255);\n"
"}")
        self.PauseButton.setObjectName("PauseButton")
        self.horizontalLayout_5.addWidget(self.PauseButton)
        self.ResetButton = QtWidgets.QPushButton(self.groupBox_4)
        self.ResetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ResetButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(15, 123, 255);\n"
"color: white;\n"
"font-family: \"Century Gothic\";\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"outline: none;\n"
"border: 1px solid  rgb(15, 123, 255);\n"
"padding: 10px;\n"
"margin-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: white;\n"
"color: rgb(15, 123, 255);\n"
"}")
        self.ResetButton.setObjectName("ResetButton")
        self.horizontalLayout_5.addWidget(self.ResetButton)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.mainGroup)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setMinimumSize(QtCore.QSize(140, 0))
        self.label_5.setStyleSheet("font-size: 18px;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_4.addWidget(self.progressBar)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_5 = QtWidgets.QGroupBox(self.mainGroup)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setMinimumSize(QtCore.QSize(140, 0))
        self.label_7.setMaximumSize(QtCore.QSize(140, 16777215))
        self.label_7.setStyleSheet("font-size: 18px;")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.StatusLabel = QtWidgets.QLabel(self.groupBox_5)
        self.StatusLabel.setMinimumSize(QtCore.QSize(140, 0))
        self.StatusLabel.setStyleSheet("font-size: 18px;")
        self.StatusLabel.setObjectName("StatusLabel")
        self.horizontalLayout_6.addWidget(self.StatusLabel)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.gridLayout.addWidget(self.mainGroup, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "File Downloader"))
        self.label_2.setText(_translate("MainWindow", "Link to File"))
        self.linkInput.setPlaceholderText(_translate("MainWindow", "Enter File Link"))
        self.label_4.setText(_translate("MainWindow", "Save Location"))
        self.fileOutput.setPlaceholderText(_translate("MainWindow", "Enter Save Location"))
        username = Path(os.path.expanduser("~")) / "Downloads"
        self.fileOutput.setText(f"{username}")
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.PauseButton.setText(_translate("MainWindow", "Pause"))
        self.ResetButton.setText(_translate("MainWindow", "Reset"))
        self.label_5.setText(_translate("MainWindow", "Progress"))
        self.label_7.setText(_translate("MainWindow", "Status"))
        self.StatusLabel.setText(_translate("MainWindow", "Not Started"))

        self.StartButton.clicked.connect(self.startDownload)

    def startDownload(self):
        self.StatusLabel.setText("Downloading...")
        self.progressBar.setValue(0)
        self.downloadThread = threading.Thread(target=self.downloadFile)
        self.downloadThread.start()

    def downloadFile(self):
        url = self.linkInput.text()
        file_path = self.fileOutput.text()
        response = requests.get(url, stream=True)
        file_size = int(response.headers.get('content-length', 0))
        fileName = os.path.basename(urlparse(url).path)

        base, ext = os.path.splitext(fileName)
        count = 1
        newName = fileName
        while os.path.exists(file_path + "\\" + newName):
            newName = f"{base} ({count}){ext}"
            count += 1

        with open(file_path + "\\" + newName, 'wb') as file:
            chunk_size = 1024
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                if file_size != 0:
                    self.progressBar.setValue(min(100, self.progressBar.value() + int(chunk_size * 100 / file_size)))

        self.StatusLabel.setText("Downloaded")
        self.progressBar.setValue(100)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
