# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIYaRab2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from pyqtgraph import PlotWidget
import pyqtgraph
from PyQt5 import QtCore, QtGui, QtWidgets
#from matplotlib.pyplot import draw
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QColorDialog, QFileDialog, QFrame, QWidget, QInputDialog, QLineEdit,QComboBox
import os
import numpy as np
from PyQt5.QtWidgets import QMessageBox
import sys 
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor




class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1384, 696)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphCh1 = PlotWidget(self.centralwidget)
        self.graphCh1.setGeometry(QtCore.QRect(10, 40, 801, 221))
        self.graphCh1.setObjectName("graphCh1")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.graphCh1)
        self.verticalScrollBar.setGeometry(QtCore.QRect(780, 0, 20, 221))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.graphCh2 = PlotWidget(self.centralwidget)
        self.graphCh2.setGeometry(QtCore.QRect(10, 370, 801,221))
        self.graphCh2.setObjectName("graphCh2")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.graphCh2)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(780, 0, 20, 221))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.spectrogram = PlotWidget(self.centralwidget)
        self.spectrogram.setGeometry(QtCore.QRect(870, 40, 411, 421))
        self.spectrogram.setObjectName("spectrogram")
        self.playButtonCh1 = QtWidgets.QPushButton(self.centralwidget)
        self.playButtonCh1.setGeometry(QtCore.QRect(10, 300, 75, 23))
        self.playButtonCh1.setObjectName("playButtonCh1")
        self.zoomInButtonCh1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomInButtonCh1.setGeometry(QtCore.QRect(170, 300, 75, 23))
        self.zoomInButtonCh1.setObjectName("zoomInButtonCh1")
        self.zoomOutButtonCh1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOutButtonCh1.setGeometry(QtCore.QRect(250, 300, 75, 23))
        self.zoomOutButtonCh1.setObjectName("zoomOutButtonCh1")
        self.stopButtonCh1 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButtonCh1.setGeometry(QtCore.QRect(330, 300, 75, 23))
        self.stopButtonCh1.setObjectName("stopButtonCh1")
        self.playButtonCh2 = QtWidgets.QPushButton(self.centralwidget)
        self.playButtonCh2.setGeometry(QtCore.QRect(10, 610, 75, 23))
        self.playButtonCh2.setObjectName("playButtonCh2")
        self.zoomInButtonCh2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomInButtonCh2.setGeometry(QtCore.QRect(170, 610, 75, 23))
        self.zoomInButtonCh2.setObjectName("zoomInButtonCh2")
        self.zoomOutButtonCh2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOutButtonCh2.setGeometry(QtCore.QRect(250, 610, 75, 23))
        self.zoomOutButtonCh2.setObjectName("zoomOutButtonCh2")
        self.stopButtonCh2 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButtonCh2.setGeometry(QtCore.QRect(330, 610, 75, 23))
        self.stopButtonCh2.setObjectName("stopButtonCh2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 5, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 330, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(960, 5, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pauseButtonCh1 = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButtonCh1.setGeometry(QtCore.QRect(90, 300, 75, 23))
        self.pauseButtonCh1.setObjectName("pauseButtonCh1")
        self.pauseButtonCh2 = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButtonCh2.setGeometry(QtCore.QRect(90, 610, 75, 23))
        self.pauseButtonCh2.setObjectName("pauseButtonCh2")
        self.slowerButtonCh1 = QtWidgets.QPushButton(self.centralwidget)
        self.slowerButtonCh1.setGeometry(QtCore.QRect(410, 300, 75, 23))
        self.slowerButtonCh1.setObjectName("slowerButtonCh1")
        self.fasterButtonCh1 = QtWidgets.QPushButton(self.centralwidget)
        self.fasterButtonCh1.setGeometry(QtCore.QRect(490, 300, 75, 23))
        self.fasterButtonCh1.setObjectName("fasterButtonCh1")
        self.slowerButtonCh2 = QtWidgets.QPushButton(self.centralwidget)
        self.slowerButtonCh2.setGeometry(QtCore.QRect(410, 610, 75, 23))
        self.slowerButtonCh2.setObjectName("slowerButtonCh2")
        self.fasterButtonCh2 = QtWidgets.QPushButton(self.centralwidget)
        self.fasterButtonCh2.setGeometry(QtCore.QRect(490, 610, 75, 23))
        self.fasterButtonCh2.setObjectName("fasterButtonCh2")
        self.showButtonCh1 = QtWidgets.QPushButton(self.centralwidget)
        self.showButtonCh1.setGeometry(QtCore.QRect(570, 300, 75, 23))
        self.showButtonCh1.setObjectName("showButtonCh1")
        self.hideButtonCh1 = QtWidgets.QPushButton(self.centralwidget)
        self.hideButtonCh1.setGeometry(QtCore.QRect(650, 300, 75, 23))
        self.hideButtonCh1.setObjectName("hideButtonCh1")
        self.showButtonCh2 = QtWidgets.QPushButton(self.centralwidget)
        self.showButtonCh2.setGeometry(QtCore.QRect(570, 610, 75, 23))
        self.showButtonCh2.setObjectName("showButtonCh2")
        self.hideButtonCh2 = QtWidgets.QPushButton(self.centralwidget)
        self.hideButtonCh2.setGeometry(QtCore.QRect(650, 610, 75, 23))
        self.hideButtonCh2.setObjectName("hideButtonCh2")
        self.spectroMinSlider = QtWidgets.QSlider(self.centralwidget)
        self.spectroMinSlider.setGeometry(QtCore.QRect(870, 500, 160, 22))
        self.spectroMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.spectroMinSlider.setObjectName("spectroMinSlider")
        self.spectroMinSlider.setMinimum(0)
        self.spectroMinSlider.setMaximum(5000)
        self.spectroMinSlider.setSingleStep(100)
        self.spectroMaxSlider = QtWidgets.QSlider(self.centralwidget)
        self.spectroMaxSlider.setGeometry(QtCore.QRect(1120, 500, 160, 22))
        self.spectroMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.spectroMaxSlider.setObjectName("spectroMaxSlider")
        self.spectroMaxSlider.setMinimum(5001)
        self.spectroMaxSlider.setMaximum(10000)
        self.spectroMaxSlider.setSingleStep(100)
        self.spectroComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.spectroComboBox.setGeometry(QtCore.QRect(1030, 540, 81, 22))
        self.spectroComboBox.setObjectName("spectroComboBox")
        self.spectroComboBox.addItem("")
        self.spectroComboBox.addItem("")
        self.spectroComboBox.addItem("")
        self.compareButtonCh1 = QtWidgets.QPushButton(self.centralwidget)
        self.compareButtonCh1.setGeometry(QtCore.QRect(730, 300, 75, 23))
        self.compareButtonCh1.setObjectName("compareButtonCh1")
        self.compareButtonCh2 = QtWidgets.QPushButton(self.centralwidget)
        self.compareButtonCh2.setGeometry(QtCore.QRect(730, 610, 75, 23))
        self.compareButtonCh2.setObjectName("compareButtonCh2")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1384, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        self.menuSave_as = QtWidgets.QMenu(self.menuFile)
        self.menuSave_as.setObjectName("menuSave_as")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuChannel_1 = QtWidgets.QMenu(self.menuActions)
        self.menuChannel_1.setObjectName("menuChannel_1")
        self.menuChannel_2 = QtWidgets.QMenu(self.menuActions)
        self.menuChannel_2.setObjectName("menuChannel_2")
        self.menuSpectrogram_Actions = QtWidgets.QMenu(self.menubar)
        self.menuSpectrogram_Actions.setObjectName("menuSpectrogram_Actions")
        self.menuColor_Palettes = QtWidgets.QMenu(self.menuSpectrogram_Actions)
        self.menuColor_Palettes.setObjectName("menuColor_Palettes")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menuOpen_Ch1 = QtWidgets.QAction(mainWindow)
        self.menuOpen_Ch1.setObjectName("menuOpen_Ch1")
        self.menuOpen_Ch2 = QtWidgets.QAction(mainWindow)
        self.menuOpen_Ch2.setObjectName("menuOpen_Ch2")
        self.actionaddTitle1 = QtWidgets.QAction(mainWindow)
        self.actionaddTitle1.setObjectName("addTitle1")
        self.actionaddTitle2 = QtWidgets.QAction(mainWindow)
        self.actionaddTitle2.setObjectName("addTitle2")
        self.menuSave_asImg = QtWidgets.QAction(mainWindow)
        self.menuSave_asImg.setObjectName("menuSave_asImg")
        self.menuSave_asMp4 = QtWidgets.QAction(mainWindow)
        self.menuSave_asMp4.setObjectName("menuSave_asMp4")
        self.actionPlay_Pause = QtWidgets.QAction(mainWindow)
        self.actionPlay_Pause.setObjectName("actionPlay_Pause")
        self.actionZoom_in = QtWidgets.QAction(mainWindow)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QtWidgets.QAction(mainWindow)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionPlay_Pause_2 = QtWidgets.QAction(mainWindow)
        self.actionPlay_Pause_2.setObjectName("actionPlay_Pause_2")
        self.actionZoom_in_2 = QtWidgets.QAction(mainWindow)
        self.actionZoom_in_2.setObjectName("actionZoom_in_2")
        self.actionZoom_out_2 = QtWidgets.QAction(mainWindow)
        self.actionZoom_out_2.setObjectName("actionZoom_out_2")
        self.actionStop = QtWidgets.QAction(mainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionSpectro = QtWidgets.QAction(mainWindow)
        self.actionSpectro.setObjectName("actionSpectro")
        self.actionPlay_Pause_3 = QtWidgets.QAction(mainWindow)
        self.actionPlay_Pause_3.setObjectName("actionPlay_Pause_3")
        self.actionZoom_in_3 = QtWidgets.QAction(mainWindow)
        self.actionZoom_in_3.setObjectName("actionZoom_in_3")
        self.actionZoom_out_3 = QtWidgets.QAction(mainWindow)
        self.actionZoom_out_3.setObjectName("actionZoom_out_3")
        self.actionStop_2 = QtWidgets.QAction(mainWindow)
        self.actionStop_2.setObjectName("actionStop_2")
        self.actionSpectro_2 = QtWidgets.QAction(mainWindow)
        self.actionSpectro_2.setObjectName("actionSpectro_2")
        self.actionExit_App = QtWidgets.QAction(mainWindow)
        self.actionExit_App.setObjectName("actionExit_App")
        self.actionExit = QtWidgets.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionShow_Hide = QtWidgets.QAction(mainWindow)
        self.actionShow_Hide.setObjectName("actionShow_Hide")
        self.actionChange_Color = QtWidgets.QAction(mainWindow)
        self.actionChange_Color.setObjectName("actionChange_Color")
        self.actionShow_Hide_2 = QtWidgets.QAction(mainWindow)
        self.actionShow_Hide_2.setObjectName("actionShow_Hide_2")
        self.actionChange_Color_2 = QtWidgets.QAction(mainWindow)
        self.actionChange_Color_2.setObjectName("actionChange_Color_2")
        self.actionSpeed_Options = QtWidgets.QAction(mainWindow)
        self.actionSpeed_Options.setObjectName("actionSpeed_Options")
        self.actionFull_Window = QtWidgets.QAction(mainWindow)
        self.actionFull_Window.setObjectName("actionFull_Window")
        self.actionPalette_1 = QtWidgets.QAction(mainWindow)
        self.actionPalette_1.setObjectName("actionPalette_1")
        self.actionPalette_2 = QtWidgets.QAction(mainWindow)
        self.actionPalette_2.setObjectName("actionPalette_2")
        self.actionPalette_3 = QtWidgets.QAction(mainWindow)
        self.actionPalette_3.setObjectName("actionPalette_3")
        self.actionPalette_4 = QtWidgets.QAction(mainWindow)
        self.actionPalette_4.setObjectName("actionPalette_4")
        self.actionPalette_5 = QtWidgets.QAction(mainWindow)
        self.actionPalette_5.setObjectName("actionPalette_5")
        self.actionPDF = QtWidgets.QAction(mainWindow)
        self.actionPDF.setObjectName("actionPDF")
        self.actionSpeed_Options_2 = QtWidgets.QAction(mainWindow)
        self.actionSpeed_Options_2.setObjectName("actionSpeed_Options_2")
        self.actionaddTitle = QtWidgets.QAction(mainWindow)
        self.actionaddTitle.setObjectName("actionAdd_Title")
        self.actionaddTitle2 = QtWidgets.QAction(mainWindow)
        self.actionaddTitle2.setObjectName("actionAdd_Title_2")
        self.menuOpen.addAction(self.menuOpen_Ch1)
        self.menuOpen.addAction(self.menuOpen_Ch2)
        self.menuOpen.addAction(self.actionaddTitle1)
        self.menuOpen.addAction(self.actionaddTitle2)
        self.menuSave_as.addAction(self.actionPDF)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.menuSave_as.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuChannel_1.addAction(self.actionChange_Color)
        self.menuChannel_2.addAction(self.actionChange_Color_2)
        self.menuActions.addAction(self.menuChannel_1.menuAction())
        self.menuActions.addAction(self.menuChannel_2.menuAction())
        self.menuColor_Palettes.addAction(self.actionPalette_1)
        self.menuColor_Palettes.addAction(self.actionPalette_2)
        self.menuColor_Palettes.addAction(self.actionPalette_3)
        self.menuColor_Palettes.addAction(self.actionPalette_4)
        self.menuColor_Palettes.addAction(self.actionPalette_5)
        self.menuSpectrogram_Actions.addAction(self.menuColor_Palettes.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuSpectrogram_Actions.menuAction())
        self.colorFrame = QtWidgets.QFrame(self.centralwidget)
        self.colorFrame.setGeometry(QtCore.QRect(330, 240, 120, 80))
        self.colorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.colorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.colorFrame.setObjectName("colorFrame")

        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
        self.timerInterval = 100
        self.penColorIndex1=1
        self.penColorIndex2=1
        self.color = "#ffaa00"
        self.label1 = "CHANNEL 1"
        self.label2 ="CHANNEL 2"
        

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "BioMedical Signal Viewer"))
        self.playButtonCh1.setText(_translate("mainWindow", "Play"))
        self.zoomInButtonCh1.setText(_translate("mainWindow", "Zoom in"))
        self.zoomOutButtonCh1.setText(_translate("mainWindow", "Zoom out"))
        self.stopButtonCh1.setText(_translate("mainWindow", "Stop"))
        self.playButtonCh2.setText(_translate("mainWindow", "Play"))
        self.zoomInButtonCh2.setText(_translate("mainWindow", "Zoom in"))
        self.zoomOutButtonCh2.setText(_translate("mainWindow", "Zoom out"))
        self.stopButtonCh2.setText(_translate("mainWindow", "Stop"))
        self.label.setText(_translate("mainWindow", "channel 1"))
        self.label_2.setText(_translate("mainWindow", "channel 2"))
        self.label_3.setText(_translate("mainWindow", "SPECTROGRAM"))
        self.pauseButtonCh1.setText(_translate("mainWindow", "Pause"))
        self.pauseButtonCh2.setText(_translate("mainWindow", "Pause"))
        self.slowerButtonCh1.setText(_translate("mainWindow", "Slower"))
        self.fasterButtonCh1.setText(_translate("mainWindow", "Faster"))
        self.slowerButtonCh2.setText(_translate("mainWindow", "Slower"))
        self.fasterButtonCh2.setText(_translate("mainWindow", "Faster"))
        self.showButtonCh1.setText(_translate("mainWindow", "Show"))
        self.hideButtonCh1.setText(_translate("mainWindow", "Hide"))
        self.showButtonCh2.setText(_translate("mainWindow", "Show"))
        self.hideButtonCh2.setText(_translate("mainWindow", "Hide"))
        self.spectroComboBox.setItemText(0, _translate("mainWindow", "Spectro"))
        self.spectroComboBox.setItemText(1, _translate("mainWindow", "Ch1"))
        self.spectroComboBox.setItemText(2, _translate("mainWindow", "Ch2"))
        self.compareButtonCh1.setText(_translate("mainWindow", "Compare"))
        self.compareButtonCh2.setText(_translate("mainWindow", "Compare"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuOpen.setTitle(_translate("mainWindow", "Open"))
        self.menuSave_as.setTitle(_translate("mainWindow", "Save as"))
        self.menuActions.setTitle(_translate("mainWindow", "Actions"))
        self.menuChannel_1.setTitle(_translate("mainWindow", "Channel 1"))
        self.menuChannel_2.setTitle(_translate("mainWindow", "Channel 2"))
        self.menuSpectrogram_Actions.setTitle(_translate("mainWindow", "Spectrogram Actions"))
        self.menuColor_Palettes.setTitle(_translate("mainWindow", "Color Palettes"))
        self.menuOpen_Ch1.setText(_translate("mainWindow", "Channel 1"))
        self.menuOpen_Ch2.setText(_translate("mainWindow", "Channel 2"))
        self.actionaddTitle1.setText(_translate("mainWindow", "add Title 1"))
        self.actionaddTitle2.setText(_translate("mainWindow", "add Title 2"))
        self.menuSave_asImg.setText(_translate("mainWindow", "Img"))
        self.menuSave_asMp4.setText(_translate("mainWindow", "mp4"))
        self.actionPlay_Pause.setText(_translate("mainWindow", "Play/Pause"))
        self.actionZoom_in.setText(_translate("mainWindow", "Zoom in"))
        self.actionZoom_out.setText(_translate("mainWindow", "Zoom out"))
        self.actionPlay_Pause_2.setText(_translate("mainWindow", "Play/Pause"))
        self.actionZoom_in_2.setText(_translate("mainWindow", "Zoom in"))
        self.actionZoom_out_2.setText(_translate("mainWindow", "Zoom out"))
        self.actionStop.setText(_translate("mainWindow", "Stop"))
        self.actionSpectro.setText(_translate("mainWindow", "Spectro"))
        self.actionPlay_Pause_3.setText(_translate("mainWindow", "Play/Pause"))
        self.actionZoom_in_3.setText(_translate("mainWindow", "Zoom in"))
        self.actionZoom_out_3.setText(_translate("mainWindow", "Zoom out"))
        self.actionStop_2.setText(_translate("mainWindow", "Stop"))
        self.actionSpectro_2.setText(_translate("mainWindow", "Spectro"))
        self.actionExit_App.setText(_translate("mainWindow", "Exit App"))
        self.actionExit.setText(_translate("mainWindow", "Exit"))
        self.actionChange_Color.setText(_translate("mainWindow", "Change Color"))
        self.actionChange_Color_2.setText(_translate("mainWindow", "Change Color"))
        self.actionSpeed_Options.setText(_translate("mainWindow", "Speed Options"))
        self.actionFull_Window.setText(_translate("mainWindow", "Full Window"))
        self.actionPalette_1.setText(_translate("mainWindow", "Palette 1"))
        self.actionPalette_2.setText(_translate("mainWindow", "Palette 2"))
        self.actionPalette_3.setText(_translate("mainWindow", "Palette 3"))
        self.actionPalette_4.setText(_translate("mainWindow", "Palette 4"))
        self.actionPalette_5.setText(_translate("mainWindow", "Palette 5"))
        self.actionPDF.setText(_translate("mainWindow", "PDF"))
        self.actionSpeed_Options_2.setText(_translate("mainWindow", "Speed Options"))
        self.actionaddTitle.setText(_translate("mainWindow", "Add Title 1"))
        self.actionaddTitle2.setText(_translate("mainWindow", "Add Title 2"))
        self.actionExit.triggered.connect(lambda: self.exitApp())
        self.menuOpen_Ch1.triggered.connect(lambda: self.openFile("ch1"))
        self.menuOpen_Ch2.triggered.connect(lambda: self.openFile("ch2"))
        #self.actionSpectro_Ch_1.triggered.connect(lambda: self.spectro("ch1"))
        #self.actionSpectro_Ch2.triggered.connect(lambda: self.spectro("ch2"))
        self.zoomInButtonCh1.clicked.connect(lambda: self.zoomIn("ch1"))
        self.zoomInButtonCh2.clicked.connect(lambda: self.zoomIn("ch2"))
        self.zoomOutButtonCh1.clicked.connect(lambda: self.zoomOut("ch1"))
        self.zoomOutButtonCh2.clicked.connect(lambda: self.zoomOut("ch2"))
        self.playButtonCh1.clicked.connect(lambda: self.playCh1())
        self.playButtonCh2.clicked.connect(lambda: self.playCh2())
        self.pauseButtonCh1.clicked.connect(lambda: self.pauseCh1())
        self.pauseButtonCh2.clicked.connect(lambda: self.pauseCh2())
        self.stopButtonCh1.clicked.connect(lambda: self.stop("ch1"))
        self.stopButtonCh2.clicked.connect(lambda: self.stop("ch2"))
        self.slowerButtonCh1.clicked.connect(lambda: self.slow("ch1",self.timerInterval))
        self.slowerButtonCh2.clicked.connect(lambda: self.slow("ch2",self.timerInterval))
        self.fasterButtonCh1.clicked.connect(lambda: self.fast("ch1",self.timerInterval))
        self.fasterButtonCh2.clicked.connect(lambda: self.fast("ch2",self.timerInterval))
        self.showButtonCh1.clicked.connect(lambda: self.show("ch1"))
        self.showButtonCh2.clicked.connect(lambda: self.show("ch2"))
        self.hideButtonCh1.clicked.connect(lambda: self.hide("ch1"))
        self.hideButtonCh2.clicked.connect(lambda: self.hide("ch2"))
        self.spectroMaxSlider.valueChanged.connect(lambda: self.maxSlider("value"))
        self.spectroMinSlider.valueChanged.connect(lambda: self.minSlider("value"))
        self.compareButtonCh1.clicked.connect(lambda: self.openFile2("ch1"))
        self.compareButtonCh2.clicked.connect(lambda: self.openFile2("ch2"))
        self.actionChange_Color.triggered.connect(lambda: self.colorPicker())
        self.actionChange_Color_2.triggered.connect(lambda: self.colorPicker())
        self.actionaddTitle1.triggered.connect(lambda: self.addTitle("ch1"))
        self.actionaddTitle2.triggered.connect(lambda: self.addTitle("ch2"))
        self.spectroComboBox.currentTextChanged.connect(lambda: self.comboChanged())
        

    def colorPicker(self):
        self.on_click()

    def comboChanged(self):
        self.spectro(self.spectroComboBox.currentText())



    @pyqtSlot()
    def on_click(self):
        self.openColorDialog()

    def openColorDialog(self):
        color = QColorDialog.getColor()
        self.color=color
        if color.isValid():
            print(color.name())

    def addTitle(self, ch):
        if ch=="ch1":
            self.label.setText(self.label1)
            self.update()
        else:
            self.label_2.setText(self.label2)
            self.update()

    
    def exitApp(self):
        sys.exit()


    def zoomOut(self,ch):
        if ch== "ch1":
            self.graphCh1.plotItem.getViewBox().scaleBy((2,2))
        
        else:
            self.graphCh2.plotItem.getViewBox().scaleBy((2,2))
        
    
    def zoomIn(self,ch):
        if ch== "ch1":
            self.graphCh1.plotItem.getViewBox().scaleBy((0.5,0.5))
        else:
            self.graphCh2.plotItem.getViewBox().scaleBy((0.5,0.5))
  
    def playCh1(self):
        self.timer1.start()

    def playCh2(self):
        self.timer2.start()

    def slow(self,ch,timerInterval):
        self.timerInterval = self.timerInterval * 2
        if ch=="ch1":
            self.timer1.setInterval(self.timerInterval)
        else:
            self.timer2.setInterval(self.timerInterval)

    def fast(self,ch,timerInterval):
        self.timerInterval = self.timerInterval /2
        if ch=="ch1":
            self.timer1.setInterval(self.timerInterval)
        else:
            self.timer2.setInterval(self.timerInterval)

    def show(self,ch):
        if ch== "ch1":
            self.penColorIndex1=1
        else:
            self.penColorIndex2=1

    def hide(self,ch):
        pass
       

    def maxSlider(self,value):
        pass

    def minSlider(self,value):
        pass

    def spectro(self,ch):
        if ch=="Ch1":
            print("hello")
        else:
            print("world")
        
        



    def openFile(self,text):
      """opens a file from the brower """
      file_path=QFileDialog.getOpenFileName()
      file_name=file_path[0].split('/')[-1]
      self.read_data(file_name,text)

    def openFile2(self,text):
      """opens a file from the brower """
      file_path=QFileDialog.getOpenFileName()
      file_name=file_path[0].split('/')[-1]
      self.read_data2(file_name,text)

    def read_data(self,file_name,text):
        """loads the data from chosen file"""
        
        if text=="ch1":
            df1=pd.read_csv(file_name)
            self.label1=file_name
            time1=list(pd.to_numeric(df1['time'],downcast="float"))
            amp1=list(pd.to_numeric(df1['amplitude'],downcast="float"))
            self.draw(time1,amp1,text,self.color)
            
        else:
            df2=pd.read_csv(file_name)
            self.label2=file_name
            time2=list(pd.to_numeric(df2['time'],downcast="float"))
            amp2=list(pd.to_numeric(df2['amplitude'],downcast="float"))
            self.draw(time2,amp2,text,self.color)

    def read_data2(self,file_name,text):
        """loads the data from chosen file"""
        
        if text=="ch1":
            df1=pd.read_csv(file_name)
            time1=list(pd.to_numeric(df1['time'],downcast="float"))
            amp1=list(pd.to_numeric(df1['amplitude'],downcast="float"))
            self.draw2(time1,amp1,text,self.color)
            
        else:
            df2=pd.read_csv(file_name)
            time2=list(pd.to_numeric(df2['time'],downcast="float"))
            amp2=list(pd.to_numeric(df2['amplitude'],downcast="float"))
            self.draw2(time2,amp2,text,self.color)

    
    def draw(self,time,amp,text,color):
        """sets up our canvas to plot"""
        self.time = time
        self.amp=amp
        self.text=text
        self.index=0  

        if self.text=="ch1":
            self.graphCh1.setBackground('w') #background color    
            pen = pyqtgraph.mkPen(color) #signal color
            self.data_line =  self.graphCh1.plot(self.time[0:self.index+500], self.amp[0:self.index+500], pen=pen)
            self.timer1.setInterval(100)
            self.timer1.timeout.connect(lambda:self.update_plot_data(self.time,self.amp))
            self.timer1.start()
                            
        else:
            self.graphCh2.setBackground('w') #background color
            
            pen = pyqtgraph.mkPen(color) #signal color
            self.data_line =  self.graphCh2.plot(self.time[0:self.index+500], self.amp[0:self.index+500], pen=pen)
            self.timer2.setInterval(100)
            self.timer2.timeout.connect(lambda:self.update_plot_data(self.time,self.amp))
            self.timer2.start()



    def draw2(self,time,amp,text,color):
        """sets up our canvas to plot"""
        self.time = time
        self.amp=amp
        self.text=text
        self.index=0  

        if self.text=="ch1":
            self.graphCh1.setBackground('w') #background color
            pen = pyqtgraph.mkPen(color) #signal color
            self.data_line =  self.graphCh1.plot(self.time[self.index:self.index+500], self.amp[self.index:self.index+500], pen=pen)
            self.timer1.setInterval(100)
            self.timer1.timeout.connect(lambda:self.update_plot_data(self.time,self.amp))
            self.timer1.start()
                     
        else:
            
            pen = pyqtgraph.mkPen(color) #signal color
            self.data_line =  self.graphCh2.plot(self.time[self.index:self.index+500], self.amp[self.index:self.index+500], pen=pen)
            self.timer2.setInterval(100)
            self.timer2.timeout.connect(lambda:self.update_plot_data(self.time,self.amp))
            self.timer2.start()


    def update_plot_data(self,time,amp): 
        """updates the data plotted on graph to get dynamic signal"""
        
        dynamic_time = time[0:self.index+500]  
        dynamic_amp = amp[0:self.index+500]
        self.index=self.index+500
    
        if self.index+500>len(time):
            self.index=0

        self.data_line.setData(dynamic_time, dynamic_amp)  # Update the data  


    def pauseCh1(self):
        """pauses the dynamic signal in ch1"""
        self.timer1.stop()  
            
 
    def pauseCh2(self):
        """ pauses the dynamic signal in ch2"""
        self.timer2.stop()        

            
   
    def stop(self,which_channel):
        """Stops the graph from any plots"""
        if which_channel== 'ch1':
            self.graphCh1.clear()  
            
        else:
            self.graphCh2.clear()  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


