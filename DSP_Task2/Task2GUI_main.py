# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task2GUI_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Task2GUI_composer import Ui_Form
from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(718, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.samplingContainer = QtWidgets.QWidget(self.centralwidget)
        self.samplingContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.samplingContainer.setObjectName("samplingContainer")
        self.label_mainChannel = QtWidgets.QLabel(self.samplingContainer)
        self.label_mainChannel.setGeometry(QtCore.QRect(9, 9, 77, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_mainChannel.sizePolicy().hasHeightForWidth())
        self.label_mainChannel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_mainChannel.setFont(font)
        self.label_mainChannel.setObjectName("label_mainChannel")
        self.samplingSlider = QtWidgets.QSlider(self.samplingContainer)
        self.samplingSlider.setGeometry(QtCore.QRect(9, 510, 84, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.samplingSlider.sizePolicy().hasHeightForWidth())
        self.samplingSlider.setSizePolicy(sizePolicy)
        self.samplingSlider.setMouseTracking(False)
        self.samplingSlider.setMaximum(3)
        self.samplingSlider.setTracking(True)
        self.samplingSlider.setOrientation(QtCore.Qt.Horizontal)
        self.samplingSlider.setInvertedAppearance(False)
        self.samplingSlider.setInvertedControls(False)
        self.samplingSlider.setObjectName("samplingSlider")
        self.splitter = QtWidgets.QSplitter(self.samplingContainer)
        self.splitter.setGeometry(QtCore.QRect(-11, 31, 711, 471))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.mainChannel = PlotWidget(self.splitter)
        self.mainChannel.setMinimumSize(QtCore.QSize(0, 100))
        self.mainChannel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainChannel.setObjectName("mainChannel")
        self.secondaryChannel = PlotWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secondaryChannel.sizePolicy().hasHeightForWidth())
        self.secondaryChannel.setSizePolicy(sizePolicy)
        self.secondaryChannel.setMaximumSize(QtCore.QSize(16777215, 200))
        self.secondaryChannel.setObjectName("secondaryChannel")
        self.horizontalLayout.addWidget(self.samplingContainer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSample = QtWidgets.QMenu(self.menubar)
        self.menuSample.setObjectName("menuSample")
        self.menuComposer = QtWidgets.QMenu(self.menubar)
        self.menuComposer.setObjectName("menuComposer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionSave_as_PDF = QtWidgets.QAction(MainWindow)
        self.actionSave_as_PDF.setObjectName("actionSave_as_PDF")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCompose_signal = QtWidgets.QAction(MainWindow)
        self.actionCompose_signal.setObjectName("actionCompose_signal")
        self.actionSampling = QtWidgets.QAction(MainWindow)
        self.actionSampling.setObjectName("actionSampling")
        self.actionRe_construction = QtWidgets.QAction(MainWindow)
        self.actionRe_construction.setObjectName("actionRe_construction")
        self.actionShow_on_secondary_channel = QtWidgets.QAction(MainWindow)
        self.actionShow_on_secondary_channel.setObjectName("actionShow_on_secondary_channel")
        self.actionHide_secondary_channel = QtWidgets.QAction(MainWindow)
        self.actionHide_secondary_channel.setObjectName("actionHide_secondary_channel")
        self.actionSave_composed_as = QtWidgets.QAction(MainWindow)
        self.actionSave_composed_as.setObjectName("actionSave_composed_as")
        self.actionShow_reconstructed_on_main_channel = QtWidgets.QAction(MainWindow)
        self.actionShow_reconstructed_on_main_channel.setObjectName("actionShow_reconstructed_on_main_channel")
        self.actionOpen_composer_window = QtWidgets.QAction(MainWindow)
        self.actionOpen_composer_window.setObjectName("actionOpen_composer_window")
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.actionSave_as_PDF)
        self.menuFile.addAction(self.actionExit)
        self.menuSample.addAction(self.actionSampling)
        self.menuSample.addAction(self.actionRe_construction)
        self.menuSample.addAction(self.actionShow_on_secondary_channel)
        self.menuSample.addAction(self.actionHide_secondary_channel)
        self.menuSample.addAction(self.actionShow_reconstructed_on_main_channel)
        self.menuComposer.addAction(self.actionOpen_composer_window)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuComposer.menuAction())
        self.menubar.addAction(self.menuSample.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_mainChannel.setText(_translate("MainWindow", "Main Channel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSample.setTitle(_translate("MainWindow", "Signal processes"))
        self.menuComposer.setTitle(_translate("MainWindow", "Composer"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionOpen_file.setShortcut(_translate("MainWindow", "Shift+O"))
        self.actionSave_as_PDF.setText(_translate("MainWindow", "Save as PDF"))
        self.actionSave_as_PDF.setShortcut(_translate("MainWindow", "Shift+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))
        self.actionCompose_signal.setText(_translate("MainWindow", "Compose signal"))
        self.actionSampling.setText(_translate("MainWindow", "Sample"))
        self.actionRe_construction.setText(_translate("MainWindow", "Re-construction"))
        self.actionShow_on_secondary_channel.setText(_translate("MainWindow", "Show on secondary channel"))
        self.actionHide_secondary_channel.setText(_translate("MainWindow", "Hide secondary channel"))
        self.actionSave_composed_as.setText(_translate("MainWindow", "Save composed as"))
        self.actionShow_reconstructed_on_main_channel.setText(_translate("MainWindow", "Show reconstructed on main channel"))
        self.actionOpen_composer_window.setText(_translate("MainWindow", "Open composer window"))
        self.actionOpen_composer_window.triggered.connect(lambda:self.openSecond())


    def openSecond(self):
        self.Form = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

