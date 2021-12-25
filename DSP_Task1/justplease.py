
# Form implementation generated from reading ui file 'GUIgodhelpus.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import pyqtgraph.exporters
from fpdf import FPDF
import statistics
from pyqtgraph import PlotWidget
import pyqtgraph
from pyqtgraph import *
import pyqtgraph as pg
from pyqtgraph import PlotWidget, PlotItem
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
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyqtgraph.graphicsItems.ScatterPlotItem import Symbols
from pyqtgraph.graphicsItems.ImageItem import ImageItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import cv2
import io

from scipy.signal.spectral import spectrogram
class SpecCanvas(FigureCanvas):

     def __init__(self, parent=None, width=5, height=4, dpi=100):
         fig = Figure(figsize = (width , height) , dpi=dpi)
         self.axes = fig.add_subplot(111)
         super(SpecCanvas, self).__init__(fig)        
         fig.tight_layout()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1384, 696)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1422, 693)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signalComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.signalComboBox.setGeometry(QtCore.QRect(370, 570, 221, 22))
        self.signalComboBox.setObjectName("SignalComboBox")
        self.signalComboBox.addItem("")
        self.signalComboBox.addItem("")
        self.signalComboBox.addItem("")
        self.signalComboBox.addItem("")
        self.pauseButtonCh = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButtonCh.setGeometry(QtCore.QRect(190, 520, 75, 23))
        self.pauseButtonCh.setObjectName("pauseButtonCh")
        self.slowerButtonCh = QtWidgets.QPushButton(self.centralwidget)
        self.slowerButtonCh.setGeometry(QtCore.QRect(510, 520, 75, 23))
        self.slowerButtonCh.setObjectName("slowerButtonCh")
        self.zoomOutButtonCh = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOutButtonCh.setGeometry(QtCore.QRect(350, 520, 75, 23))
        self.zoomOutButtonCh.setObjectName("zoomOutButtonCh")
        self.showButtonCh = QtWidgets.QPushButton(self.centralwidget)
        self.showButtonCh.setGeometry(QtCore.QRect(670, 520, 75, 23))
        self.showButtonCh.setObjectName("showButtonCh")
        self.zoomInButtonCh = QtWidgets.QPushButton(self.centralwidget)
        self.zoomInButtonCh.setGeometry(QtCore.QRect(270, 520, 75, 23))
        self.zoomInButtonCh.setObjectName("zoomInButtonCh")
        self.spectroButtonCh = QtWidgets.QPushButton(self.centralwidget)
        self.spectroButtonCh.setGeometry(QtCore.QRect(430, 520, 75, 23))
        self.spectroButtonCh.setObjectName("spectroButtonCh")
        self.hideButtonCh = QtWidgets.QPushButton(self.centralwidget)
        self.hideButtonCh.setGeometry(QtCore.QRect(750, 520, 75, 23))
        self.hideButtonCh.setObjectName("hideButtonCh")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 520, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 5, 191, 31))
        self.label1.setFont(font)
        self.label1.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 55, 16))
        self.label_2.setObjectName("label_2")

        self.playButtonCh = QtWidgets.QPushButton(self.centralwidget)
        self.playButtonCh.setGeometry(QtCore.QRect(110, 520, 75, 23))
        self.playButtonCh.setObjectName("playButtonCh")
        self.fasterButtonCh = QtWidgets.QPushButton(self.centralwidget)
        self.fasterButtonCh.setGeometry(QtCore.QRect(590, 520, 75, 23))
        self.fasterButtonCh.setObjectName("fasterButtonCh")
        self.addLabelButton = QtWidgets.QPushButton(self.centralwidget)
        self.addLabelButton.setGeometry(QtCore.QRect(830, 520, 75, 23))
        self.addLabelButton.setObjectName("addLabelButton")
        self.spectroMinSlider = QtWidgets.QSlider(self.centralwidget)
        self.spectroMinSlider.setGeometry(QtCore.QRect(990, 480, 160, 22))
        self.spectroMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.spectroMinSlider.setObjectName("spectroMinSlider")
        self.spectroMaxSlider = QtWidgets.QSlider(self.centralwidget)
        self.spectroMaxSlider.setGeometry(QtCore.QRect(1220, 480, 160, 22))
        self.spectroMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.spectroMaxSlider.setObjectName("spectroMaxSlider")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(40, 80, 1271, 361))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        
        #Our plotting widget
        self.graphCh1Container=QtWidgets.QWidget(self.splitter)
        self.graphCh1=pyqtgraph.GraphicsLayoutWidget(self.graphCh1Container)
        self.graphCh1.setGeometry(QtCore.QRect(20, 0, 1271, 360))
        self.graphCh1.setObjectName("graphCh1")
        
        
  #      self.max_x_limit=100
        #creating a plot (axis ..etc)
        self.p1=self.graphCh1.addPlot()   
        self.p2=self.graphCh1.addPlot()   

        #to put the limits of our graph .. solved compression problem)
        #coz it controls range of axis in the single frame
        self.scrollInitial=0
        self.scrollFinal=10
        self.p1.setXRange(self.scrollInitial, 20, padding=0)     
        self.p1.setLimits(xMin=0)
        self.p1.setLimits(xMax=62)
        self.p1.setLimits(yMin=-1)
        self.p1.setLimits(yMax=1)
        
        #defining our 3 curves
        self.curve1 = self.p1.plot()
        self.curve2 = self.p1.plot()
        self.curve3 = self.p1.plot()
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.graphCh1)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 347, 631, 14))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.spectrogram = PlotWidget(self.splitter)
        self.spectrogram.setObjectName("spectrogram")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1422, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuChannel_1 = QtWidgets.QMenu(self.menuActions)
        self.menuChannel_1.setObjectName("menuChannel_1")
        self.menuChannel_2 = QtWidgets.QMenu(self.menuActions)
        self.menuChannel_2.setObjectName("menuChannel_2")
        self.menuChannel_3 = QtWidgets.QMenu(self.menuActions)
        self.menuChannel_3.setObjectName("menuChannel_3")
        self.menuSpectrogram_Actions = QtWidgets.QMenu(self.menubar)
        self.menuSpectrogram_Actions.setObjectName("menuSpectrogram_Actions")
        self.menuColor_Palettes = QtWidgets.QMenu(self.menuSpectrogram_Actions)
        self.menuColor_Palettes.setObjectName("menuColor_Palettes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionChannel_1 = QtWidgets.QAction(MainWindow)
        self.actionChannel_1.setObjectName("actionChannel_1")
        self.actionChannel_2 = QtWidgets.QAction(MainWindow)
        self.actionChannel_2.setObjectName("actionChannel_2")
        self.actionChannel_3 = QtWidgets.QAction(MainWindow)
        self.actionChannel_3.setObjectName("actionChannel_3")
        self.actionSave_as_PDF = QtWidgets.QAction(MainWindow)
        self.actionSave_as_PDF.setObjectName("actionSave_as_PDF")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionChange_Color = QtWidgets.QAction(MainWindow)
        self.actionChange_Color.setObjectName("actionChange_Color")
        self.actionChange_Color_2 = QtWidgets.QAction(MainWindow)
        self.actionChange_Color_2.setObjectName("actionChange_Color_2")
        self.actionChange_Color_3 = QtWidgets.QAction(MainWindow)
        self.actionChange_Color_3.setObjectName("actionChange_Color_3")
        self.actionAdd_Title = QtWidgets.QAction(MainWindow)
        self.actionAdd_Title.setObjectName("actionAdd_Title")
        self.actionAdd_Titlee = QtWidgets.QAction(MainWindow)
        self.actionAdd_Titlee.setObjectName("actionAdd_Titlee")
        self.actionAdd_Title_2 = QtWidgets.QAction(MainWindow)
        self.actionAdd_Title_2.setObjectName("actionAdd_Title_2")
        self.actionPalette_1 = QtWidgets.QAction(MainWindow)
        self.actionPalette_1.setObjectName("actionPalette_1")
        self.actionPalette_2 = QtWidgets.QAction(MainWindow)
        self.actionPalette_2.setObjectName("actionPalette_2")
        self.actionPalette_3 = QtWidgets.QAction(MainWindow)
        self.actionPalette_3.setObjectName("actionPalette_3")
        self.actionPalette_4 = QtWidgets.QAction(MainWindow)
        self.actionPalette_4.setObjectName("actionPalette_4")
        self.actionPalette_5 = QtWidgets.QAction(MainWindow)
        self.actionPalette_5.setObjectName("actionPalette_5")
        self.actionChannel_7 = QtWidgets.QAction(MainWindow)
        self.actionChannel_7.setObjectName("actionChannel_7")
        self.actionChannel_8 = QtWidgets.QAction(MainWindow)
        self.actionChannel_8.setObjectName("actionChannel_8")
        self.actionChannel_9 = QtWidgets.QAction(MainWindow)
        self.actionChannel_9.setObjectName("actionChannel_9")
        self.actionChannel_10 = QtWidgets.QAction(MainWindow)
        self.actionChannel_10.setObjectName("actionChannel_10")
        self.actionChannel_11 = QtWidgets.QAction(MainWindow)
        self.actionChannel_11.setObjectName("actionChannel_11")
        self.menuOpen.addAction(self.actionChannel_1)
        self.menuOpen.addAction(self.actionChannel_2)
        self.menuOpen.addAction(self.actionChannel_3)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.actionSave_as_PDF)
        self.menuFile.addAction(self.actionExit)
        self.menuChannel_1.addAction(self.actionChange_Color)
        self.menuChannel_2.addAction(self.actionChange_Color_2)
        self.menuChannel_3.addAction(self.actionChange_Color_3)
        self.menuActions.addAction(self.menuChannel_1.menuAction())
        self.menuActions.addAction(self.menuChannel_2.menuAction())
        self.menuActions.addAction(self.menuChannel_3.menuAction())
        self.menuColor_Palettes.addAction(self.actionPalette_1)
        self.menuColor_Palettes.addAction(self.actionPalette_2)
        self.menuColor_Palettes.addAction(self.actionPalette_3)
        self.menuColor_Palettes.addAction(self.actionPalette_4)
        self.menuColor_Palettes.addAction(self.actionPalette_5)
        self.menuSpectrogram_Actions.addAction(self.menuColor_Palettes.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuSpectrogram_Actions.menuAction())
        

        self.channel="Ch1"
        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
        self.timer3 = QtCore.QTimer()   

    

        self.timerInterval = 100
        self.penColorIndex1=1
        self.penColorIndex2=1
        self.color = "#ffaa00"    
        self.label1 = "CHANNEL 1"
        self.file_name="CHANNEL_NAME"
        self.amp1=self.amp2=self.amp3=0
        self.time1=self.time2=self.time3=0
        self.palette = "viridis"
        
        self.rmin = 0
        self.rmax = 256
        self.gmin = 0
        self.gmax = 256
        self.bmin = 0
        self.bmax = 256
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.signalComboBox.setCurrentText(_translate("MainWindow", "Choose a channel"))
        self.signalComboBox.setItemText(0, _translate("MainWindow", "Choose a channel"))
        self.signalComboBox.setItemText(1, _translate("MainWindow", "Ch1"))
        self.signalComboBox.setItemText(2, _translate("MainWindow", "Ch2"))
        self.signalComboBox.setItemText(3, _translate("MainWindow", "Ch3"))
        self.pauseButtonCh.setText(_translate("MainWindow", "Pause"))
        self.pauseButtonCh.setShortcut(_translate("MainWindow", "P"))
        self.slowerButtonCh.setText(_translate("MainWindow", "Slower"))
        self.slowerButtonCh.setShortcut(_translate("MainWindow", "W"))
        self.zoomOutButtonCh.setText(_translate("MainWindow", "Zoom out"))
        self.zoomOutButtonCh.setShortcut(_translate("MainWindow", "-"))
        self.showButtonCh.setText(_translate("MainWindow", "Show"))
        self.showButtonCh.setShortcut(_translate("MainWindow", "G"))
        self.zoomInButtonCh.setText(_translate("MainWindow", "Zoom in"))
        self.zoomInButtonCh.setShortcut(_translate("MainWindow", "+"))
        self.spectroButtonCh.setText(_translate("MainWindow", "Spectro"))
        self.spectroButtonCh.setShortcut(_translate("MainWindow", "Q"))
        self.hideButtonCh.setText(_translate("MainWindow", "Hide"))
        self.hideButtonCh.setShortcut(_translate("MainWindow", "H"))
        self.label.setText(_translate("MainWindow", "Controls"))
        self.label_2.setText(_translate("mainWindow", "channel 1"))
        self.playButtonCh.setText(_translate("MainWindow", "Play"))
        self.playButtonCh.setShortcut(_translate("MainWindow", "S"))
        self.fasterButtonCh.setText(_translate("MainWindow", "Faster"))
        self.fasterButtonCh.setShortcut(_translate("MainWindow", "F"))
        self.addLabelButton.setText(_translate("MainWindow", "Add Label"))
        self.addLabelButton.setShortcut(_translate("MainWindow", "L"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.menuChannel_1.setTitle(_translate("MainWindow", "Channel 1"))
        self.menuChannel_2.setTitle(_translate("MainWindow", "Channel 2"))
        self.menuChannel_3.setTitle(_translate("MainWindow", "Channel 3"))
        self.menuSpectrogram_Actions.setTitle(_translate("MainWindow", "Spectrogram Actions"))
        self.menuColor_Palettes.setTitle(_translate("MainWindow", "Color Palettes"))
        self.actionChannel_1.setText(_translate("MainWindow", "Channel 1"))
        self.actionChannel_2.setText(_translate("MainWindow", "Channel 2"))
        self.actionChannel_3.setText(_translate("MainWindow", "Channel 3"))
        self.actionSave_as_PDF.setText(_translate("MainWindow", "Save as PDF"))
        self.actionSave_as_PDF.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "esc"))
        self.actionChange_Color.setText(_translate("MainWindow", "Change Color"))
        self.actionChange_Color_2.setText(_translate("MainWindow", "Change Color"))
        self.actionChange_Color_3.setText(_translate("MainWindow", "Change Color"))
        self.actionAdd_Title.setText(_translate("MainWindow", "Add Title"))
        self.actionAdd_Titlee.setText(_translate("MainWindow", "Add Title"))
        self.actionAdd_Title_2.setText(_translate("MainWindow", "Add Title"))
        self.actionPalette_1.setText(_translate("MainWindow", "Gray"))
        self.actionPalette_2.setText(_translate("MainWindow", "HSV"))
        self.actionPalette_3.setText(_translate("MainWindow", "Summer"))
        self.actionPalette_4.setText(_translate("MainWindow", "Viridis"))
        self.actionPalette_5.setText(_translate("MainWindow", "Turbo"))
        self.actionChannel_7.setText(_translate("MainWindow", "Channel 4"))
        self.actionChannel_8.setText(_translate("MainWindow", "Channel 5"))
        self.actionChannel_9.setText(_translate("MainWindow", "Channel 6"))
        self.actionChannel_10.setText(_translate("MainWindow", "Channel 4"))
        self.actionChannel_11.setText(_translate("MainWindow", "Channel 5"))
        self.signalComboBox.currentTextChanged.connect(lambda: self.channelComboBox())
        self.actionExit.triggered.connect(lambda: self.exitApp())
        self.menuOpen.triggered.connect(lambda: self.channelComboBox())
        self.zoomInButtonCh.clicked.connect(lambda: self.zoomIn(self.channel))
        self.zoomOutButtonCh.clicked.connect(lambda: self.zoomOut(self.channel))
        self.playButtonCh.clicked.connect(lambda: self.playCh(self.channel))
        self.pauseButtonCh.clicked.connect(lambda: self.pauseCh1(self.channel))
        self.spectroButtonCh.clicked.connect(lambda: self.spectro(self.channel))
        self.slowerButtonCh.clicked.connect(lambda: self.slow(self.channel,self.timerInterval))
        self.fasterButtonCh.clicked.connect(lambda: self.fast(self.channel,self.timerInterval))
        self.showButtonCh.clicked.connect(lambda: self.show(self.channel))
        self.hideButtonCh.clicked.connect(lambda: self.hide(self.channel))
        self.actionChange_Color.triggered.connect(lambda: self.colorPicker())
        self.actionChange_Color_2.triggered.connect(lambda: self.colorPicker())
        self.actionChange_Color_3.triggered.connect(lambda: self.colorPicker())
        self.spectroMinSlider.valueChanged.connect(lambda:self.minSlider(self.spectroMinSlider.value()))
        self.spectroMaxSlider.valueChanged.connect(lambda:self.maxSlider(self.spectroMaxSlider.value()))
        self.spectroMinSlider.setMinimum(0)
        self.spectroMinSlider.setMaximum(255)
        self.spectroMaxSlider.setMinimum(0)
        self.spectroMaxSlider.setMaximum(255)
        self.addLabelButton.clicked.connect(lambda: self.addTitle())
        self.actionSave_as_PDF.triggered.connect(lambda: self.gen_pdf())
        self.horizontalScrollBar.valueChanged.connect(lambda: self.scroll(self.horizontalScrollBar.value()))
        self.actionPalette_1.triggered.connect(lambda : self.setpalette(self.actionPalette_1.text()))
        self.actionPalette_2.triggered.connect(lambda : self.setpalette(self.actionPalette_2.text()))
        self.actionPalette_3.triggered.connect(lambda : self.setpalette(self.actionPalette_3.text()))
        self.actionPalette_4.triggered.connect(lambda : self.setpalette(self.actionPalette_4.text()))
        self.actionPalette_5.triggered.connect(lambda : self.setpalette(self.actionPalette_5.text()))
        

        
    def setpalette(self , txt):  
        self.palette = txt
        self.spectro(self.channel)



        #declaring necessary globals 
        global time1
        global amp1
        global time2
        global amp2
        global time3
        global amp3
        

    def scroll(self, val):
        if val>self.scrollInitial:
            self.scrollRight()
        else:
            self.scrollLeft()

    
    def scrollRight(self):
        self.p1.setXRange(self.scrollInitial, self.scrollFinal, padding=0) 
        self.scrollInitial+=5
        self.scrollFinal+=5

    def scrollLeft(self):
        self.p1.setXRange(self.scrollInitial, self.scrollFinal, padding=0) 
        self.scrollInitial-=5
        self.scrollFinal-=5
       

    def channelComboBox(self):
        self.channel=self.signalComboBox.currentText()
        if self.channel =="Ch1":
            self.open_file()
        elif self.channel=="Ch2":
            self.open_file2()
        else :
            self.open_file3()


    def get_stats(self,time,amp):
        
        """gets statistics of our signal"""
        mean_amp = round(statistics.mean(amp),6)
        std_amp = round(statistics.stdev(amp),6)
        max_val=round(max(amp),6)
        min_val=round(min(amp),6)
        duration=round(time[-1],6)

        
        stats=[mean_amp,std_amp,max_val,min_val,duration] 
        return stats

    def gen_pdf(self):
        """creates a pdf containing stats and pic"""
        global time1
        global amp1
        global time2
        global amp2    
        global time3
        global amp3          
        exporter = pyqtgraph.exporters.ImageExporter(self.graphCh1.scene())
        exporter.export('the_graph.png') 
        exporter2=pyqtgraph.exporters.ImageExporter(self.spectrogram.scene())
        exporter2.export('the_spectro.png') 
         
        
        try:
            stats1=self.get_stats(time1,amp1)
        except NameError:
            stats1=["NA","NA","NA","NA","NA"]
            print("well, you didn't open ch1 !") 
    
        try:
            stats2=self.get_stats(time2,amp2)
        except NameError:
            stats2=["NA","NA","NA","NA","NA"]
            print("well, you didn't open ch2 !!")

        try:
            stats3=self.get_stats(time3,amp3)
        except NameError:
            stats3=["NA","NA","NA","NA","NA"]
            print("well, you didn't open ch3 !!")
            
        stats=stats1+stats2+stats3    
        print(stats)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('arial', 'B', 11)
        pdf.cell(60)
        pdf.cell(75, 10, 'Signal Viewer - Summary & statistics', 0, 2, 'C')
        pdf.cell(90, 10, ' ', 0, 2, 'C')
        pdf.cell(-55)
        columnNameList = ['Mean','std',"max_amp","min_amp","duration"]

        for header in columnNameList:
            pdf.cell(32, 10, header, 0, 0, 'C')         

        pdf.cell(0,ln=1)
        pdf.set_font('arial', '', 7)
        r=0
        for row in range(0, 3):
            i=r
            for col in range(0,5):
                pdf.cell(32,10, str(stats[i]), 0, 0, 'C')
                i=i+1
            r=r+5
            pdf.cell(0,ln=1)
  
        pdf.cell(0,ln=1)
        pdf.cell(0,ln=1)
        pdf.cell(0,ln=1)
        pdf.cell(0,ln=1)
        pdf.cell(0,ln=1)
        pdf.cell(0,ln=1)
        
        pdf.set_font('arial', 'B', 10)
        pdf.cell(32, 10, "Graph & Spectro:", 0, 0, 'C')
        pdf.image('the_graph.png', x = 25, y = 70,w = 100, h = 50)
        pdf.image('the_spectro.png', x = 25, y = 140,w = 100, h = 50)
    
        pdf.output('signal viewer summary.pdf')

    def open_file(self):
      """opens a file from the brower """
      file_path=QFileDialog.getOpenFileName()
      self.file_name=file_path[0].split('/')[-1]
      self.read_data(self.file_name)

    def open_file2(self):
      """opens a file from the brower """
      file_path=QFileDialog.getOpenFileName()
      self.file_name=file_path[0].split('/')[-1]
      self.read_data2(self.file_name)

    def open_file3(self):
      """opens a file from the brower """
      file_path=QFileDialog.getOpenFileName()
      self.file_name=file_path[0].split('/')[-1]
      self.read_data3(self.file_name)



    def read_data(self,file_name):
        """loads the data from chosen file"""
        df1=pd.read_csv(file_name)
        self.label1=file_name
        global time1
        global amp1
        time1=list(pd.to_numeric(df1['time'],downcast="float"))
        amp1=list(pd.to_numeric(df1['amplitude'],downcast="float"))
        self.draw(time1,amp1,self.color)

    
             
            
    def read_data2(self,file_name):
        """loads the data from chosen file"""  
        df2=pd.read_csv(file_name)
        global time2
        global amp2       
        self.label2=file_name  #trial
        time2=list(pd.to_numeric(df2['time'],downcast="float"))
        amp2=list(pd.to_numeric(df2['amplitude'],downcast="float"))
        self.draw2(time2,amp2,self.color)



    def read_data3(self,file_name):
        """loads the data from chosen file"""
        df3=pd.read_csv(file_name)
        global time3
        global amp3  
        self.label3 = file_name
        time3=list(pd.to_numeric(df3['time'],downcast="float"))
        amp3=list(pd.to_numeric(df3['amplitude'],downcast="float"))
        self.draw3(time3,amp3,self.color)
    
    def draw(self,time,amp,color):
        """sets up our canvas to plot"""
        self.time1 = time
        self.amp1 = amp
        self.index = 0  
        pen = pyqtgraph.mkPen(color) #signal color
        self.curve1.setData(self.time1[0:self.index+1000], self.amp1[0:self.index+1000], pen=pen)     
        self.timer1.setInterval(100)
        self.timer1.timeout.connect(lambda:self.update_plot_data(self.time1,self.amp1))
        self.timer1.start()
                            

    def draw2(self,time,amp,color):
        """sets up our canvas to plot"""
        self.time2 = time
        self.amp2 = amp
        self.index2=0  
        pen = pyqtgraph.mkPen(color) #signal color
        self.curve2.setData(self.time2[0:self.index2+1000], self.amp2[0:self.index2+1000], pen=pen)
        self.timer2.setInterval(100)
        self.timer2.timeout.connect(lambda:self.update_plot_data2(self.time2,self.amp2))
        self.timer2.start()

    def draw3(self,time,amp,color):
        """sets up our canvas to plot"""
        self.time3 = time
        self.amp3 = amp
        self.index3=0  
        pen = pyqtgraph.mkPen(color) #signal color
        self.curve3.setData(self.time3[0:self.index3+1000], self.amp3[0:self.index3+1000], pen=pen)
        self.timer3.setInterval(100)
        self.timer3.timeout.connect(lambda:self.update_plot_data3(self.time3,self.amp3))
        self.timer3.start()                     


    def update_plot_data(self,time,amp): 
        """updates the data plotted on graph to get dynamic signal"""
        
        dynamic_time = time[0:self.index+1000]  
        dynamic_amp = amp[0:self.index+1000]
        try:
            self.p1.setXRange(time[self.index], time[self.index+1000], padding=0) 
        except:
            pass
        
        self.index=self.index+1000
        if self.index+1000>len(time):
            self.index=0

        self.curve1.setData(dynamic_time, dynamic_amp)  # Update the data  


    def update_plot_data2(self,time2,amp2): 
        """updates the data plotted on graph to get dynamic signal"""
        
        dynamic_time2 = time2[0:self.index2+1000]  
        dynamic_amp2 = amp2[0:self.index2+1000]
        try:
            self.p1.setXRange(time2[self.index2], time2[self.index2+1000], padding=0) 
        except:
            pass        

        self.index2=self.index2+1000
        if self.index2+1000>len(time2):
            self.index2=0

        self.curve2.setData(dynamic_time2, dynamic_amp2)  # Update the data 

    def update_plot_data3(self,time3,amp3): 
        """updates the data plotted on graph to get dynamic signal"""
        
        dynamic_time3 = self.time3[0:self.index3+1000]  
        dynamic_amp3 = self.amp3[0:self.index3+1000]
        try:
           self.p1.setXRange(time3[self.index3], time3[self.index3+1000], padding=0) 
        except:
            pass      
        
        self.index3=self.index3+1000
        if self.index3+1000>len(time3):
            self.index3=0

        self.curve3.setData(dynamic_time3, dynamic_amp3)  # Update the data 
        
 
    def colorPicker(self):
        self.on_click()

    @pyqtSlot()
    def on_click(self):
        self.openColorDialog()

    def openColorDialog(self):
        color = QColorDialog.getColor()
        self.color=color
        if color.isValid():
            print(color.name())
    


    def exitApp(self):
        sys.exit()



    def addTitle(self):
        
        self.label_2.setText(self.file_name)
        self.label_2.update()
        

 
    def zoomIn(self,ch):
       if ch=="Ch1":
            self.curve1.getViewBox().scaleBy((0.5,0.5))
        
       elif ch==  "Ch2":
            self.curve2.getViewBox().scaleBy((0.5,0.5))
            
       else:
            self.curve3.getViewBox().scaleBy((0.5,0.5))

    def zoomOut(self,ch):
        if ch=="Ch1":
            self.curve1.getViewBox().scaleBy((2,2))
        
        elif ch==  "Ch2":
            self.curve2.getViewBox().scaleBy((2,2))
            
        else:
            self.curve3.getViewBox().scaleBy((2,2))
    
  
    def playCh(self, channel):
        if channel =="Ch1":
            self.timer1.start()
        elif channel=="Ch2": 
            self.timer2.start()
        else:
            self.timer3.start()



    def pauseCh1(self, channel):
        """pauses the dynamic signal in ch1"""
        if channel =="Ch1":
            self.timer1.stop()
        elif channel=="Ch2":
            self.timer2.stop()
        else:
            self.timer3.stop() 

        


    def slow(self,channel,timerInterval):
        self.timerInterval = self.timerInterval * 2
        if channel== "Ch1": 
            self.timer1.setInterval(self.timerInterval)
        elif channel =="Ch2":
            self.timer2.setInterval(self.timerInterval)
        else:
            self.timer3.setInterval(self.timerInterval)
        

    def fast(self,channel,timerInterval):
        self.timerInterval = self.timerInterval / 2
        if channel == "Ch1":
            self.timer1.setInterval(self.timerInterval)
        elif channel=="Ch2":
            self.timer2.setInterval(self.timerInterval)
        else:
            self.timer3.setInterval(self.timerInterval)
       


    def hide(self,channel):
        if channel =="Ch1":
            self.draw(self.time1,self.amp1,"k")
        elif channel == "Ch2":
            self.draw2(self.time2,self.amp2,"k")
        else:
            self.draw3(self.time3,self.amp3,"k")

    def show(self,channel):
        if channel =="Ch1":
            self.draw(self.time1,self.amp1,self.color)
        elif channel=="Ch2":
            self.draw2(self.time2,self.amp2,self.color)
        else:
            self.draw3(self.time3,self.amp3,self.color)



    def maxSlider(self , value):
        slider_value=value
        self.rmax=slider_value 
        self.gmax=slider_value   
        self.bmax=slider_value 
        self.spectro(self.channel)
        

    def minSlider(self , value ):
        slider_value=value
        self.rmin=slider_value 
        self.gmin=slider_value  
        self.bmin=slider_value
        self.spectro(self.channel)
       

    def figToImg(self ,fig ,dpi = 90):
        buf = io.BytesIO()
        fig.savefig(buf, format="jpeg", dpi=dpi)
        buf.seek(0)
        arrimg = np.frombuffer(buf.getvalue(), dtype=np.uint8)
        print(buf.getvalue())
        buf.close()
        self.img = cv2.imdecode(arrimg, 1)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        return self.img
    
    def spectro(self , channel):
        if channel =="Ch1":
            if not self.amp1:
                 pass
            else:   
                fig=plt.figure()
                self.spec_gram = plt.specgram(self.amp1, Fs=200 )
                self.plotGraph = pyqtgraph.PlotItem()
                pyqtgraph.PlotItem.enableAutoScale(self.plotGraph)
                pyqtgraph.PlotItem.hideAxis(self.plotGraph,'left')
                pyqtgraph.PlotItem.hideAxis(self.plotGraph,'bottom')
                self.spectrogram.setCentralItem(self.plotGraph)
                self.img=self.figToImg(fig)
                self.img = np.rot90(self.img , k=1 , axes= (1,0))
                self.image = pyqtgraph.ImageItem(self.img)
                self.image.setLevels([[ self.rmin , self.rmax] , [ self.gmin , self.gmax], [ self.bmin , self.bmax]])
                self.plotGraph.addItem(self.image)
        elif channel =="Ch2":
            if not self.amp2:
                 pass
            else:   
                fig=plt.figure()
                self.spec_gram = plt.specgram(self.amp2, Fs=256 )
                self.plotGraph = pyqtgraph.PlotItem()
                pyqtgraph.PlotItem.enableAutoScale(self.plotGraph)
                pyqtgraph.PlotItem.hideAxis(self.plotGraph,'left')
                pyqtgraph.PlotItem.hideAxis(self.plotGraph,'bottom')
                self.spectrogram.setCentralItem(self.plotGraph)
                self.img=self.figToImg(fig)
                self.img = np.rot90(self.img , k=1 , axes= (1,0))
                self.image = pyqtgraph.ImageItem(self.img)
                self.image.setLevels([[ self.rmin , self.rmax] , [ self.gmin , self.gmax], [ self.bmin , self.bmax]])
                self.plotGraph.addItem(self.image)
        elif channel == "Ch3":
            if not self.amp3:
                pass
            else:   
                fig=plt.figure()
                self.spec_gram = plt.specgram(self.amp3, Fs=256 )
                self.plotGraph = pyqtgraph.PlotItem()
                pyqtgraph.PlotItem.enableAutoScale(self.plotGraph)
                pyqtgraph.PlotItem.hideAxis(self.plotGraph,'left')
                pyqtgraph.PlotItem.hideAxis(self.plotGraph,'bottom')
                self.spectrogram.setCentralItem(self.plotGraph)
                self.img=self.figToImg(fig)
                self.img = np.rot90(self.img , k=1 , axes= (1,0))
                self.image = pyqtgraph.ImageItem(self.img)
                self.image.setLevels([[ self.rmin , self.rmax] , [ self.gmin , self.gmax], [ self.bmin , self.bmax]])
                self.plotGraph.addItem(self.image)
        else:
            pass
                
   

              
             

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())