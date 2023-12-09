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

from GUI import Ui_mainWindow

class mainApp(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(mainApp, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit.triggered.connect(lambda: self.exitApp())
        #self.ui.menuOpen.triggered.connect(lambda: self.channelComboBox())
        self.ui.actionChange_Color.triggered.connect(lambda: self.colorPicker())
        self.ui.actionChange_Color_2.triggered.connect(lambda: self.colorPicker())
        #self.ui.actionPalette_1.triggered.connect(lambda : self.setpalette(self.actionPalette_1.text))
        #self.ui.actionPalette_2.triggered.connect(lambda : self.setpalette(self.actionPalette_2.text))
        #self.ui.actionPalette_3.triggered.connect(lambda : self.setpalette(self.actionPalette_3.text))
        #self.ui.actionPalette_4.triggered.connect(lambda : self.setpalette(self.actionPalette_4.text))
        #self.ui.actionPalette_5.triggered.connect(lambda : self.setpalette(self.actionPalette_5.text))
        self.ui.menuOpen_Ch1.triggered.connect(lambda: self.playCh("Ch1"))
        self.ui.menuOpen_Ch2.triggered.connect(lambda: self.playCh("Ch2"))
        self.ui.Faster1_2.triggered.connect(lambda: self.fast("Ch1") )
        self.ui.Faster2_2.triggered.connect(lambda: self.fast("Ch2") )
        self.ui.Slower1_2.triggered.connect(lambda: self.slow("Ch1"))
        self.ui.Slower2_2.triggered.connect(lambda: self.slow("Ch2"))

        #Our plotting widget
        self.graphCh1Container=QtWidgets.QWidget(self.ui.Channel)
        self.graphCh1=pyqtgraph.GraphicsLayoutWidget(self.graphCh1Container)
        self.graphCh1.setGeometry(QtCore.QRect(20, 0, 1271, 360))
        self.graphCh1.setObjectName("graphCh1")


        #declaring necessary globals 
        global time1
        global amp1
        global time2
        global amp2
        global time3
        global amp3
        global palette
        #setting channel 1 as the default
        channelFlag = "Ch1"
        scrollInitial = 0
        #setting initail timerInterval into 1 so to not get initailized with any random nu,ber but 1
        timerInterval =1

    def setpalette(self , txt):  
        self.palette = txt
        self.spectro(self.channelFlag)
        

    def scroll(self, val):
        if val>self.scrollInitial:
            self.scrollRight()
        else:
            self.scrollLeft()
        #creating a plot (axis ..etc)
        self.p1=self.graphCh1.addPlot()   
        #to put the limits of our graph .. solved compression problem)
        #coz it controls range of axis in the single frame
        self.scrollInitial=0
        self.scrollFinal=10
        self.p1.setXRange(self.scrollInitial, 20, padding=0)     
        self.p1.setLimits(xMin=0)
        
        #defining our 3 curves
        self.curve1 = self.p1.plot()
        self.curve2 = self.p1.plot()
        self.curve3 = self.p1.plot()
        


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
      #  pdf.cell(35, 10, 0, 0, 'C')         

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


    
    def draw(self,time,amp,color):
        """sets up our canvas to plot"""
        self.time1 = time
        self.amp1=amp
        self.index=0  
        pen = pyqtgraph.mkPen(color) #signal color
        self.curve1.setData(self.time1[0:self.index+500], self.amp1[0:self.index+500], pen=pen)
        
        self.timer1.setInterval(100)
        self.timer1.timeout.connect(lambda:self.update_plot_data(self.time1,self.amp1))
        self.timer1.start()
                            

    def draw2(self,time2,amp2,color):
        """sets up our canvas to plot"""
        self.time2 = time2
        self.amp2=amp2
        self.index2=0  
        pen = pyqtgraph.mkPen(color) #signal color
        self.curve2.setData(self.time2[0:self.index2+500], self.amp2[0:self.index2+500], pen=pen)
        self.timer2.setInterval(100)
        self.timer2.timeout.connect(lambda:self.update_plot_data2(self.time2,self.amp2))
        self.timer2.start()


    def update_plot_data(self,time,amp): 
        """updates the data plotted on graph to get dynamic signal"""
        
        dynamic_time = time[0:self.index+500]  
        dynamic_amp = amp[0:self.index+500]
        self.index=self.index+500
    
        if self.index+500>len(time):
            self.index=0

        self.curve1.setData(dynamic_time, dynamic_amp)  # Update the data  

    def update_plot_data2(self,time2,amp2): 
        """updates the data plotted on graph to get dynamic signal"""
        
        dynamic_time2 = time2[0:self.index2+500]  
        dynamic_amp2 = amp2[0:self.index2+500]
        self.index2=self.index2+500
    
        if self.index2+500>len(time2):
            self.index2=0

        self.curve2.setData(dynamic_time2, dynamic_amp2)  # Update the data 

        
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



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = mainApp()
    main.show()
    sys.exit(app.exec_())