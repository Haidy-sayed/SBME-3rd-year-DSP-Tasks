# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task2GUI_mainFinal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import itertools
from pyqtgraph import PlotWidget
from Task2GUI_composerFinal import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from Task2GUI_composerFinal import Ui_Form
import pyqtgraph.exporters
from fpdf import FPDF
import statistics
from pyqtgraph import PlotWidget
import pyqtgraph
from pyqtgraph import *
import pyqtgraph as pg
from pyqtgraph import PlotWidget, PlotItem
#from matplotlib.pyplot import draw
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
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
import io
from numpy.fft import fft, fftfreq, ifft
from scipy.fftpack import fft, ifft
from scipy import signal
import cmath

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.widget_2)
        self.splitter.setMinimumSize(QtCore.QSize(100, 0))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.mainChannel = PlotWidget(self.splitter)
        self.mainChannel.setObjectName("mainChannel")
        self.secindaryChannel = PlotWidget(self.splitter)
        self.secindaryChannel.setObjectName("secindaryChannel")
        self.verticalLayout.addWidget(self.splitter)
        self.freqSlider = QtWidgets.QSlider(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.freqSlider.setFont(font)
        self.freqSlider.setMaximum(3)
        self.freqSlider.setOrientation(QtCore.Qt.Horizontal)
        self.freqSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.freqSlider.setObjectName("freqSlider")
        self.verticalLayout.addWidget(self.freqSlider)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainLabel = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName("mainLabel")
        self.verticalLayout_2.addWidget(self.mainLabel)
        self.secondaryLabel = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.secondaryLabel.setFont(font)
        self.secondaryLabel.setObjectName("secondaryLabel")
        self.verticalLayout_2.addWidget(self.secondaryLabel)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuComposer = QtWidgets.QMenu(self.menubar)
        self.menuComposer.setObjectName("menuComposer")
        self.menuSignal_processes = QtWidgets.QMenu(self.menubar)
        self.menuSignal_processes.setObjectName("menuSignal_processes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen_composer = QtWidgets.QAction(MainWindow)
        self.actionOpen_composer.setObjectName("actionOpen_composer")
        self.actionSample = QtWidgets.QAction(MainWindow)
        self.actionSample.setObjectName("actionSample")
        self.actionReconstruct = QtWidgets.QAction(MainWindow)
        self.actionReconstruct.setObjectName("actionReconstruct")
        self.actionShow_2nd_Ch = QtWidgets.QAction(MainWindow)
        self.actionShow_2nd_Ch.setObjectName("actionShow_2nd_Ch")
        self.actionHide_2nd_Ch = QtWidgets.QAction(MainWindow)
        self.actionHide_2nd_Ch.setObjectName("actionHide_2nd_Ch")
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.actionExit)
        self.menuComposer.addAction(self.actionOpen_composer)
        self.menuSignal_processes.addAction(self.actionSample)
        self.menuSignal_processes.addAction(self.actionReconstruct)
        self.menuSignal_processes.addAction(self.actionShow_2nd_Ch)
        self.menuSignal_processes.addAction(self.actionHide_2nd_Ch)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuComposer.menuAction())
        self.menubar.addAction(self.menuSignal_processes.menuAction())
        self.actionOpen_composer.triggered.connect(lambda:self.openSecond())

        self.timer1 = QtCore.QTimer()
        self.time1 = []
        self.amp1 =[]
        
        #self.timeSample=0
        self.numSamples=0
        self.samplingInterval=0
        self.Fsample=0
        self.color = "#ffaa00" 
        self.timerInterval = 1
        self.coeffSample=0
        self.mainChannel.setXRange(0, 2, padding=0)     
        self.mainChannel.setLimits(xMin=0)
        self.mainChannel.setLimits(xMax=20)
        self.mainChannel.setLimits(yMin=-20)
        self.mainChannel.setLimits(yMax=20)
        self.array1=0
        self.array2=0
        self.array3=0
        self.logHistory=[]
        global dataFile
        
        self.secindaryChannel.setXRange(0, 2, padding=0)     
        self.secindaryChannel.setLimits(xMin=0)
        self.secindaryChannel.setLimits(xMax=62)
        self.secindaryChannel.setLimits(yMin=-20)
        self.secindaryChannel.setLimits(yMax=20)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainLabel.setText(_translate("MainWindow", "Main Channel"))
        self.secondaryLabel.setText(_translate("MainWindow", "Secondary Channel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuComposer.setTitle(_translate("MainWindow", "Composer"))
        self.menuSignal_processes.setTitle(_translate("MainWindow", "Signal processes"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "esc"))
        self.actionOpen_composer.setText(_translate("MainWindow", "Open composer"))
        self.actionSample.setText(_translate("MainWindow", "Sample"))
        self.actionReconstruct.setText(_translate("MainWindow", "Reconstruct"))
        self.actionShow_2nd_Ch.setText(_translate("MainWindow", "Show 2nd Ch"))
        self.actionHide_2nd_Ch.setText(_translate("MainWindow", "Hide 2nd Ch"))
        self.actionExit.triggered.connect(lambda: self.exitApp())
        self.actionOpen_file.triggered.connect(lambda: self.openFile())
        self.actionSample.triggered.connect(lambda: self.signalSample(self.dataFile, self.freqSlider.value(), self.amp1))
        self.freqSlider.valueChanged.connect(lambda: self.signalSample(self.dataFile,self.freqSlider.value(),self.amp1))
        self.actionHide_2nd_Ch.triggered.connect(lambda: self.hideSecondChannel())
        self.actionShow_2nd_Ch.triggered.connect(lambda: self.showSecondChannel())
        self.actionReconstruct.triggered.connect(lambda: self.reConstruct(self.numSamples, self.samplingInterval, self.ampArray))
        
        
    ##hiding the secondary channel by default
        self.secindaryChannel.setMaximumHeight(0)
        self.secondaryLabel.setMaximumHeight(0)

    def openFile(self):
      
      """opens a file from the brower """
      file_path=QFileDialog.getOpenFileName()
      self.file_name=file_path[0].split('/')[-1]
      self.read_data(self.file_name)
      self.logHistory.append("Opening file")
      

    def read_data(self,file_name):
        """loads the data from chosen file"""
        self.dataFile=pd.read_csv(file_name)
        self.label1=file_name
        self.time1=list(pd.to_numeric(self.dataFile['time'],downcast="float"))
        self.amp1=list(pd.to_numeric(self.dataFile['amplitude'],downcast="float"))
        self.draw(self.color)
        self.signalSample(self.dataFile, self.freqSlider.value(), self.amp1)
        self.logHistory.append("Reading file")

    def draw(self,color):
        """Clearing main channel in case of recalling"""
        self.mainChannel.clear()
        """sets up our canvas to plot"""
        self.index=0  
        pen = pyqtgraph.mkPen(color) #signal color
        self.mainChannel.plot(self.time1, self.amp1, pen=pen)
        print(self.amp1)
        self.timer1.setInterval(100)
        self.timer1.start()

        self.logHistory.append("Drawing the read signal")

    def signalSample(self, signal,sliderValue,amplitudes):
        self.secindaryChannel.clear()
        self.logHistory.append("Slider value = ")
        self.logHistory.append(sliderValue)
        if sliderValue==0:
            self.logHistory.append("inside sample but slider didn't move!")
            self.logHistory.append("Sampling value = 0 , use the slider please!")
        else:
            self.coeffSample=sliderValue
            #sampleFreqs, segmentTimes, sxx= signal.spectrogram(signal,, nperseg=256, noverlap=128, nfft=512, window=('hamming'))
            Fourier2DArray=fft(signal)
            self.logHistory.append("Fourier 2D")
            self.logHistory.append(Fourier2DArray)
            #print(type(FourierArray))
            #Fourier1DArray=Fourier2DArray.flatten()
            frequenciesArray = map(lambda Fourier1DArray: Fourier1DArray[0], Fourier2DArray)
            self.logHistory.append("Frequencies")
            self.logHistory.append(frequenciesArray)
            Fmax = int(abs(max(frequenciesArray)))
            samplingRate = self.coeffSample * Fmax
            samplingInterval =1/samplingRate
            self.timeEnd=self.time1[-1]
            self.timeBegin=0
            #self.timeSample = np.arange(self.timeBegin,(self.timeEnd),(self.timeEnd/len(self.time1)))
            ampArray =list(itertools.repeat(0, len(self.time1)))
            self.numSamples=int(self.timeEnd/samplingInterval)
            samplingStep= int(len(self.time1)/self.numSamples)
            counter=0
            sampleCounter=0
            self.logHistory.append("Fmax = ")
            self.logHistory.append(Fmax)
            #self.logHistory.append("Length of timeSample = ")
            #self.logHistory.append(len(self.timeSample))
            self.logHistory.append("samplingInterval = ")
            self.logHistory.append(samplingInterval)
            self.logHistory.append("number of Samples = ")
            self.logHistory.append(self.numSamples)
            self.logHistory.append("Sampled amplitude array")
            self.logHistory.append(ampArray)
        

            while (sampleCounter <len(self.time1)):
                ampArray[sampleCounter]=amplitudes[sampleCounter]
                
                sampleCounter = sampleCounter+samplingStep
                print(sampleCounter)
                #print(amplitudes[sampleCounter])
                #print(self.ampArray[sampleCounter])

            print(ampArray)
            self.logHistory.append("sucessfully finished the sampling")
         # self.updatePlot(sliderValue,timeSample,ampArray)
            pen = pyqtgraph.mkPen('Blue') #signal color
            self.logHistory.append("choose blue for the sampled")
            self.secindaryChannel.plot(self.time1, ampArray, symbl= '+')
            #self.mainChannel.plot(self.time1[0:len(self.time1)],self.ampArray[0:len(self.time1)], symbol = '+')
            self.logHistory.append("Passed by the draw call of the samples")

            
    def reConstruct(self, numSample, tVal, ampArr, tSample):
        self.logHistory.append("Inside the reconstruction function ")
        timeReconstrct=tSample
        ampReconstruct=ampArr
        #print(len(ampReconstruct))
        #removing the none
        i=0
        while i < len(ampReconstruct):
            if ampReconstruct[i] == None:
                ampReconstruct[i]=0
            i=i+1
        sumSignalReconstruct=[0]*len(self.time1)

        FReConstSample= self.Fsample
        j=0        
        #print("===============================================================================================")
        maxAmp= max(self.ampArray)
        while j < len(timeReconstrct):
            #print(j)
            #print(ampReconstruct[j])
            #print( ampReconstruct[j])
            #print(numpy.sinc(j))
            for k in np.arange(-len(timeReconstrct), len(timeReconstrct),1):
                sumSignalReconstruct[j] += maxAmp*((numpy.sinc((timeReconstrct[j]-(k*(1/FReConstSample)))/(1/FReConstSample))))
            j+=1
        #print(sumSignalReconstruct)
        #print(ampReconstruct)
           
        self.secindaryChannel.plot(timeReconstrct[0:len(timeReconstrct)],sumSignalReconstruct[0:len(timeReconstrct)])
        self.updateReconstruct(timeReconstrct,sumSignalReconstruct,self.freqSlider.value()) 

    def updateReconstruct(self,time,sum,val):
        self.logHistory.append("Inside the update reconstruction function ")
        
        if val==0:
            self.secindaryChannel.plot(time[0:len(time)],self.array1[0:len(time)],pen = pyqtgraph.mkPen("#000000"))
            self.secindaryChannel.plot(time[0:len(time)],self.array2[0:len(time)],pen = pyqtgraph.mkPen("#000000"))
            self.secindaryChannel.plot(time[0:len(time)],self.array3[0:len(time)],pen = pyqtgraph.mkPen("#000000"))

        elif val==1:
            self.array1=sum
            self.secindaryChannel.plot(time[0:len(time)],self.array1[0:len(time)],pen = pyqtgraph.mkPen("#ffaa00"))
            self.secindaryChannel.plot(time[0:len(time)],self.array2[0:len(time)],pen = pyqtgraph.mkPen("#000000"))
            self.secindaryChannel.plot(time[0:len(time)],self.array3[0:len(time)],pen = pyqtgraph.mkPen("#000000"))

        elif val==2:
           
            self.array2=sum
            self.secindaryChannel.plot(time[0:len(time)],self.array1[0:len(time)],pen = pyqtgraph.mkPen("#000000"))
            self.secindaryChannel.plot(time[0:len(time)],self.array2[0:len(time)],pen = pyqtgraph.mkPen("#ffaa00"))
            self.secindaryChannel.plot(time[0:len(time)],self.array3[0:len(time)],pen = pyqtgraph.mkPen("#000000"))
        elif val==3:
      
            self.array3=sum
            self.secindaryChannel.plot(time[0:len(time)],self.array1[0:len(time)],pen = pyqtgraph.mkPen("#000000"))
            self.secindaryChannel.plot(time[0:len(time)],self.array2[0:len(time)],pen = pyqtgraph.mkPen("#000000"))
            self.secindaryChannel.plot(time[0:len(time)],self.array3[0:len(time)],pen = pyqtgraph.mkPen("#ffaa00"))
        





    def hideSecondChannel(self):
        self.secindaryChannel.setMaximumHeight(0)
        self.secondaryLabel.setMaximumHeight(0)

    def showSecondChannel(self):
        self.secindaryChannel.setMinimumHeight(0)
        self.secindaryChannel.setMaximumHeight(200)
        self.secondaryLabel.setMaximumHeight(30)


    def exitApp(self):
        self.logHistory.append("Closing!! BYE ")
        self.logging()
        sys.exit()

    def move_to_main(self):
        """moves composed signal to main graph"""
        self.move_t=self.ui.t
      #  print(self.ui.sum_amp)
        self.move_amp=self.ui.sum_amp
        self.mainChannel.plot(self.move_t,self.move_amp)


    def openSecond(self):
        """opens the composer gui"""

        self.Form = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
        self.ui.pushButton_2.clicked.connect( lambda : self.move_to_main())

    def logging(self):
        f=open("Task2Log.txt","w+")
        for i in self.logHistory:
            f.write("=> %s\r\n" %(i))
        f.close()    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
