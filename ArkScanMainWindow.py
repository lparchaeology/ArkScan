# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ArkScanMainWindow.ui'
#
# Created: Fri Feb 20 14:29:34 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ArkScanMainWindow(object):
    def setupUi(self, ArkScanMainWindow):
        ArkScanMainWindow.setObjectName(_fromUtf8("ArkScanMainWindow"))
        ArkScanMainWindow.resize(1101, 971)
        self.centralwidget = QtGui.QWidget(ArkScanMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.m_previewButton = QtGui.QPushButton(self.layoutWidget)
        self.m_previewButton.setObjectName(_fromUtf8("m_previewButton"))
        self.verticalLayout.addWidget(self.m_previewButton)
        self.m_scanButton = QtGui.QPushButton(self.layoutWidget)
        self.m_scanButton.setObjectName(_fromUtf8("m_scanButton"))
        self.verticalLayout.addWidget(self.m_scanButton)
        self.m_saveButton = QtGui.QPushButton(self.layoutWidget)
        self.m_saveButton.setObjectName(_fromUtf8("m_saveButton"))
        self.verticalLayout.addWidget(self.m_saveButton)
        self.m_printButton = QtGui.QPushButton(self.layoutWidget)
        self.m_printButton.setObjectName(_fromUtf8("m_printButton"))
        self.verticalLayout.addWidget(self.m_printButton)
        self.m_copyButton = QtGui.QPushButton(self.layoutWidget)
        self.m_copyButton.setObjectName(_fromUtf8("m_copyButton"))
        self.verticalLayout.addWidget(self.m_copyButton)
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.m_siteLabel = QtGui.QLabel(self.layoutWidget)
        self.m_siteLabel.setObjectName(_fromUtf8("m_siteLabel"))
        self.gridLayout_3.addWidget(self.m_siteLabel, 0, 0, 1, 1)
        self.m_siteEdit = QtGui.QLineEdit(self.layoutWidget)
        self.m_siteEdit.setReadOnly(False)
        self.m_siteEdit.setObjectName(_fromUtf8("m_siteEdit"))
        self.gridLayout_3.addWidget(self.m_siteEdit, 0, 1, 1, 1)
        self.m_typeLabel = QtGui.QLabel(self.layoutWidget)
        self.m_typeLabel.setObjectName(_fromUtf8("m_typeLabel"))
        self.gridLayout_3.addWidget(self.m_typeLabel, 1, 0, 1, 1)
        self.m_typeCombo = QtGui.QComboBox(self.layoutWidget)
        self.m_typeCombo.setObjectName(_fromUtf8("m_typeCombo"))
        self.m_typeCombo.addItem(_fromUtf8(""))
        self.m_typeCombo.addItem(_fromUtf8(""))
        self.m_typeCombo.addItem(_fromUtf8(""))
        self.m_typeCombo.addItem(_fromUtf8(""))
        self.m_typeCombo.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.m_typeCombo, 1, 1, 1, 1)
        self.m_numberLabel = QtGui.QLabel(self.layoutWidget)
        self.m_numberLabel.setObjectName(_fromUtf8("m_numberLabel"))
        self.gridLayout_3.addWidget(self.m_numberLabel, 2, 0, 1, 1)
        self.m_numberSpin = QtGui.QSpinBox(self.layoutWidget)
        self.m_numberSpin.setMaximum(9999)
        self.m_numberSpin.setObjectName(_fromUtf8("m_numberSpin"))
        self.gridLayout_3.addWidget(self.m_numberSpin, 2, 1, 1, 1)
        self.m_gridLabel = QtGui.QLabel(self.layoutWidget)
        self.m_gridLabel.setObjectName(_fromUtf8("m_gridLabel"))
        self.gridLayout_3.addWidget(self.m_gridLabel, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.m_eastSpin = QtGui.QSpinBox(self.layoutWidget)
        self.m_eastSpin.setMaximum(9999)
        self.m_eastSpin.setSingleStep(5)
        self.m_eastSpin.setObjectName(_fromUtf8("m_eastSpin"))
        self.horizontalLayout_2.addWidget(self.m_eastSpin)
        self.m_northSpin = QtGui.QSpinBox(self.layoutWidget)
        self.m_northSpin.setMaximum(9999)
        self.m_northSpin.setSingleStep(5)
        self.m_northSpin.setObjectName(_fromUtf8("m_northSpin"))
        self.horizontalLayout_2.addWidget(self.m_northSpin)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.m_suffixLabel = QtGui.QLabel(self.layoutWidget)
        self.m_suffixLabel.setObjectName(_fromUtf8("m_suffixLabel"))
        self.gridLayout_3.addWidget(self.m_suffixLabel, 4, 0, 1, 1)
        self.m_suffixEdit = QtGui.QLineEdit(self.layoutWidget)
        self.m_suffixEdit.setMaxLength(10)
        self.m_suffixEdit.setObjectName(_fromUtf8("m_suffixEdit"))
        self.gridLayout_3.addWidget(self.m_suffixEdit, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.m_scanSavePlanButton = QtGui.QPushButton(self.layoutWidget)
        self.m_scanSavePlanButton.setDefault(True)
        self.m_scanSavePlanButton.setObjectName(_fromUtf8("m_scanSavePlanButton"))
        self.verticalLayout.addWidget(self.m_scanSavePlanButton)
        self.m_savePlanButton = QtGui.QPushButton(self.layoutWidget)
        self.m_savePlanButton.setObjectName(_fromUtf8("m_savePlanButton"))
        self.verticalLayout.addWidget(self.m_savePlanButton)
        self.m_scanCropSavePlanButton = QtGui.QPushButton(self.layoutWidget)
        self.m_scanCropSavePlanButton.setObjectName(_fromUtf8("m_scanCropSavePlanButton"))
        self.verticalLayout.addWidget(self.m_scanCropSavePlanButton)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.m_resolutionCombo = QtGui.QComboBox(self.layoutWidget)
        self.m_resolutionCombo.setObjectName(_fromUtf8("m_resolutionCombo"))
        self.m_resolutionCombo.addItem(_fromUtf8(""))
        self.m_resolutionCombo.addItem(_fromUtf8(""))
        self.m_resolutionCombo.addItem(_fromUtf8(""))
        self.m_resolutionCombo.addItem(_fromUtf8(""))
        self.m_resolutionCombo.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.m_resolutionCombo, 1, 1, 1, 1)
        self.m_orientationCombo = QtGui.QComboBox(self.layoutWidget)
        self.m_orientationCombo.setObjectName(_fromUtf8("m_orientationCombo"))
        self.m_orientationCombo.addItem(_fromUtf8(""))
        self.m_orientationCombo.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.m_orientationCombo, 3, 1, 1, 1)
        self.m_orientationLabel = QtGui.QLabel(self.layoutWidget)
        self.m_orientationLabel.setObjectName(_fromUtf8("m_orientationLabel"))
        self.gridLayout_2.addWidget(self.m_orientationLabel, 3, 0, 1, 1)
        self.m_pageSizeCombo = QtGui.QComboBox(self.layoutWidget)
        self.m_pageSizeCombo.setObjectName(_fromUtf8("m_pageSizeCombo"))
        self.m_pageSizeCombo.addItem(_fromUtf8(""))
        self.m_pageSizeCombo.addItem(_fromUtf8(""))
        self.m_pageSizeCombo.addItem(_fromUtf8(""))
        self.m_pageSizeCombo.addItem(_fromUtf8(""))
        self.m_pageSizeCombo.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.m_pageSizeCombo, 2, 1, 1, 1)
        self.m_pageSizeLabel = QtGui.QLabel(self.layoutWidget)
        self.m_pageSizeLabel.setObjectName(_fromUtf8("m_pageSizeLabel"))
        self.gridLayout_2.addWidget(self.m_pageSizeLabel, 2, 0, 1, 1)
        self.m_resolutionLabel = QtGui.QLabel(self.layoutWidget)
        self.m_resolutionLabel.setObjectName(_fromUtf8("m_resolutionLabel"))
        self.gridLayout_2.addWidget(self.m_resolutionLabel, 1, 0, 1, 1)
        self.m_modeCombo = QtGui.QComboBox(self.layoutWidget)
        self.m_modeCombo.setObjectName(_fromUtf8("m_modeCombo"))
        self.m_modeCombo.addItem(_fromUtf8(""))
        self.m_modeCombo.addItem(_fromUtf8(""))
        self.m_modeCombo.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.m_modeCombo, 0, 1, 1, 1)
        self.m_modeLabel = QtGui.QLabel(self.layoutWidget)
        self.m_modeLabel.setObjectName(_fromUtf8("m_modeLabel"))
        self.gridLayout_2.addWidget(self.m_modeLabel, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.m_scanSizeLayout = QtGui.QGridLayout()
        self.m_scanSizeLayout.setObjectName(_fromUtf8("m_scanSizeLayout"))
        self.m_xOriginLabel = QtGui.QLabel(self.layoutWidget)
        self.m_xOriginLabel.setObjectName(_fromUtf8("m_xOriginLabel"))
        self.m_scanSizeLayout.addWidget(self.m_xOriginLabel, 1, 0, 1, 1)
        self.m_xOriginSpin = QtGui.QSpinBox(self.layoutWidget)
        self.m_xOriginSpin.setMaximum(297)
        self.m_xOriginSpin.setObjectName(_fromUtf8("m_xOriginSpin"))
        self.m_scanSizeLayout.addWidget(self.m_xOriginSpin, 1, 1, 1, 1)
        self.m_yOriginLabel = QtGui.QLabel(self.layoutWidget)
        self.m_yOriginLabel.setObjectName(_fromUtf8("m_yOriginLabel"))
        self.m_scanSizeLayout.addWidget(self.m_yOriginLabel, 1, 2, 1, 1)
        self.m_yOriginSpin = QtGui.QSpinBox(self.layoutWidget)
        self.m_yOriginSpin.setMaximum(433)
        self.m_yOriginSpin.setObjectName(_fromUtf8("m_yOriginSpin"))
        self.m_scanSizeLayout.addWidget(self.m_yOriginSpin, 1, 3, 1, 1)
        self.m_widthLabel = QtGui.QLabel(self.layoutWidget)
        self.m_widthLabel.setObjectName(_fromUtf8("m_widthLabel"))
        self.m_scanSizeLayout.addWidget(self.m_widthLabel, 2, 0, 1, 1)
        self.m_widthSpin = QtGui.QSpinBox(self.layoutWidget)
        self.m_widthSpin.setMaximum(297)
        self.m_widthSpin.setObjectName(_fromUtf8("m_widthSpin"))
        self.m_scanSizeLayout.addWidget(self.m_widthSpin, 2, 1, 1, 1)
        self.m_heightLabel = QtGui.QLabel(self.layoutWidget)
        self.m_heightLabel.setObjectName(_fromUtf8("m_heightLabel"))
        self.m_scanSizeLayout.addWidget(self.m_heightLabel, 2, 2, 1, 1)
        self.m_heightSpin = QtGui.QSpinBox(self.layoutWidget)
        self.m_heightSpin.setMaximum(433)
        self.m_heightSpin.setObjectName(_fromUtf8("m_heightSpin"))
        self.m_scanSizeLayout.addWidget(self.m_heightSpin, 2, 3, 1, 1)
        self.m_scanSizeLabel1 = QtGui.QLabel(self.layoutWidget)
        self.m_scanSizeLabel1.setObjectName(_fromUtf8("m_scanSizeLabel1"))
        self.m_scanSizeLayout.addWidget(self.m_scanSizeLabel1, 0, 1, 1, 1)
        self.m_scanSizeLabel2 = QtGui.QLabel(self.layoutWidget)
        self.m_scanSizeLabel2.setObjectName(_fromUtf8("m_scanSizeLabel2"))
        self.m_scanSizeLayout.addWidget(self.m_scanSizeLabel2, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.m_scanSizeLayout)
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.m_detectCropAreaButton = QtGui.QPushButton(self.layoutWidget)
        self.m_detectCropAreaButton.setObjectName(_fromUtf8("m_detectCropAreaButton"))
        self.verticalLayout.addWidget(self.m_detectCropAreaButton)
        self.m_cropSizeLayout = QtGui.QGridLayout()
        self.m_cropSizeLayout.setObjectName(_fromUtf8("m_cropSizeLayout"))
        self.m_xCropLabel = QtGui.QLabel(self.layoutWidget)
        self.m_xCropLabel.setObjectName(_fromUtf8("m_xCropLabel"))
        self.m_cropSizeLayout.addWidget(self.m_xCropLabel, 1, 0, 1, 1)
        self.m_xCropSpin = QtGui.QSpinBox(self.layoutWidget)
        self.m_xCropSpin.setMaximum(99999)
        self.m_xCropSpin.setObjectName(_fromUtf8("m_xCropSpin"))
        self.m_cropSizeLayout.addWidget(self.m_xCropSpin, 1, 1, 1, 1)
        self.m_yCropLabel = QtGui.QLabel(self.layoutWidget)
        self.m_yCropLabel.setObjectName(_fromUtf8("m_yCropLabel"))
        self.m_cropSizeLayout.addWidget(self.m_yCropLabel, 1, 2, 1, 1)
        self.m_yCropSpin = QtGui.QSpinBox(self.layoutWidget)
        self.m_yCropSpin.setMaximum(99999)
        self.m_yCropSpin.setObjectName(_fromUtf8("m_yCropSpin"))
        self.m_cropSizeLayout.addWidget(self.m_yCropSpin, 1, 3, 1, 1)
        self.m_wCropLabel = QtGui.QLabel(self.layoutWidget)
        self.m_wCropLabel.setObjectName(_fromUtf8("m_wCropLabel"))
        self.m_cropSizeLayout.addWidget(self.m_wCropLabel, 2, 0, 1, 1)
        self.m_wCropSpin = QtGui.QSpinBox(self.layoutWidget)
        self.m_wCropSpin.setMaximum(99999)
        self.m_wCropSpin.setObjectName(_fromUtf8("m_wCropSpin"))
        self.m_cropSizeLayout.addWidget(self.m_wCropSpin, 2, 1, 1, 1)
        self.m_hCropLabel = QtGui.QLabel(self.layoutWidget)
        self.m_hCropLabel.setObjectName(_fromUtf8("m_hCropLabel"))
        self.m_cropSizeLayout.addWidget(self.m_hCropLabel, 2, 2, 1, 1)
        self.m_hCropSpin = QtGui.QSpinBox(self.layoutWidget)
        self.m_hCropSpin.setMaximum(99999)
        self.m_hCropSpin.setObjectName(_fromUtf8("m_hCropSpin"))
        self.m_cropSizeLayout.addWidget(self.m_hCropSpin, 2, 3, 1, 1)
        self.m_pixelLabel1 = QtGui.QLabel(self.layoutWidget)
        self.m_pixelLabel1.setObjectName(_fromUtf8("m_pixelLabel1"))
        self.m_cropSizeLayout.addWidget(self.m_pixelLabel1, 0, 1, 1, 1)
        self.m_pixelLabel2 = QtGui.QLabel(self.layoutWidget)
        self.m_pixelLabel2.setObjectName(_fromUtf8("m_pixelLabel2"))
        self.m_cropSizeLayout.addWidget(self.m_pixelLabel2, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.m_cropSizeLayout)
        self.m_cropButton = QtGui.QPushButton(self.layoutWidget)
        self.m_cropButton.setObjectName(_fromUtf8("m_cropButton"))
        self.verticalLayout.addWidget(self.m_cropButton)
        self.m_progressBar = QtGui.QProgressBar(self.layoutWidget)
        self.m_progressBar.setProperty("value", 0)
        self.m_progressBar.setObjectName(_fromUtf8("m_progressBar"))
        self.verticalLayout.addWidget(self.m_progressBar)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.splitter = QtGui.QSplitter(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(0, 0))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.m_scanView = ArkScanGraphicsView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_scanView.sizePolicy().hasHeightForWidth())
        self.m_scanView.setSizePolicy(sizePolicy)
        self.m_scanView.setMinimumSize(QtCore.QSize(800, 650))
        self.m_scanView.setAutoFillBackground(True)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.m_scanView.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.m_scanView.setForegroundBrush(brush)
        self.m_scanView.setInteractive(True)
        self.m_scanView.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.m_scanView.setObjectName(_fromUtf8("m_scanView"))
        self.m_outputText = QtGui.QTextBrowser(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_outputText.sizePolicy().hasHeightForWidth())
        self.m_outputText.setSizePolicy(sizePolicy)
        self.m_outputText.setObjectName(_fromUtf8("m_outputText"))
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        ArkScanMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ArkScanMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1101, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.m_menu = QtGui.QMenu(self.menubar)
        self.m_menu.setObjectName(_fromUtf8("m_menu"))
        ArkScanMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ArkScanMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ArkScanMainWindow.setStatusBar(self.statusbar)
        self.m_quitAction = QtGui.QAction(ArkScanMainWindow)
        self.m_quitAction.setObjectName(_fromUtf8("m_quitAction"))
        self.m_menu.addAction(self.m_quitAction)
        self.menubar.addAction(self.m_menu.menuAction())
        self.m_siteLabel.setBuddy(self.m_siteEdit)
        self.m_typeLabel.setBuddy(self.m_typeCombo)
        self.m_numberLabel.setBuddy(self.m_numberSpin)
        self.m_gridLabel.setBuddy(self.m_eastSpin)
        self.m_suffixLabel.setBuddy(self.m_suffixEdit)

        self.retranslateUi(ArkScanMainWindow)
        QtCore.QMetaObject.connectSlotsByName(ArkScanMainWindow)
        ArkScanMainWindow.setTabOrder(self.m_previewButton, self.m_scanButton)
        ArkScanMainWindow.setTabOrder(self.m_scanButton, self.m_saveButton)
        ArkScanMainWindow.setTabOrder(self.m_saveButton, self.m_printButton)
        ArkScanMainWindow.setTabOrder(self.m_printButton, self.m_copyButton)
        ArkScanMainWindow.setTabOrder(self.m_copyButton, self.m_siteEdit)
        ArkScanMainWindow.setTabOrder(self.m_siteEdit, self.m_typeCombo)
        ArkScanMainWindow.setTabOrder(self.m_typeCombo, self.m_numberSpin)
        ArkScanMainWindow.setTabOrder(self.m_numberSpin, self.m_eastSpin)
        ArkScanMainWindow.setTabOrder(self.m_eastSpin, self.m_northSpin)
        ArkScanMainWindow.setTabOrder(self.m_northSpin, self.m_suffixEdit)
        ArkScanMainWindow.setTabOrder(self.m_suffixEdit, self.m_savePlanButton)
        ArkScanMainWindow.setTabOrder(self.m_savePlanButton, self.m_scanCropSavePlanButton)
        ArkScanMainWindow.setTabOrder(self.m_scanCropSavePlanButton, self.m_modeCombo)
        ArkScanMainWindow.setTabOrder(self.m_modeCombo, self.m_resolutionCombo)
        ArkScanMainWindow.setTabOrder(self.m_resolutionCombo, self.m_pageSizeCombo)
        ArkScanMainWindow.setTabOrder(self.m_pageSizeCombo, self.m_orientationCombo)
        ArkScanMainWindow.setTabOrder(self.m_orientationCombo, self.m_xOriginSpin)
        ArkScanMainWindow.setTabOrder(self.m_xOriginSpin, self.m_yOriginSpin)
        ArkScanMainWindow.setTabOrder(self.m_yOriginSpin, self.m_widthSpin)
        ArkScanMainWindow.setTabOrder(self.m_widthSpin, self.m_heightSpin)
        ArkScanMainWindow.setTabOrder(self.m_heightSpin, self.m_detectCropAreaButton)
        ArkScanMainWindow.setTabOrder(self.m_detectCropAreaButton, self.m_xCropSpin)
        ArkScanMainWindow.setTabOrder(self.m_xCropSpin, self.m_yCropSpin)
        ArkScanMainWindow.setTabOrder(self.m_yCropSpin, self.m_wCropSpin)
        ArkScanMainWindow.setTabOrder(self.m_wCropSpin, self.m_hCropSpin)
        ArkScanMainWindow.setTabOrder(self.m_hCropSpin, self.m_cropButton)
        ArkScanMainWindow.setTabOrder(self.m_cropButton, self.m_scanView)
        ArkScanMainWindow.setTabOrder(self.m_scanView, self.m_outputText)

    def retranslateUi(self, ArkScanMainWindow):
        ArkScanMainWindow.setWindowTitle(_translate("ArkScanMainWindow", "MainWindow", None))
        self.m_previewButton.setText(_translate("ArkScanMainWindow", "Preview", None))
        self.m_scanButton.setText(_translate("ArkScanMainWindow", "Scan", None))
        self.m_saveButton.setText(_translate("ArkScanMainWindow", "Save", None))
        self.m_printButton.setText(_translate("ArkScanMainWindow", "Print", None))
        self.m_copyButton.setText(_translate("ArkScanMainWindow", "Copy", None))
        self.m_siteLabel.setText(_translate("ArkScanMainWindow", "Site:", None))
        self.m_typeLabel.setText(_translate("ArkScanMainWindow", "Type:", None))
        self.m_typeCombo.setItemText(0, _translate("ArkScanMainWindow", "Context", None))
        self.m_typeCombo.setItemText(1, _translate("ArkScanMainWindow", "Plan", None))
        self.m_typeCombo.setItemText(2, _translate("ArkScanMainWindow", "Section", None))
        self.m_typeCombo.setItemText(3, _translate("ArkScanMainWindow", "Top Plan", None))
        self.m_typeCombo.setItemText(4, _translate("ArkScanMainWindow", "Matrix", None))
        self.m_numberLabel.setText(_translate("ArkScanMainWindow", "Number:", None))
        self.m_numberSpin.setToolTip(_translate("ArkScanMainWindow", "Context Number", None))
        self.m_gridLabel.setText(_translate("ArkScanMainWindow", "Grid Ref:", None))
        self.m_suffixLabel.setText(_translate("ArkScanMainWindow", "Suffix:", None))
        self.m_scanSavePlanButton.setText(_translate("ArkScanMainWindow", "Scan and Save Plan", None))
        self.m_savePlanButton.setText(_translate("ArkScanMainWindow", "Save Plan", None))
        self.m_scanCropSavePlanButton.setText(_translate("ArkScanMainWindow", "Scan, Auto Crop and Save Plan", None))
        self.m_resolutionCombo.setItemText(0, _translate("ArkScanMainWindow", "600", None))
        self.m_resolutionCombo.setItemText(1, _translate("ArkScanMainWindow", "300", None))
        self.m_resolutionCombo.setItemText(2, _translate("ArkScanMainWindow", "150", None))
        self.m_resolutionCombo.setItemText(3, _translate("ArkScanMainWindow", "75", None))
        self.m_resolutionCombo.setItemText(4, _translate("ArkScanMainWindow", "50", None))
        self.m_orientationCombo.setItemText(0, _translate("ArkScanMainWindow", "Portrait", None))
        self.m_orientationCombo.setItemText(1, _translate("ArkScanMainWindow", "Landscape", None))
        self.m_orientationLabel.setText(_translate("ArkScanMainWindow", "Orientation", None))
        self.m_pageSizeCombo.setItemText(0, _translate("ArkScanMainWindow", "Permatrace", None))
        self.m_pageSizeCombo.setItemText(1, _translate("ArkScanMainWindow", "A3", None))
        self.m_pageSizeCombo.setItemText(2, _translate("ArkScanMainWindow", "A4", None))
        self.m_pageSizeCombo.setItemText(3, _translate("ArkScanMainWindow", "A5", None))
        self.m_pageSizeCombo.setItemText(4, _translate("ArkScanMainWindow", "Custom", None))
        self.m_pageSizeLabel.setText(_translate("ArkScanMainWindow", "Page Size:", None))
        self.m_resolutionLabel.setText(_translate("ArkScanMainWindow", "Resolution:", None))
        self.m_modeCombo.setItemText(0, _translate("ArkScanMainWindow", "Color", None))
        self.m_modeCombo.setItemText(1, _translate("ArkScanMainWindow", "Grayscale", None))
        self.m_modeCombo.setItemText(2, _translate("ArkScanMainWindow", "Line", None))
        self.m_modeLabel.setText(_translate("ArkScanMainWindow", "Mode:", None))
        self.m_xOriginLabel.setText(_translate("ArkScanMainWindow", "X:", None))
        self.m_yOriginLabel.setText(_translate("ArkScanMainWindow", "Y:", None))
        self.m_widthLabel.setText(_translate("ArkScanMainWindow", "W:", None))
        self.m_heightLabel.setText(_translate("ArkScanMainWindow", "H:", None))
        self.m_scanSizeLabel1.setText(_translate("ArkScanMainWindow", "0mm - 297mm", None))
        self.m_scanSizeLabel2.setText(_translate("ArkScanMainWindow", "0mm - 433mm", None))
        self.m_detectCropAreaButton.setText(_translate("ArkScanMainWindow", "Detect Crop Area", None))
        self.m_xCropLabel.setText(_translate("ArkScanMainWindow", "X:", None))
        self.m_yCropLabel.setText(_translate("ArkScanMainWindow", "Y:", None))
        self.m_wCropLabel.setText(_translate("ArkScanMainWindow", "W:", None))
        self.m_hCropLabel.setText(_translate("ArkScanMainWindow", "H:", None))
        self.m_pixelLabel1.setText(_translate("ArkScanMainWindow", "Pixels", None))
        self.m_pixelLabel2.setText(_translate("ArkScanMainWindow", "Pixels", None))
        self.m_cropButton.setText(_translate("ArkScanMainWindow", "Crop", None))
        self.m_menu.setTitle(_translate("ArkScanMainWindow", "ArkScan", None))
        self.m_quitAction.setText(_translate("ArkScanMainWindow", "Quit", None))

from ark_scan_graphics_view import ArkScanGraphicsView
