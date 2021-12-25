# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIF.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from pyqtgraph import PlotWidget
import pyqtgraph
from PyQt5 import QtCore, QtGui, QtWidgets
#from matplotlib.pyplot import draw
#from pyqtgraph.widgets.PlotWidget import PlotWidget
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QInputDialog, QLineEdit
import os
import numpy as np
from PyQt5.QtWidgets import QMessageBox

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(847, 674)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #channel1
        self.graphCh1 = PlotWidget(self.centralwidget)
        self.graphCh1.setGeometry(QtCore.QRect(10, 40, 491, 151))
        self.graphCh1.setObjectName("graphCh1")
        
        #channel2
        self.graphCh2 = PlotWidget(self.centralwidget)
        self.graphCh2.setGeometry(QtCore.QRect(10, 320, 491, 161))
        self.graphCh2.setObjectName("graphCh2")
        
        #sprctogram
        self.spectrogram = QtWidgets.QWidget(self.centralwidget)
        self.spectrogram.setGeometry(QtCore.QRect(550, 40, 211, 371))
        self.spectrogram.setObjectName("spectrogram")
        
        self.playPauseButtonCh1 = QtWidgets.QPushButton(self.centralwidget)
        self.playPauseButtonCh1.setGeometry(QtCore.QRect(10, 220, 75, 23))
        self.playPauseButtonCh1.setObjectName("playPauseButtonCh1")
        self.playPauseButtonCh1.clicked.connect(lambda:self.Pause1()) #pausing 1st

        
        self.zoomInButtonCh1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomInButtonCh1.setGeometry(QtCore.QRect(150, 220, 75, 23))
        self.zoomInButtonCh1.setObjectName("zoomInButtonCh1")
        
        self.zoomOutButtonCh1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOutButtonCh1.setGeometry(QtCore.QRect(290, 220, 75, 23))
        self.zoomOutButtonCh1.setObjectName("zoomOutButtonCh1")
        
        self.stopButtonCh1 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButtonCh1.setGeometry(QtCore.QRect(430, 220, 75, 23))
        self.stopButtonCh1.setObjectName("stopButtonCh1")
        self.stopButtonCh1.clicked.connect(lambda:self.clear('ch_one')) #clear 1st

        
        self.playPauseButtonCh2 = QtWidgets.QPushButton(self.centralwidget)
        self.playPauseButtonCh2.setGeometry(QtCore.QRect(10, 520, 75, 23))
        self.playPauseButtonCh2.setObjectName("playPauseButtonCh2")
        self.playPauseButtonCh2.clicked.connect(lambda:self.Pause2()) #pausing 2nd


        self.zoomInButtonCh2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomInButtonCh2.setGeometry(QtCore.QRect(150, 520, 75, 23))
        self.zoomInButtonCh2.setObjectName("zoomInButtonCh2")
        
        self.zoomOutButtonCh2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOutButtonCh2.setGeometry(QtCore.QRect(290, 520, 75, 23))
        self.zoomOutButtonCh2.setObjectName("zoomOutButtonCh2")
        
        self.stopButtonCh2 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButtonCh2.setGeometry(QtCore.QRect(430, 520, 75, 23))
        self.stopButtonCh2.setObjectName("stopButtonCh2")
        self.stopButtonCh2.clicked.connect(lambda:self.clear('ch_two')) #clear 2nd

        
        self.spectroRun = QtWidgets.QPushButton(self.centralwidget)
        self.spectroRun.setGeometry(QtCore.QRect(620, 450, 75, 23))
        self.spectroRun.setObjectName("spectroRun")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 5, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 275, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 20, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 520, 75, 23))
        self.pushButton.setObjectName("pushButton")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 26))
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
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
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
        self.actionSpectro_Ch_1 = QtWidgets.QAction(mainWindow)
        self.actionSpectro_Ch_1.setObjectName("actionSpectro_Ch_1")
        self.actionSpectro_Ch2 = QtWidgets.QAction(mainWindow)
        self.actionSpectro_Ch2.setObjectName("actionSpectro_Ch2")
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
        self.actionAdd_Title = QtWidgets.QAction(mainWindow)
        self.actionAdd_Title.setObjectName("actionAdd_Title")
        self.actionAdd_Title_2 = QtWidgets.QAction(mainWindow)
        self.actionAdd_Title_2.setObjectName("actionAdd_Title_2")
        self.menuOpen.addAction(self.menuOpen_Ch1)
        self.menuOpen.addAction(self.menuOpen_Ch2)
        self.menuOpen.addAction(self.actionSpectro_Ch_1)
        self.menuOpen.addAction(self.actionSpectro_Ch2)
        self.menuSave_as.addAction(self.actionPDF)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.menuSave_as.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuChannel_1.addAction(self.actionShow_Hide)
        self.menuChannel_1.addAction(self.actionChange_Color)
        self.menuChannel_1.addAction(self.actionSpeed_Options_2)
        self.menuChannel_1.addAction(self.actionAdd_Title)
        self.menuChannel_2.addAction(self.actionShow_Hide_2)
        self.menuChannel_2.addAction(self.actionChange_Color_2)
        self.menuChannel_2.addAction(self.actionSpeed_Options)
        self.menuChannel_2.addAction(self.actionAdd_Title_2)
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
        self.menubar.addAction(self.menuAbout.menuAction())
        
        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "BioMedical Signal Viewer"))
        self.playPauseButtonCh1.setText(_translate("mainWindow", "Play/Pause"))
        self.zoomInButtonCh1.setText(_translate("mainWindow", "Zoom in"))
        self.zoomOutButtonCh1.setText(_translate("mainWindow", "Zoom out"))
        self.stopButtonCh1.setText(_translate("mainWindow", "Clear"))
        self.playPauseButtonCh2.setText(_translate("mainWindow", "Play/Pause"))
        self.zoomInButtonCh2.setText(_translate("mainWindow", "Zoom in"))
        self.zoomOutButtonCh2.setText(_translate("mainWindow", "Zoom out"))
        self.stopButtonCh2.setText(_translate("mainWindow", "Clear"))
        self.spectroRun.setText(_translate("mainWindow", "Spectro 1"))
        self.label.setText(_translate("mainWindow", "CHANNEL 1"))
        self.label_2.setText(_translate("mainWindow", "CHANNEL 2"))
        self.label_3.setText(_translate("mainWindow", "SPECTROGRAM"))
        self.pushButton.setText(_translate("mainWindow", "Spectro 2"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuOpen.setTitle(_translate("mainWindow", "Open"))
        self.menuSave_as.setTitle(_translate("mainWindow", "Save as"))
        self.menuActions.setTitle(_translate("mainWindow", "Actions"))
        self.menuChannel_1.setTitle(_translate("mainWindow", "Channel 1"))
        self.menuChannel_2.setTitle(_translate("mainWindow", "Channel 2"))
        self.menuAbout.setTitle(_translate("mainWindow", "About"))
        self.menuSpectrogram_Actions.setTitle(_translate("mainWindow", "Spectrogram Actions"))
        self.menuColor_Palettes.setTitle(_translate("mainWindow", "Color Palettes"))
        self.menuOpen_Ch1.setText(_translate("mainWindow", "Channel 1"))
        self.menuOpen_Ch2.setText(_translate("mainWindow", "Channel 2"))
        self.actionSpectro_Ch_1.setText(_translate("mainWindow", "Spectro-Ch 1"))
        self.actionSpectro_Ch2.setText(_translate("mainWindow", "Spectro-Ch2"))
        self.menuSave_asImg.setText(_translate("mainWindow", "Img"))
        self.menuSave_asMp4.setText(_translate("mainWindow", "mp4"))
        self.actionPlay_Pause.setText(_translate("mainWindow", "Play/Pause"))
        self.actionZoom_in.setText(_translate("mainWindow", "Zoom in"))
        self.actionZoom_out.setText(_translate("mainWindow", "Zoom out"))
        self.actionPlay_Pause_2.setText(_translate("mainWindow", "Play/Pause"))
        self.actionZoom_in_2.setText(_translate("mainWindow", "Zoom in"))
        self.actionZoom_out_2.setText(_translate("mainWindow", "Zoom out"))
        self.actionStop.setText(_translate("mainWindow", "Clear"))
        self.actionSpectro.setText(_translate("mainWindow", "Spectro"))
        self.actionPlay_Pause_3.setText(_translate("mainWindow", "Play/Pause"))
        self.actionZoom_in_3.setText(_translate("mainWindow", "Zoom in"))
        self.actionZoom_out_3.setText(_translate("mainWindow", "Zoom out"))
        self.actionStop_2.setText(_translate("mainWindow", "Clear"))
        self.actionSpectro_2.setText(_translate("mainWindow", "Spectro"))
        self.actionExit_App.setText(_translate("mainWindow", "Exit App"))
        self.actionExit.setText(_translate("mainWindow", "Exit"))
        self.actionShow_Hide.setText(_translate("mainWindow", "Show/Hide"))
        self.actionChange_Color.setText(_translate("mainWindow", "Change Color"))
        self.actionShow_Hide_2.setText(_translate("mainWindow", "Show/Hide"))
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
        self.actionAdd_Title.setText(_translate("mainWindow", "Add Title"))
        self.actionAdd_Title_2.setText(_translate("mainWindow", "Add Title"))
        self.actionExit.triggered.connect(lambda: self.exitApp())
        self.menuOpen_Ch1.triggered.connect(lambda: self.openFile("ch1"))
        self.menuOpen_Ch2.triggered.connect(lambda: self.openFile("ch2"))

    def exitApp(self):
        sys.exit()

    
    def openFile(self,text):
      """opens a file from the brower """
      file_path=QFileDialog.getOpenFileName()
      file_name=file_path[0].split('/')[-1]
      self.read_data(file_name,text)


    def read_data(self,file_name,text):
        """loads the data from chosen file"""
        
        if text=="ch1":
            df1=pd.read_csv(file_name)
            time1=list(pd.to_numeric(df1['time'],downcast="float"))
            amp1=list(pd.to_numeric(df1['amplitude'],downcast="float"))
            self.draw(time1,amp1,text)
            
        else:
            df2=pd.read_csv(file_name)
            time2=list(pd.to_numeric(df2['time'],downcast="float"))
            amp2=list(pd.to_numeric(df2['amplitude'],downcast="float"))
            self.draw(time2,amp2,text)
            
      
    def draw(self,time,amp,text):
        """sets up our canvas to plot"""
        self.time = time
        self.amp=amp
        self.text=text
        self.index=0  

        if self.text=="ch1":
            self.graphCh1.setBackground('w') #background color
            pen = pyqtgraph.mkPen(color=(255, 0, 0)) #signal color
            self.data_line =  self.graphCh1.plot(self.time[self.index:self.index+500], self.amp[self.index:self.index+500], pen=pen)
            self.timer1.setInterval(100)
            self.timer1.timeout.connect(lambda:self.update_plot_data(self.time,self.amp))
            self.timer1.start()
                     
        else:
            
            pen = pyqtgraph.mkPen(color=(0, 0, 255)) #signal color
            self.data_line =  self.graphCh2.plot(self.time[self.index:self.index+500], self.amp[self.index:self.index+500], pen=pen)
            self.timer2.setInterval(100)
            self.timer2.timeout.connect(lambda:self.update_plot_data(self.time,self.amp))
            self.timer2.start()


    def update_plot_data(self,time,amp): 
        """updates the data plotted on graph to get dynamic signal"""
        
        dynamic_time = time[self.index:self.index+500]  
        dynamic_amp = amp[self.index:self.index+500]
        self.index=self.index+500
    
        if self.index+500>len(time):
            self.index=0

        self.data_line.setData(dynamic_time, dynamic_amp)  # Update the data  


    def Pause1(self):
        """pauses the dynamic signal in ch1"""
        self.timer1.stop()  
            
 
    def Pause2(self):
        """ pauses the dynamic signal in ch2"""
        self.timer2.stop()        

            
   
    def clear(self,which_channel):
        """Clears the graph from any plots"""
        if which_channel== 'ch_one':
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

