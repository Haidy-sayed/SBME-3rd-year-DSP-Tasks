# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task2GUI_composer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(688, 600)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.composerContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.composerContainer.sizePolicy().hasHeightForWidth())
        self.composerContainer.setSizePolicy(sizePolicy)
        self.composerContainer.setMinimumSize(QtCore.QSize(0, 0))
        self.composerContainer.setMaximumSize(QtCore.QSize(8377215, 16777215))
        self.composerContainer.setObjectName("composerContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.composerContainer)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.composerContainer)
        self.splitter.setMinimumSize(QtCore.QSize(200, 0))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.composer_channel_1 = PlotWidget(self.splitter)
        self.composer_channel_1.setObjectName("composer_channel_1")
        self.composer_channel_2 = PlotWidget(self.splitter)
        self.composer_channel_2.setObjectName("composer_channel_2")
        self.horizontalLayout_3.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.composer_control = QtWidgets.QWidget(self.composerContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.composer_control.sizePolicy().hasHeightForWidth())
        self.composer_control.setSizePolicy(sizePolicy)
        self.composer_control.setMinimumSize(QtCore.QSize(0, 0))
        self.composer_control.setMaximumSize(QtCore.QSize(400, 16777215))
        self.composer_control.setObjectName("composer_control")
        self.formLayout = QtWidgets.QFormLayout(self.composer_control)
        self.formLayout.setObjectName("formLayout")
        self.label_composer = QtWidgets.QLabel(self.composer_control)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_composer.setFont(font)
        self.label_composer.setObjectName("label_composer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_composer)
        self.label_composer_phase = QtWidgets.QLabel(self.composer_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_composer_phase.sizePolicy().hasHeightForWidth())
        self.label_composer_phase.setSizePolicy(sizePolicy)
        self.label_composer_phase.setObjectName("label_composer_phase")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_composer_phase)
        self.phase_input = QtWidgets.QLineEdit(self.composer_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phase_input.sizePolicy().hasHeightForWidth())
        self.phase_input.setSizePolicy(sizePolicy)
        self.phase_input.setMinimumSize(QtCore.QSize(0, 0))
        self.phase_input.setObjectName("phase_input")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.phase_input)
        self.label_composer_mag = QtWidgets.QLabel(self.composer_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_composer_mag.sizePolicy().hasHeightForWidth())
        self.label_composer_mag.setSizePolicy(sizePolicy)
        self.label_composer_mag.setObjectName("label_composer_mag")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_composer_mag)
        self.magnitude_input = QtWidgets.QLineEdit(self.composer_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.magnitude_input.sizePolicy().hasHeightForWidth())
        self.magnitude_input.setSizePolicy(sizePolicy)
        self.magnitude_input.setObjectName("magnitude_input")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.magnitude_input)
        self.pushButton_2 = QtWidgets.QPushButton(self.composer_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.composer_control)
        self.pushButton_4 = QtWidgets.QPushButton(self.composer_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.composer_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.comboBox = QtWidgets.QComboBox(self.composer_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.freq_input = QtWidgets.QLineEdit(self.composer_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freq_input.sizePolicy().hasHeightForWidth())
        self.freq_input.setSizePolicy(sizePolicy)
        self.freq_input.setObjectName("freq_input")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.freq_input)
        self.label_composer_freq = QtWidgets.QLabel(self.composer_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_composer_freq.sizePolicy().hasHeightForWidth())
        self.label_composer_freq.setSizePolicy(sizePolicy)
        self.label_composer_freq.setObjectName("label_composer_freq")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_composer_freq)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(10, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.horizontalLayout.addWidget(self.composer_control)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addWidget(self.composerContainer)
        Form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 21))
        self.menubar.setObjectName("menubar")
        self.menuComposer = QtWidgets.QMenu(self.menubar)
        self.menuComposer.setObjectName("menuComposer")
        Form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)
        self.actionSave_composed_signal = QtWidgets.QAction(Form)
        self.actionSave_composed_signal.setObjectName("actionSave_composed_signal")
        self.menuComposer.addAction(self.actionSave_composed_signal)
        self.menubar.addAction(self.menuComposer.menuAction())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_composer.setText(_translate("Form", "Composer"))
        self.label_composer_phase.setText(_translate("Form", "Phase"))
        self.label_composer_mag.setText(_translate("Form", "Magnitude"))
        self.pushButton_2.setText(_translate("Form", "Draw on main graph"))
        self.pushButton_4.setText(_translate("Form", "Draw sin"))
        self.pushButton_3.setText(_translate("Form", "remove"))
        self.pushButton.setText(_translate("Form", "Compose"))
        self.comboBox.setItemText(0, _translate("Form", "Choose sinusoidal"))
        self.label_composer_freq.setText(_translate("Form", "Frequency"))
        self.menuComposer.setTitle(_translate("Form", "Composer"))
        self.actionSave_composed_signal.setText(_translate("Form", "Save composed signal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
