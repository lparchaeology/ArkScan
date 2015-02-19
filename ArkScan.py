import sys
from PyQt4 import QtCore, QtGui
import ArkScanMainWindow

class ArkScan(QtGui.QMainWindow):

    # Default settings
    #TODO load from QSettings
    scanSavePath = '/filebin/1120L - 100 Minories/GIS/plans/incoming/scans/'
    cropSavePath = '/filebin/1120L - 100 Minories/GIS/plans/incoming/raw/'
    defaultSite = 'MNO12'
    defaultType = 'Context'
    defaultEast = 100
    defaultNorth = 100
    defaultNumber = 1000
    defaultSuffix = ''
    defaultMode = 'Color'
    defaultPageSize = 'Permatrace'
    defaultResolution = '300'
    defaultOrientation = 'Portrait'
    defaultOriginX = 0
    defaultOriginY = 39
    defaultWidth = 290
    defaultHeight = 320
    permatraceOriginX = 0
    permatraceOriginY = 39
    permatraceWidth = 290
    permatraceHeight = 320

    # Internal flags
    useReader = False
    cropAfterScan = False
    saveAfterScan = False
    status = 'invalid'

    def __init__(self):
        super(ArkScan, self).__init__()
        self.ui = ArkScanMainWindow.Ui_ArkScanMainWindow()
        self.ui.setupUi(self)
        self.applyDefaultSettings()
        self.setupUi()
        self.setupProcess()
        self.enableUi(True)

    # Setup methods

    def applyDefaultSettings(self):
        self.ui.m_siteEdit.setText(self.defaultSite)
        i = self.ui.m_typeCombo.findText(self.defaultType)
        self.ui.m_typeCombo.setCurrentIndex(i)
        self.ui.m_numberSpin.setValue(self.defaultNumber)
        self.ui.m_eastSpin.setValue(self.defaultEast)
        self.ui.m_northSpin.setValue(self.defaultNorth)
        self.ui.m_suffixEdit.setText(self.defaultSuffix)

        i = self.ui.m_modeCombo.findText(self.defaultMode)
        self.ui.m_modeCombo.setCurrentIndex(i)
        i = self.ui.m_resolutionCombo.findText(self.defaultResolution)
        self.ui.m_resolutionCombo.setCurrentIndex(i)
        i = self.ui.m_pageSizeCombo.findText(self.defaultPageSize)
        self.ui.m_pageSizeCombo.setCurrentIndex(i)
        i = self.ui.m_orientationCombo.findText(self.defaultOrientation)
        self.ui.m_orientationCombo.setCurrentIndex(i)
        self.ui.m_xOriginSpin.setValue(self.defaultOriginX)
        self.ui.m_yOriginSpin.setValue(self.defaultOriginY)
        self.ui.m_widthSpin.setValue(self.defaultWidth)
        self.ui.m_heightSpin.setValue(self.defaultHeight)

    def setupUi(self):
        self.ui.m_previewButton.clicked.connect(self.preview)
        self.ui.m_scanButton.clicked.connect(self.scan)
        self.ui.m_saveButton.clicked.connect(self.save)
        self.ui.m_printButton.clicked.connect(self.printScan)
        self.ui.m_copyButton.clicked.connect(self.copy)

        self.ui.m_typeCombo.activated.connect(self.typeChanged)
        self.ui.m_savePlanButton.clicked.connect(self.savePlan)
        self.ui.m_scanSavePlanButton.clicked.connect(self.scanSavePlan)
        self.ui.m_scanCropSavePlanButton.clicked.connect(self.scanCropSavePlan)

        self.ui.m_pageSizeCombo.activated.connect(self.pageSizeChanged)
        self.ui.m_orientationCombo.activated.connect(self.orientationChanged)

        self.ui.m_detectCropAreaButton.clicked.connect(self.detectCropArea)
        self.ui.m_cropButton.clicked.connect(self.crop)

        self.scanPixmap = QtGui.QPixmap('logo.png')
        self.scene = QtGui.QGraphicsScene(self)
        self.scanItem = self.scene.addPixmap(self.scanPixmap)
        self.ui.m_scanView.setScene(self.scene)
        self.scene.setSceneRect(QtCore.QRectF(self.scanPixmap.rect()))
        self.scene.update()
        self.zoomToFit()
        #self.ui.m_scanView.setBackgroundBrush(QtGui.QBrush(QColor()))

    def setupProcess(self):
        self.scanProcess = QtCore.QProcess()
        self.scanProcess.started.connect(self.scanProcessStarted)
        self.scanProcess.finished.connect(self.scanProcessEnded)
        self.scanProcess.error.connect(self.scanProcessError)
        self.scanProcess.readyReadStandardError.connect(self.scanProcessError)
        self.showText('Supported Image Formats:')
        formats = ' '
        for format in QtGui.QImageReader.supportedImageFormats():
            formats += str(format)
            formats += ' '
        self.showText(formats)
        #TODO if list contains pnm then enable reader
        if (self.useReader):
            self.reader = QtGui.QImageReader(self.scanProcess)

        self.cropProcess = QtCore.QProcess()
        self.cropProcess.started.connect(self.cropProcessStarted)
        self.cropProcess.finished.connect(self.cropProcessEnded)
        self.cropProcess.error.connect(self.cropProcessError)
        self.cropProcess.readyReadStandardError.connect(self.cropProcessError)

    def enableUi(self, status):
        self.ui.m_previewButton.setEnabled(status)
        self.ui.m_scanButton.setEnabled(status)
        self.ui.m_saveButton.setEnabled(status)
        self.ui.m_printButton.setEnabled(status)
        self.ui.m_copyButton.setEnabled(status)

        self.ui.m_siteEdit.setEnabled(status)
        self.ui.m_typeCombo.setEnabled(status)
        if status:
            self.typeChanged(self.ui.m_typeCombo.currentText())
        else:
            self.ui.m_numberSpin.setEnabled(status)
        self.ui.m_suffixEdit.setEnabled(status)
        self.ui.m_eastSpin.setEnabled(status)
        self.ui.m_northSpin.setEnabled(status)
        self.ui.m_savePlanButton.setEnabled(status)
        self.ui.m_savePlanButton.setEnabled(status)
        self.ui.m_scanSavePlanButton.setEnabled(status)
        self.ui.m_scanCropSavePlanButton.setEnabled(status)

        self.ui.m_modeCombo.setEnabled(status)
        self.ui.m_resolutionCombo.setEnabled(status)
        self.ui.m_pageSizeCombo.setEnabled(status)
        self.ui.m_orientationCombo.setEnabled(status)
        self.ui.m_xOriginSpin.setEnabled(status)
        self.ui.m_yOriginSpin.setEnabled(status)
        self.ui.m_heightSpin.setEnabled(status)
        self.ui.m_widthSpin.setEnabled(status)

        self.ui.m_detectCropAreaButton.setEnabled(status)
        self.ui.m_xCropSpin.setEnabled(status)
        self.ui.m_yCropSpin.setEnabled(status)
        self.ui.m_wCropSpin.setEnabled(status)
        self.ui.m_hCropSpin.setEnabled(status)
        self.ui.m_cropButton.setEnabled(status)

        if (status):
            self.ui.m_progressBar.setRange(0, 100)
        else:
            self.ui.m_progressBar.setRange(0, 0)

    # Utility methods

    def showText(self, text):
        self.ui.m_outputText.append(text)

    def updatePixmap(self):
        self.scanItem.setPixmap(self.scanPixmap)
        self.scene.setSceneRect(QtCore.QRectF(self.scanPixmap.rect()))
        self.scene.update()
        self.zoomToFit()
        self.defaultCropArea()

    def zoomToFit(self):
        self.ui.m_scanView.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)

    # General scanning methods

    def preview(self):
        self.doPreview()

    def scan(self):
        self.doScan()

    def save(self):
        saveFileName = QtGui.QFileDialog.getSaveFileName(self, 'Save Image As', '', "Images (*.png *.jpg *.tiff);;Documents (*.pdf)")
        saveFileInfo = QtCore.QFileInfo(saveFileName)
        if saveFileInfo.exists():
            result = QtGui.QMessageBox.warning(None, 'File Already Exists!', 'The chosen file already exists. Do you want to overwrite it?', QtGui.QMessageBox.Save | QtGui.QMessageBox.Cancel)
            if (result != QtGui.QMessageBox.Save):
                return
        format = saveFileInfo.suffix().toUpper()
        if format == 'PDF':
            pass
        elif self.scanPixmap.save(saveFileName, format):
            self.showText('Image saved as ' + saveFileName)
        else:
            self.showText('Image save as ' + saveFileName + ' failed!')

    def printScan(self):
        printer = QtGui.QPrinter()
        dialog = QtGui.QPrintDialog(printer, self)
        if (dialog.exec_() == QtGui.QDialog.Accepted):
            painter = QtGui.QPainter()
            painter.begin(printer)
            painter.drawPixmap(0, 0, self.scanPixmap)
            painter.end()

    def copy():
        self.scan()
        self.printScan()

    # Context Plan methods

    def typeChanged(self, newText):
        if (newText == 'Top Plan' or newText == 'Matrix'):
            self.ui.m_numberSpin.setEnabled(False)
        else:
            self.ui.m_numberSpin.setEnabled(True)

    def savePlan(self):
        if (self.status == 'invalid'):
            return
        self.enableUi(False)
        filename = ''
        if (self.status == 'scanned'):
            filename = self.scanSavePath
        else:
            filename = self.cropSavePath
        filename = filename + self.planName() + '.png'
        ok = True
        if (QtCore.QFileInfo(filename).exists()):
            result = QtGui.QMessageBox.warning(None, 'File Already Exists!', 'The chosen scan file already exists. Do you want to overwrite it?', QtGui.QMessageBox.Save | QtGui.QMessageBox.Cancel)
            if (result != QtGui.QMessageBox.Save):
                ok = False
        if (ok and self.scanPixmap.save(filename, 'PNG')):
            self.showText('Image saved as ' + filename)
        else:
            self.showText('Image save as ' + filename + ' failed!')
        self.enableUi(True)

    def scanSavePlan(self):
        self.saveAfterScan = True
        self.scan()

    def scanCropSavePlan(self):
        self.saveAfterScan = True
        self.cropAfterScan = True
        self.scan()

    def planName(self):
        name = self.ui.m_siteEdit.text() + '_'
        #TODO Use data?
        useNumber = True
        if (self.ui.m_typeCombo.currentText() == 'Context'):
            pass
        elif (self.ui.m_typeCombo.currentText() == 'Plan'):
            name += 'P'
        elif (self.ui.m_typeCombo.currentText() == 'Section'):
            name += 'S'
        elif (self.ui.m_typeCombo.currentText() == 'Top Plan'):
            name += 'TP'
            useNumber = False
        elif (self.ui.m_typeCombo.currentText() == 'Matrix'):
            name += 'Matrix'
            useNumber = False
        if (useNumber and self.ui.m_numberSpin.value() > 0):
            name += str(self.ui.m_numberSpin.value())
        if (self.ui.m_eastSpin.value() != 0 and self.ui.m_northSpin.value() != 0):
            name += '_E'
            name += str(self.ui.m_eastSpin.value())
            name += '_N'
            name += str(self.ui.m_northSpin.value())
        if (self.ui.m_suffixEdit.text() and self.ui.m_suffixEdit.text() != ' '):
            name += '_'
            name += self.ui.m_suffixEdit.text()
        return name

    # Scan options methods
        self.ui.m_pageSizeCombo.activated.connect(self.pageSizeChanged)
        self.ui.m_orientationCombo.activated.connect(self.orientationChanged)

    def pageSizeChanged(self):
        pass

    def orientationChanged(self):
        pass

    # Scan process methods

    def scanProcessStarted(self):
        self.showText('Scanning image...')

    def scanProcessEnded(self):
        if (self.scanProcess.exitCode() != 0):
            self.showText('Scanning image failed!')
            self.enableUi(True)
            return

        image = QtGui.QImage()
        if (self.useReader):
            image = self.reader.read()
        else:
            #image = QtGui.QImage.fromData(self.scanProcess.readAllStandardOutput())
            image.load('temp.tiff')
        if (image.isNull()):
            self.showText('Scanning failed: invalid image conversion')
        else:
            if (self.useReader):
                self.scanPixmap.convertFromImage(image)
            else:
                self.scanPixmap.load('temp.tiff')
            self.updatePixmap()
            self.status = 'scanned'
            self.showText('Scanning image completed!')
            if (self.cropAfterScan):
                self.detectCropArea()
            elif (self.saveAfterScan):
                self.saveAfterScan = False
                self.save()
        self.enableUi(True)

    def scanProcessError(self):
        self.showProcessError(self.scanProcess)

    def cropProcessStarted(self):
        self.showText('Detecting crop area...')

    def cropProcessEnded(self):
        if (self.cropProcess.exitCode() != 0):
            self.showText('Detecting crop area failed!')
            self.enableUi(True)
            return

        info = str(self.cropProcess.readAllStandardOutput())
        self.showText(info)
        # Format is W+H+X+Y
        info = info.strip("'")
        info = info.replace('+', ',')
        dim = info.split(',')
        self.ui.m_wCropSpin.setValue(int(dim[0]))
        self.ui.m_hCropSpin.setValue(int(dim[1]))
        self.ui.m_xCropSpin.setValue(int(dim[2]))
        self.ui.m_yCropSpin.setValue(int(dim[3]))
        #TODO draw rubber band
        self.showText('Detecting crop area completed!')
        if (self.cropAfterScan):
            cropAfterScan = False
            self.crop()
        self.enableUi(True)

    def cropProcessError(self):
        self.showProcessError(self.cropProcess)

    def showProcessError(self, process):
        self.showText(str(process.readAllStandardError()))

    def doPreview(self):
        self.enableUi(False)
        self.status = 'invalid'
        command = 'scanimage --mode Color --resolution 75 --lamp-off-at-exit=no'
        if (not self.useReader):
            # PNM unsupported so write to temp file instead as TIFF can't be streamed
            self.scanProcess.setStandardOutputFile('temp.tiff')
            command += ' --format=tiff'
        self.scanProcess.start(command)

    def setPermatraceScanArea(self):
        self.ui.m_xOriginSpin.setValue(self.permatraceOriginX)
        self.ui.m_yOriginSpin.setValue(self.permatraceOriginY)
        self.ui.m_widthSpin.setValue(self.permatraceWidth)
        self.ui.m_heightSpin.setValue(self.permatraceHeight)

    def doScan(self):
        self.enableUi(False)
        self.status = 'invalid'
        scanRect = QtCore.QRect(self.ui.m_xOriginSpin.value(), self.ui.m_yOriginSpin.value(), self.ui.m_widthSpin.value(), self.ui.m_heightSpin.value())
        command = 'scanimage --mode Color --resolution 300 --lamp-off-at-exit=no -l%d -t%d -x%d -y%d' % (scanRect.x(), scanRect.y(), scanRect.width(), scanRect.height())
        if (not self.useReader):
            # PNM unsupported so write to temp file instead as TIFF can't be streamed
            self.scanProcess.setStandardOutputFile('temp.tiff')
            command += ' --format=tiff'
        self.scanProcess.start(command)

    def defaultCropArea(self):
        self.ui.m_xCropSpin.setMaximum(self.scanPixmap.width())
        self.ui.m_xCropSpin.setValue(0)
        self.ui.m_yCropSpin.setMaximum(self.scanPixmap.height())
        self.ui.m_yCropSpin.setValue(0)
        self.ui.m_wCropSpin.setMaximum(self.scanPixmap.width())
        self.ui.m_wCropSpin.setValue(self.scanPixmap.width())
        self.ui.m_hCropSpin.setMaximum(self.scanPixmap.height())
        self.ui.m_hCropSpin.setValue(self.scanPixmap.height())

    def detectCropArea(self):
        if (self.status == 'invalid'):
            return
        self.enableUi(False)
        if (self.scanPixmap.save('temp_crop.png', 'PNG')):
            command = "convert temp_crop.png -virtual-pixel edge -blur 0X15 -fuzz 10% -trim -format '%w+%h%O' info:"
            self.cropProcess.start(command)
        else:
            self.showText('Detect crop area failed, could not write temp file!')

    def crop(self):
        if (self.status == 'invalid'):
            return
        self.enableUi(False)
        self.enableUi(False)
        cropRect = QtCore.QRect(self.ui.m_xCropSpin.value(), self.ui.m_yCropSpin.value(), self.ui.m_wCropSpin.value(), self.ui.m_hCropSpin.value())
        self.scanPixmap = self.scanPixmap.copy(cropRect)
        self.updatePixmap()
        if (self.saveAfterScan):
            self.saveAfterScan = False
            self.save()
        else:
            self.enableUi(True)

# Application level code

app = QtGui.QApplication(sys.argv)

my_mainWindow = ArkScan()
my_mainWindow.show()

sys.exit(app.exec_())
