# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task3GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import numpy as np
from playsound import playsound
from PyQt5 import QtCore, QtGui, QtWidgets
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
from PyQt5.QtGui import QColor ,QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyqtgraph.graphicsItems.ScatterPlotItem import Symbols
from pyqtgraph.graphicsItems.ImageItem import ImageItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import cv2
import io
from numpy.fft import fft, fftfreq, ifft
from scipy.fftpack import fft, ifft
from scipy import signal
import cmath
from scipy.io.wavfile import write


from PyQt5 import QtCore, QtGui, QtWidgets 
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_5)
        self.layoutWidget_3.setGeometry(QtCore.QRect(2, 0, 802, 518))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.layoutWidget_3)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 300))
        self.widget_3.setObjectName("widget_3")
        self.splitter_3 = QtWidgets.QSplitter(self.widget_3)
        self.splitter_3.setGeometry(QtCore.QRect(0, 10, 761, 291))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.MainGraph_3 = QtWidgets.QWidget(self.splitter_3)
        self.MainGraph_3.setMinimumSize(QtCore.QSize(400, 0))
        self.MainGraph_3.setObjectName("MainGraph_3")
        self.MainSpectroControls_3 = QtWidgets.QWidget(self.splitter_3)
        self.MainSpectroControls_3.setMinimumSize(QtCore.QSize(60, 0))
        self.MainSpectroControls_3.setMaximumSize(QtCore.QSize(65, 16777215))
        self.MainSpectroControls_3.setObjectName("MainSpectroControls_3")
        self.MainControl_3 = QtWidgets.QToolBox(self.MainSpectroControls_3)
        self.MainControl_3.setGeometry(QtCore.QRect(0, 2, 69, 281))
        self.MainControl_3.setObjectName("MainControl_3")
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setGeometry(QtCore.QRect(0, 0, 69, 219))
        self.page_13.setObjectName("page_13")
        self.SpectroButton_3 = QtWidgets.QPushButton(self.page_13)
        self.SpectroButton_3.setGeometry(QtCore.QRect(0, 20, 61, 23))
        self.SpectroButton_3.setObjectName("SpectroButton_3")
        self.PlayButton_3 = QtWidgets.QPushButton(self.page_13)
        self.PlayButton_3.setGeometry(QtCore.QRect(0, 60, 61, 23))
        self.PlayButton_3.setObjectName("PlayButton_3")
        self.OpenFileButton_3 = QtWidgets.QPushButton(self.page_13)
        self.OpenFileButton_3.setGeometry(QtCore.QRect(0, 0, 61, 23))
        self.OpenFileButton_3.setStyleSheet("radius:\"3\";")
        self.OpenFileButton_3.setObjectName("OpenFileButton_3")
        self.PauseButton_3 = QtWidgets.QPushButton(self.page_13)
        self.PauseButton_3.setGeometry(QtCore.QRect(0, 80, 61, 23))
        self.PauseButton_3.setObjectName("PauseButton_3")
        self.FasterButton_3 = QtWidgets.QPushButton(self.page_13)
        self.FasterButton_3.setGeometry(QtCore.QRect(0, 140, 61, 23))
        self.FasterButton_3.setObjectName("FasterButton_3")
        self.SlowerButton_3 = QtWidgets.QPushButton(self.page_13)
        self.SlowerButton_3.setGeometry(QtCore.QRect(0, 120, 61, 23))
        self.SlowerButton_3.setObjectName("SlowerButton_3")
        self.ZoomInButton_3 = QtWidgets.QPushButton(self.page_13)
        self.ZoomInButton_3.setGeometry(QtCore.QRect(0, 180, 61, 23))
        self.ZoomInButton_3.setObjectName("ZoomInButton_3")
        self.ZoomOutButton_3 = QtWidgets.QPushButton(self.page_13)
        self.ZoomOutButton_3.setGeometry(QtCore.QRect(0, 200, 61, 23))
        self.ZoomOutButton_3.setObjectName("ZoomOutButton_3")
        self.MainControl_3.addItem(self.page_13, "")
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_14.setObjectName("page_14")
        self.AudioVolumeSlider_3 = QtWidgets.QSlider(self.page_14)
        self.AudioVolumeSlider_3.setGeometry(QtCore.QRect(20, 20, 22, 61))
        self.AudioVolumeSlider_3.setMaximum(10)
        self.AudioVolumeSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.AudioVolumeSlider_3.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.AudioVolumeSlider_3.setTickInterval(1)
        self.AudioVolumeSlider_3.setObjectName("AudioVolumeSlider_3")
        self.MainVolumeLabel_3 = QtWidgets.QLabel(self.page_14)
        self.MainVolumeLabel_3.setGeometry(QtCore.QRect(10, -10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.MainVolumeLabel_3.setFont(font)
        self.MainVolumeLabel_3.setObjectName("MainVolumeLabel_3")
        self.SpectroLabel_3 = QtWidgets.QLabel(self.page_14)
        self.SpectroLabel_3.setGeometry(QtCore.QRect(10, 90, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SpectroLabel_3.setFont(font)
        self.SpectroLabel_3.setObjectName("SpectroLabel_3")
        self.PaletteComboBox_3 = QtWidgets.QComboBox(self.page_14)
        self.PaletteComboBox_3.setGeometry(QtCore.QRect(0, 120, 61, 22))
        self.PaletteComboBox_3.setObjectName("PaletteComboBox_3")
        self.PaletteComboBox_3.addItem("")
        self.Spec_minSLider_3 = QtWidgets.QSlider(self.page_14)
        self.Spec_minSLider_3.setGeometry(QtCore.QRect(0, 162, 61, 20))
        self.Spec_minSLider_3.setMaximum(255)
        self.Spec_minSLider_3.setOrientation(QtCore.Qt.Horizontal)
        self.Spec_minSLider_3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Spec_minSLider_3.setObjectName("Spec_minSLider_3")
        self.Spec_MaxSlider_3 = QtWidgets.QSlider(self.page_14)
        self.Spec_MaxSlider_3.setGeometry(QtCore.QRect(0, 202, 61, 20))
        self.Spec_MaxSlider_3.setMaximum(255)
        self.Spec_MaxSlider_3.setTracking(True)
        self.Spec_MaxSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.Spec_MaxSlider_3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Spec_MaxSlider_3.setObjectName("Spec_MaxSlider_3")
        self.MainControl_3.addItem(self.page_14, "")
        self.SpectroChannel_3 = QtWidgets.QWidget(self.splitter_3)
        self.SpectroChannel_3.setObjectName("SpectroChannel_3")
        self.verticalLayout_3.addWidget(self.widget_3)
        self.Equalizer_5 = QtWidgets.QWidget(self.layoutWidget_3)
        self.Equalizer_5.setObjectName("Equalizer_5")
        self.EqualizerControl_3 = QtWidgets.QToolBox(self.Equalizer_5)
        self.EqualizerControl_3.setGeometry(QtCore.QRect(10, 20, 91, 171))
        self.EqualizerControl_3.setObjectName("EqualizerControl_3")
        self.page_21 = QtWidgets.QWidget()
        self.page_21.setGeometry(QtCore.QRect(0, 0, 91, 109))
        self.page_21.setObjectName("page_21")
        self.ImageOFInstHolder_3 = QtWidgets.QLabel(self.page_21)
        self.ImageOFInstHolder_3.setGeometry(QtCore.QRect(6, 2, 81, 111))
        self.ImageOFInstHolder_3.setObjectName("ImageOFInstHolder_3")
        self.EqualizerControl_3.addItem(self.page_21, "")
        self.page_22 = QtWidgets.QWidget()
        self.page_22.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_22.setObjectName("page_22")
        self.Instrument_8 = QtWidgets.QPushButton(self.page_22)
        self.Instrument_8.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.Instrument_8.setObjectName("Instrument_8")
        self.Instrument_9 = QtWidgets.QPushButton(self.page_22)
        self.Instrument_9.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.Instrument_9.setObjectName("Instrument_9")
        self.Instrument_10 = QtWidgets.QPushButton(self.page_22)
        self.Instrument_10.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.Instrument_10.setObjectName("Instrument_10")
        self.EqualizerControl_3.addItem(self.page_22, "")
        self.EqualizerVolume_3 = QtWidgets.QSlider(self.Equalizer_5)
        self.EqualizerVolume_3.setGeometry(QtCore.QRect(180, 20, 22, 141))
        self.EqualizerVolume_3.setMaximum(10)
        self.EqualizerVolume_3.setOrientation(QtCore.Qt.Vertical)
        self.EqualizerVolume_3.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.EqualizerVolume_3.setObjectName("EqualizerVolume_3")
        self.EqualizerGain_3 = QtWidgets.QSlider(self.Equalizer_5)
        self.EqualizerGain_3.setGeometry(QtCore.QRect(280, 20, 22, 141))
        self.EqualizerGain_3.setMaximum(10)
        self.EqualizerGain_3.setOrientation(QtCore.Qt.Vertical)
        self.EqualizerGain_3.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.EqualizerGain_3.setObjectName("EqualizerGain_3")
        self.verticalSlider_24 = QtWidgets.QSlider(self.Equalizer_5)
        self.verticalSlider_24.setGeometry(QtCore.QRect(380, 20, 22, 141))
        self.verticalSlider_24.setMaximum(10)
        self.verticalSlider_24.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_24.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_24.setObjectName("verticalSlider_24")
        self.verticalSlider_25 = QtWidgets.QSlider(self.Equalizer_5)
        self.verticalSlider_25.setGeometry(QtCore.QRect(480, 20, 22, 141))
        self.verticalSlider_25.setMaximum(10)
        self.verticalSlider_25.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_25.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_25.setObjectName("verticalSlider_25")
        self.verticalSlider_26 = QtWidgets.QSlider(self.Equalizer_5)
        self.verticalSlider_26.setGeometry(QtCore.QRect(580, 20, 22, 141))
        self.verticalSlider_26.setMaximum(10)
        self.verticalSlider_26.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_26.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_26.setObjectName("verticalSlider_26")
        self.verticalSlider_27 = QtWidgets.QSlider(self.Equalizer_5)
        self.verticalSlider_27.setGeometry(QtCore.QRect(680, 20, 22, 141))
        self.verticalSlider_27.setMaximum(10)
        self.verticalSlider_27.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_27.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_27.setObjectName("verticalSlider_27")
        self.VolumeLabel_19 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_19.setGeometry(QtCore.QRect(170, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_19.setFont(font)
        self.VolumeLabel_19.setObjectName("VolumeLabel_19")
        self.VolumeLabel_20 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_20.setGeometry(QtCore.QRect(280, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_20.setFont(font)
        self.VolumeLabel_20.setObjectName("VolumeLabel_20")
        self.VolumeLabel_21 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_21.setGeometry(QtCore.QRect(380, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_21.setFont(font)
        self.VolumeLabel_21.setObjectName("VolumeLabel_21")
        self.Equalizer_6 = QtWidgets.QWidget(self.Equalizer_5)
        self.Equalizer_6.setGeometry(QtCore.QRect(420, 180, 800, 210))
        self.Equalizer_6.setObjectName("Equalizer_6")
        self.verticalSlider_28 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider_28.setGeometry(QtCore.QRect(180, 20, 22, 141))
        self.verticalSlider_28.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_28.setObjectName("verticalSlider_28")
        self.verticalSlider_29 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider_29.setGeometry(QtCore.QRect(280, 20, 22, 141))
        self.verticalSlider_29.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_29.setObjectName("verticalSlider_29")
        self.verticalSlider_30 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider_30.setGeometry(QtCore.QRect(380, 20, 22, 141))
        self.verticalSlider_30.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_30.setObjectName("verticalSlider_30")
        self.verticalSlider_31 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider_31.setGeometry(QtCore.QRect(480, 20, 22, 141))
        self.verticalSlider_31.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_31.setObjectName("verticalSlider_31")
        self.verticalSlider_32 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider_32.setGeometry(QtCore.QRect(580, 20, 22, 141))
        self.verticalSlider_32.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_32.setObjectName("verticalSlider_32")
        self.verticalSlider_33 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider_33.setGeometry(QtCore.QRect(680, 20, 22, 141))
        self.verticalSlider_33.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_33.setObjectName("verticalSlider_33")
        self.VolumeLabel_22 = QtWidgets.QLabel(self.Equalizer_6)
        self.VolumeLabel_22.setGeometry(QtCore.QRect(170, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_22.setFont(font)
        self.VolumeLabel_22.setObjectName("VolumeLabel_22")
        self.VolumeLabel_23 = QtWidgets.QLabel(self.Equalizer_6)
        self.VolumeLabel_23.setGeometry(QtCore.QRect(280, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_23.setFont(font)
        self.VolumeLabel_23.setObjectName("VolumeLabel_23")
        self.VolumeLabel_24 = QtWidgets.QLabel(self.Equalizer_6)
        self.VolumeLabel_24.setGeometry(QtCore.QRect(380, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_24.setFont(font)
        self.VolumeLabel_24.setObjectName("VolumeLabel_24")
        self.VolumeLabel_25 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_25.setGeometry(QtCore.QRect(470, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_25.setFont(font)
        self.VolumeLabel_25.setObjectName("VolumeLabel_25")
        self.VolumeLabel_26 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_26.setGeometry(QtCore.QRect(570, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_26.setFont(font)
        self.VolumeLabel_26.setObjectName("VolumeLabel_26")
        self.VolumeLabel_27 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_27.setGeometry(QtCore.QRect(670, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_27.setFont(font)
        self.VolumeLabel_27.setObjectName("VolumeLabel_27")
        self.verticalLayout_3.addWidget(self.Equalizer_5)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_6)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 0, 941, 591))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_19 = QtWidgets.QWidget()
        self.page_19.setObjectName("page_19")
        self.piano = QtWidgets.QPushButton(self.page_19)
        self.piano.setGeometry(QtCore.QRect(60, 20, 231, 241))
        self.piano.setText("")
        self.piano.setObjectName("piano")
        self.textEdit = QtWidgets.QTextEdit(self.page_19)
        self.textEdit.setGeometry(QtCore.QRect(360, 230, 241, 71))
        self.textEdit.setObjectName("textEdit")
        self.drums = QtWidgets.QPushButton(self.page_19)
        self.drums.setGeometry(QtCore.QRect(360, 340, 231, 241))
        self.drums.setText("")
        self.drums.setObjectName("drums")
        self.bongos = QtWidgets.QPushButton(self.page_19)
        self.bongos.setGeometry(QtCore.QRect(670, 20, 231, 241))
        self.bongos.setText("")
        self.bongos.setObjectName("bongos")
        self.stackedWidget.addWidget(self.page_19)
        self.page_20 = QtWidgets.QWidget()
        self.page_20.setObjectName("page_20")
        self.label = QtWidgets.QLabel(self.page_20)
        self.label.setGeometry(QtCore.QRect(200, 200, 461, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../pianoplay2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.page_20)
        self.pushButton.setGeometry(QtCore.QRect(200, 360, 31, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 360, 31, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_6.setGeometry(QtCore.QRect(300, 360, 31, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 360, 31, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_8.setGeometry(QtCore.QRect(390, 360, 31, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_9.setGeometry(QtCore.QRect(440, 360, 31, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_10.setGeometry(QtCore.QRect(480, 360, 31, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_11.setGeometry(QtCore.QRect(530, 360, 31, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_12.setGeometry(QtCore.QRect(580, 360, 31, 28))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_13.setGeometry(QtCore.QRect(620, 360, 31, 28))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_14.setGeometry(QtCore.QRect(230, 280, 31, 28))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_15.setGeometry(QtCore.QRect(280, 280, 31, 28))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_16.setGeometry(QtCore.QRect(370, 280, 31, 28))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_17.setGeometry(QtCore.QRect(420, 280, 31, 28))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_18.setGeometry(QtCore.QRect(550, 280, 31, 28))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_19.setGeometry(QtCore.QRect(460, 280, 31, 28))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_20.setGeometry(QtCore.QRect(600, 280, 31, 28))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page_20)
        self.page_23 = QtWidgets.QWidget()
        self.page_23.setObjectName("page_23")
        self.label_2 = QtWidgets.QLabel(self.page_23)
        self.label_2.setGeometry(QtCore.QRect(190, 130, 421, 281))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_23)
        self.label_3.setGeometry(QtCore.QRect(160, 150, 531, 291))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../bangos1.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_21 = QtWidgets.QPushButton(self.page_23)
        self.pushButton_21.setGeometry(QtCore.QRect(540, 210, 31, 28))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.page_23)
        self.pushButton_22.setGeometry(QtCore.QRect(270, 200, 31, 28))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_23)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget.addWidget(self.page_23)
        self.page_24 = QtWidgets.QWidget()
        self.page_24.setObjectName("page_24")
        self.label_4 = QtWidgets.QLabel(self.page_24)
        self.label_4.setGeometry(QtCore.QRect(150, 120, 671, 391))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../blog-graphics-labeled-drum-kit.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_24 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_24.setGeometry(QtCore.QRect(540, 380, 31, 31))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_27 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_27.setGeometry(QtCore.QRect(580, 240, 31, 31))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_23 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_23.setGeometry(QtCore.QRect(260, 320, 31, 31))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_25 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_25.setGeometry(QtCore.QRect(390, 240, 31, 31))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_28 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_28.setGeometry(QtCore.QRect(660, 320, 31, 31))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_30 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_30.setGeometry(QtCore.QRect(360, 340, 31, 31))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_29 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_29.setGeometry(QtCore.QRect(290, 190, 31, 31))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_26 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_26.setGeometry(QtCore.QRect(480, 250, 31, 31))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_31 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_31.setGeometry(QtCore.QRect(460, 350, 31, 31))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page_24)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.shortcut1 = QShortcut(QKeySequence('A') , self)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.MainControl_3.setCurrentIndex(0)
        self.EqualizerControl_3.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SpectroButton_3.setText(_translate("MainWindow", "Spectro"))
        self.PlayButton_3.setText(_translate("MainWindow", "Play"))
        self.OpenFileButton_3.setText(_translate("MainWindow", "Open File"))
        self.PauseButton_3.setText(_translate("MainWindow", "Pause"))
        self.FasterButton_3.setText(_translate("MainWindow", "Faster"))
        self.SlowerButton_3.setText(_translate("MainWindow", "Slower"))
        self.ZoomInButton_3.setText(_translate("MainWindow", "Zoom in"))
        self.ZoomOutButton_3.setText(_translate("MainWindow", "Zoom out"))
        self.MainControl_3.setItemText(self.MainControl_3.indexOf(self.page_13), _translate("MainWindow", "Page 1"))
        self.MainVolumeLabel_3.setText(_translate("MainWindow", "Volume"))
        self.SpectroLabel_3.setText(_translate("MainWindow", "Spectro"))
        self.PaletteComboBox_3.setItemText(0, _translate("MainWindow", "Palettes"))
        self.MainControl_3.setItemText(self.MainControl_3.indexOf(self.page_14), _translate("MainWindow", "Page 2"))
        self.ImageOFInstHolder_3.setText(_translate("MainWindow", "Image of Instr."))
        self.EqualizerControl_3.setItemText(self.EqualizerControl_3.indexOf(self.page_21), _translate("MainWindow", "Page 1"))
        self.Instrument_8.setText(_translate("MainWindow", "Inst 1"))
        self.Instrument_9.setText(_translate("MainWindow", "Inst 2"))
        self.Instrument_10.setText(_translate("MainWindow", "Inst 3"))
        self.EqualizerControl_3.setItemText(self.EqualizerControl_3.indexOf(self.page_22), _translate("MainWindow", "Page 2"))
        self.VolumeLabel_19.setText(_translate("MainWindow", "Volume"))
        self.VolumeLabel_20.setText(_translate("MainWindow", "Gain"))
        self.VolumeLabel_21.setText(_translate("MainWindow", "Label3"))
        self.VolumeLabel_22.setText(_translate("MainWindow", "Volume"))
        self.VolumeLabel_23.setText(_translate("MainWindow", "Gain"))
        self.VolumeLabel_24.setText(_translate("MainWindow", "Label3"))
        self.VolumeLabel_25.setText(_translate("MainWindow", "Label3"))
        self.VolumeLabel_26.setText(_translate("MainWindow", "Label3"))
        self.VolumeLabel_27.setText(_translate("MainWindow", "Label3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Tab 1"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Choose an instrument to play</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "A"))
        self.pushButton_2.setText(_translate("MainWindow", "S"))
        self.pushButton_6.setText(_translate("MainWindow", "D"))
        self.pushButton_7.setText(_translate("MainWindow", "F"))
        self.pushButton_8.setText(_translate("MainWindow", "G"))
        self.pushButton_9.setText(_translate("MainWindow", "H"))
        self.pushButton_10.setText(_translate("MainWindow", "J"))
        self.pushButton_11.setText(_translate("MainWindow", "K"))
        self.pushButton_12.setText(_translate("MainWindow", "L"))
        self.pushButton_13.setText(_translate("MainWindow", ":"))
        self.pushButton_14.setText(_translate("MainWindow", "E"))
        self.pushButton_15.setText(_translate("MainWindow", "R"))
        self.pushButton_16.setText(_translate("MainWindow", "T"))
        self.pushButton_17.setText(_translate("MainWindow", "Y"))
        self.pushButton_18.setText(_translate("MainWindow", "I"))
        self.pushButton_19.setText(_translate("MainWindow", "U"))
        self.pushButton_20.setText(_translate("MainWindow", "O"))
        self.pushButton_3.setText(_translate("MainWindow", "back to menu"))
        self.pushButton_21.setText(_translate("MainWindow", "W"))
        self.pushButton_22.setText(_translate("MainWindow", "Q"))
        self.pushButton_4.setText(_translate("MainWindow", "back to menu"))
        self.pushButton_24.setText(_translate("MainWindow", "C"))
        self.pushButton_27.setText(_translate("MainWindow", "B"))
        self.pushButton_23.setText(_translate("MainWindow", "Z"))
        self.pushButton_25.setText(_translate("MainWindow", "M"))
        self.pushButton_28.setText(_translate("MainWindow", "V"))
        self.pushButton_30.setText(_translate("MainWindow", "X"))
        self.pushButton_29.setText(_translate("MainWindow", ","))
        self.pushButton_26.setText(_translate("MainWindow", "N"))
        self.pushButton_31.setText(_translate("MainWindow", "/"))
        self.pushButton_5.setText(_translate("MainWindow", "back to menu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Tab 2"))
        self.piano.clicked.connect(lambda: self.pianoPlay())
        self.bongos.clicked.connect(lambda: self.BongosPlay())
        self.drums.clicked.connect(lambda: self.drumsPlay())
        self.pushButton_3.clicked.connect(lambda : self.backToMenu())
        self.pushButton_4.clicked.connect(lambda : self.backToMenu())
        self.pushButton_5.clicked.connect(lambda : self.backToMenu())
        self.piano.setIcon(QtGui.QIcon('piano.jpg'))
        self.piano.setIconSize((QtCore.QSize(453,392)))
        self.bongos.setIcon(QtGui.QIcon('bongos.jpg'))
        self.bongos.setIconSize((QtCore.QSize(231,352)))
        self.drums.setIcon(QtGui.QIcon('drum.jpg'))
        self.drums.setIconSize((QtCore.QSize(493,392)))
        self.pushButton_21.clicked.connect(lambda : self.playRightBango())
        self.pushButton.clicked.connect(lambda: self.playC4())
        self.pushButton_2.clicked.connect(lambda: self.playD4())
        self.pushButton_6.clicked.connect(lambda: self.playE4())
        self.pushButton_7.clicked.connect(lambda: self.playF4())
        self.pushButton_8.clicked.connect(lambda: self.playG4())
        self.pushButton_9.clicked.connect(lambda: self.playA4())
        self.pushButton_10.clicked.connect(lambda: self.playB4())
        self.pushButton_11.clicked.connect(lambda: self.playC5())
        self.pushButton_12.clicked.connect(lambda: self.playD5())
        self.pushButton_13.clicked.connect(lambda: self.playE5())
        self.pushButton_14.clicked.connect(lambda: self.playDb4())
        self.pushButton_15.clicked.connect(lambda: self.playEb4())
        self.pushButton_16.clicked.connect(lambda: self.playGb4())
        self.pushButton_17.clicked.connect(lambda: self.playAb4())
        self.pushButton_19.clicked.connect(lambda:self.playBb4())
        self.pushButton_18.clicked.connect(lambda: self.playDb5())
        self.pushButton_20.clicked.connect(lambda: self.playEb5())
        self.shortcut1.activated.connect(lambda: self.playC4() )
        self.sample_rate = 44100 
        self.duration = 0.5



    def backToMenu(self):
        self.stackedWidget.setCurrentIndex(0)
    def pianoPlay(self):
     self.stackedWidget.setCurrentIndex(1)
     self.note_freqs = self.get_piano_notes()
    def playC4 (self):
        frequency = self.note_freqs['C4']
        C4_wave = self.get_wave(frequency)
        write('C4.wav', self.sample_rate, C4_wave.astype(np.int16))
        playsound('C4.wav')

    def playD4 (self):
        frequency = self.note_freqs['D4']
        D4_wave = self.get_wave(frequency)
        write('D4.wav', self.sample_rate, D4_wave.astype(np.int16))
        playsound('D4.wav')
    def playE4 (self):
            frequency = self.note_freqs['E4']
            E4_wave = self.get_wave(frequency)
            write('E4.wav', self.sample_rate, E4_wave.astype(np.int16))
            playsound('E4.wav')
    def playF4 (self):
            frequency = self.note_freqs['F4']
            F4_wave = self.get_wave(frequency)
            write('F4.wav', self.sample_rate, F4_wave.astype(np.int16))
            playsound('F4.wav')
    def playG4 (self):
            frequency = self.note_freqs['G4']
            G4_wave = self.get_wave(frequency)
            write('G4.wav', self.sample_rate, G4_wave.astype(np.int16))
            playsound('G4.wav')
    def playA4 (self):
            frequency = self.note_freqs['A4']
            A4_wave = self.get_wave(frequency)
            write('A4.wav', self.sample_rate, A4_wave.astype(np.int16))
            playsound('A4.wav')
    def playB4 (self):
            frequency = self.note_freqs['B4']
            B4_wave = self.get_wave(frequency)
            write('B4.wav', self.sample_rate, B4_wave.astype(np.int16))
            playsound('B4.wav')
    def playDb4 (self):
            frequency = self.note_freqs['Db4']
            Db4_wave = self.get_wave(frequency)
            write('Db4.wav', self.sample_rate, Db4_wave.astype(np.int16))
            playsound('Db4.wav')
    def playEb4 (self):
            frequency = self.note_freqs['Eb4']
            Eb4_wave = self.get_wave(frequency)
            write('Eb4.wav', self.sample_rate, Eb4_wave.astype(np.int16))
            playsound('Eb4.wav')
    def playGb4 (self):
            frequency = self.note_freqs['Gb4']
            Gb4_wave = self.get_wave(frequency)
            write('Gb4.wav', self.sample_rate, Gb4_wave.astype(np.int16))
            playsound('Gb4.wav')
    def playAb4 (self):
            frequency = self.note_freqs['Ab4']
            Ab4_wave = self.get_wave(frequency)
            write('Ab4.wav', self.sample_rate, Ab4_wave.astype(np.int16))
            playsound('Ab4.wav')
    def playBb4 (self):
            frequency = self.note_freqs['Bb4']
            Bb4_wave = self.get_wave(frequency)
            write('Bb4.wav', self.sample_rate, Bb4_wave.astype(np.int16))
            playsound('Bb4.wav')
    def playC5 (self):
            frequency = self.note_freqs['C5']
            C5_wave = self.get_wave(frequency)
            write('C5.wav', self.sample_rate, C5_wave.astype(np.int16))
            playsound('C5.wav')
    def playDb5 (self):
            frequency = self.note_freqs['Db5']
            Db5_wave = self.get_wave(frequency)
            write('Db5.wav', self.sample_rate, Db5_wave.astype(np.int16))
            playsound('Db5.wav')
    def playEb5 (self):
            frequency = self.note_freqs['Eb5']
            Eb5_wave = self.get_wave(frequency)
            write('Db5.wav', self.sample_rate, Eb5_wave.astype(np.int16))
            playsound('Eb5.wav')
    def playGb5 (self):
                frequency = self.note_freqs['Gb5']
                Gb5_wave = self.get_wave(frequency)
                write('Gb5.wav', self.sample_rate, Gb5_wave.astype(np.int16))
                playsound('Gb5.wav')
    def playAb5 (self):
                frequency = self.note_freqs['Ab5']
                Ab5_wave = self.get_wave(frequency)
                write('Ab5.wav', self.sample_rate, Ab5_wave.astype(np.int16))
                playsound('Ab5.wav')
    def playBb5 (self):
                frequency = self.note_freqs['Bb5']
                Bb5_wave = self.get_wave(frequency)
                write('Bb5.wav', self.sample_rate, Bb5_wave.astype(np.int16))
                playsound('Bb5.wav')
    
    def get_wave(self ,freq ):
        amplitude = 4096
        t = np.linspace(0 , self.duration , int(self.sample_rate *self.duration))
        wave = amplitude * np.sin(2 * np.pi * freq * t)
        return wave

    def get_piano_notes(self ):
    # Returns a dict object for all the piano 
    # note's frequencies
    # White keys are in Uppercase and black keys (sharps) are in lowercase
        octave = ['C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4' , 'C5' ,'Db5' , 'D5' , 'Eb5' , 'E5'] 
        base_freq = 261.63 #Frequency of Note C4
        freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))}       
        
        return freqs
    def BongosPlay(self):
        self.stackedWidget.setCurrentIndex(2)

    def drumsPlay(self):
        self.stackedWidget.setCurrentIndex(3)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())