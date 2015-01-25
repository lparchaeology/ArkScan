import sys
from enum import Enum
from PyQt4 import QtCore, QtGui
import ArkScanMainWindow

class ScanStatus(Enum):
    invalid = 0
    scanned = 1
    cropped = 2

class ArkScan(QtGui.QMainWindow):

    # Default settings
    #TODO load from QSettings
    scanSavePath = '/media/build/ark/'
    cropSavePath = '/media/build/ark/'
    defaultSite = 'MNO12'
    defaultEast = 100
    defaultNorth = 100
    defaultNumber = 1000
    defaultScanX = 0
    defaultScanY = 0
    defaultScanW = 215
    defaultScanH = 296

    # Internal flags
    useReader = False
    cropAfterScan = False
    saveAfterScan = False
    status = ScanStatus.invalid

    def __init__(self):
        super(ArkScan, self).__init__()
        self.ui = ArkScanMainWindow.Ui_ArkScanMainWindow()
        self.ui.setupUi(self)
        self.ui.m_siteEdit.setText(self.defaultSite)
        self.ui.m_eastSpin.setValue(self.defaultEast)
        self.ui.m_northSpin.setValue(self.defaultNorth)
        self.ui.m_numberSpin.setValue(self.defaultNumber)
        self.ui.m_previewButton.clicked.connect(self.preview)
        self.ui.m_defaultScanAreaButton.clicked.connect(self.defaultScanArea)
        self.defaultScanArea()
        self.ui.m_scanButton.clicked.connect(self.scan)
        self.ui.m_detectCropAreaButton.clicked.connect(self.detectCropArea)
        self.ui.m_cropButton.clicked.connect(self.crop)
        self.ui.m_saveButton.clicked.connect(self.save)
        self.ui.m_scanSaveButton.clicked.connect(self.scanSave)
        self.ui.m_allButton.clicked.connect(self.all)
        self.scanPixmap = QtGui.QPixmap('logo.png')
        self.scene = QtGui.QGraphicsScene(self)
        self.scanItem = self.scene.addPixmap(self.scanPixmap)
        self.ui.m_scanView.setScene(self.scene)
        #self.ui.m_scanView.setBackgroundBrush(QtGui.QBrush(QColor()))

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
        self.ui.m_siteEdit.setEnabled(status)
        self.ui.m_typeCombo.setEnabled(status)
        self.ui.m_numberSpin.setEnabled(status)
        self.ui.m_suffixEdit.setEnabled(status)
        self.ui.m_eastSpin.setEnabled(status)
        self.ui.m_northSpin.setEnabled(status)
        self.ui.m_previewButton.setEnabled(status)
        self.ui.m_defaultScanAreaButton.setEnabled(status)
        self.ui.m_xScanSpin.setEnabled(status)
        self.ui.m_yScanSpin.setEnabled(status)
        self.ui.m_hScanSpin.setEnabled(status)
        self.ui.m_wScanSpin.setEnabled(status)
        self.ui.m_scanButton.setEnabled(status)
        self.ui.m_detectCropAreaButton.setEnabled(status)
        self.ui.m_xCropSpin.setEnabled(status)
        self.ui.m_yCropSpin.setEnabled(status)
        self.ui.m_wCropSpin.setEnabled(status)
        self.ui.m_hCropSpin.setEnabled(status)
        self.ui.m_cropButton.setEnabled(status)
        self.ui.m_saveButton.setEnabled(status)
        self.ui.m_scanSaveButton.setEnabled(status)
        self.ui.m_allButton.setEnabled(status)

    def updatePixmap(self):
        self.scanItem.setPixmap(self.scanPixmap)
        self.scene.setSceneRect(QtCore.QRectF(self.scanPixmap.rect()))
        #TODO Zoom to fit
        self.scene.update()
        self.ui.m_scanView.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        self.defaultCropArea()

    def planName(self):
        name = self.ui.m_siteEdit.text() + '_'
        #TODO Use data?
        if (self.ui.m_typeCombo.currentText() == 'Context'):
            name += 'C'
        elif (self.ui.m_typeCombo.currentText() == 'Plan'):
            name += 'P'
        elif (self.ui.m_typeCombo.currentText() == 'Section'):
            name += 'S'
        elif (self.ui.m_typeCombo.currentText() == 'Matrix'):
            name += 'M'
        name += str(self.ui.m_numberSpin.value())
        if (self.ui.m_suffixEdit.text() and self.ui.m_suffixEdit.text() != ' '):
            name += self.ui.m_suffixEdit.text()
        if (self.ui.m_eastSpin.value() != 0 and self.ui.m_northSpin.value() != 0):
            name += '_E'
            name += str(self.ui.m_eastSpin.value())
            name += '_N'
            name += str(self.ui.m_northSpin.value())
        return name

    def showText(self, text):
        self.ui.m_outputText.append(text)

    def scanProcessStarted(self):
        self.showText('Scanning image...')

    def scanProcessEnded(self):
        if (self.scanProcess.exitCode() != 0):
            self.showText('Scanning image failed!')
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
            self.status = ScanStatus.scanned
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

    def preview(self):
        self.enableUi(False)
        self.status = ScanStatus.invalid
        command = 'scanimage --mode Color --resolution 75'
        #command = 'scanimage --mode Color --resolution 75 --lamp-off-at-exit=no'
        if (not self.useReader):
            # PNM unsupported so write to temp file instead as TIFF can't be streamed
            self.scanProcess.setStandardOutputFile('temp.tiff')
            command += ' --format=tiff'
        self.scanProcess.start(command)

    def defaultScanArea(self):
        self.ui.m_xScanSpin.setValue(self.defaultScanX)
        self.ui.m_yScanSpin.setValue(self.defaultScanY)
        self.ui.m_wScanSpin.setValue(self.defaultScanW)
        self.ui.m_hScanSpin.setValue(self.defaultScanH)

    def scan(self):
        self.enableUi(False)
        self.status = ScanStatus.invalid
        scanRect = QtCore.QRect(self.ui.m_xScanSpin.value(), self.ui.m_yScanSpin.value(), self.ui.m_wScanSpin.value(), self.ui.m_hScanSpin.value())
        command = 'scanimage --mode Color --resolution 300 -l%d -t%d -x%d -y%d' % (scanRect.x(), scanRect.y(), scanRect.width(), scanRect.height())
        #command = 'scanimage --mode Color --resolution 300 --lamp-off-at-exit=no -l%d -t%d -x%d -y%d' % (scanRect.x(), scanRect.y(), scanRect.width(), scanRect.height())
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
        if (self.status == ScanStatus.invalid):
            return
        self.enableUi(False)
        if (self.scanPixmap.save('temp_crop.png', 'PNG')):
            command = "convert temp_crop.png -virtual-pixel edge -blur 0X15 -fuzz 10% -trim -format '%w+%h%O' info:"
            self.cropProcess.start(command)
        else:
            self.showText('Detect crop area failed, could not write temp file!')

    def crop(self):
        self.enableUi(False)
        if (self.status == ScanStatus.invalid):
            return
        self.enableUi(False)
        cropRect = QtCore.QRect(self.ui.m_xCropSpin.value(), self.ui.m_yCropSpin.value(), self.ui.m_wCropSpin.value(), self.ui.m_hCropSpin.value())
        self.scanPixmap = self.scanPixmap.copy(cropRect)
        self.updatePixmap()
        if (self.saveAfterScan):
            self.saveAfterScan = False
            self.save()
        else:
            self.enableUi(True)

    def save(self):
        self.enableUi(False)
        if (self.status == ScanStatus.invalid):
            return
        filename = ''
        if (self.status == ScanStatus.scanned):
            filename = self.scanSavePath
        else:
            filename = self.cropSavePath
        filename = filename + self.planName() + '.png'
        if (self.scanPixmap.save(filename, 'PNG')):
            self.showText('Image saved as ' + filename)
        else:
            self.showText('Image save as ' + filename + ' failed!')
        self.enableUi(True)

    def scanSave(self):
        self.saveAfterScan = True
        self.scan()

    def all(self):
        self.saveAfterScan = True
        self.cropAfterScan = True
        self.scan()

app = QtGui.QApplication(sys.argv)

my_mainWindow = ArkScan()
my_mainWindow.show()

sys.exit(app.exec_())
