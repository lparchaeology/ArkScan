import sys
from enum import Enum
from PyQt4 import QtCore, QtGui
import ArkScanMainWindow

class ScanStatus(Enum):
    invalid = 0
    scanned = 1
    cropped = 2

class ArkScan(QtGui.QMainWindow):

    useReader = False
    status = ScanStatus.invalid

    def __init__(self):
        super(ArkScan, self).__init__()
        self.ui = ArkScanMainWindow.Ui_ArkScanMainWindow()
        self.ui.setupUi(self)
        self.ui.m_siteEdit.setText('MNO12')
        self.ui.m_eastSpin.setValue(100)
        self.ui.m_northSpin.setValue(100)
        self.ui.m_numberSpin.setValue(1000)
        self.ui.m_previewButton.clicked.connect(self.preview)
        self.ui.m_defaultButton.clicked.connect(self.defaultArea)
        self.defaultArea()
        self.ui.m_scanButton.clicked.connect(self.scan)
        self.ui.m_autocropButton.clicked.connect(self.autocrop)
        self.ui.m_saveButton.clicked.connect(self.save)
        self.ui.m_scanSaveButton.clicked.connect(self.scanSave)
        self.ui.m_allButton.clicked.connect(self.all)
        self.scanPixmap = QtGui.QPixmap('logo.png')
        self.scene = QtGui.QGraphicsScene(self)
        self.scanItem = self.scene.addPixmap(self.scanPixmap)
        self.ui.m_scanView.setScene(self.scene)

        self.scanSavePath = '/filebin/Development/'
        self.cropSavePath = '/filebin/Development/'

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
        self.showText('Scanning process started...')

    def scanProcessEnded(self):
        if (self.scanProcess.exitCode() == 0):
            self.showText('Loading scanned image')
            image = QtGui.QImage()
            if (self.useReader):
                image = self.reader.read()
            else:
                #image = QtGui.QImage.fromData(self.scanProcess.readAllStandardOutput())
                self.showText('about to load')
                image.load('temp.tiff')
                self.showText('loaded')
            if (image.isNull()):
                self.showText('Scanning failed: invalid image conversion')
            else:
                self.showText('about to convert')
                if (self.useReader):
                    self.scanPixmap.convertFromImage(image)
                else:
                    self.scanPixmap.load('temp.tiff')
                self.scanItem.setPixmap(self.scanPixmap)
                self.scene.setSceneRect(QtCore.QRectF(self.scanPixmap.rect()))
                self.scene.update()
                self.status = ScanStatus.scanned
                self.showText('Scanning process finished OK!')
        else:
            self.showText('Scanning process failed!')

    def scanProcessError(self):
        self.showProcessError(self.scanProcess)

    def cropProcessStarted(self):
        self.showText('Auto-crop process started...')

    def cropProcessEnded(self):
        return

    def cropProcessError(self):
        self.showProcessError(self.cropProcess)

    def showProcessOutput(self, process):
        self.showText(str(process.readAllStandardOutput()))

    def showProcessError(self, process):
        self.showText(str(process.readAllStandardError()))

    def preview(self):
        self.status = ScanStatus.invalid
        command = 'scanimage --mode Color --resolution 75 --lamp-off-at-exit=no'
        if (not self.useReader):
            # PNM unsupported so write to temp file instead as TIFF can't be streamed
            self.scanProcess.setStandardOutputFile('temp.tiff')
            command += ' --format=tiff'
        self.scanProcess.start(command)

    def defaultArea(self):
        self.ui.m_xSpin.setValue(0)
        self.ui.m_ySpin.setValue(35)
        self.ui.m_wSpin.setValue(297)
        self.ui.m_hSpin.setValue(330)

    def scan(self):
        self.status = ScanStatus.invalid
        command = 'scanimage --mode Color --resolution 300 --lamp-off-at-exit=no -l%d -t%d -x%d -y%d' % (self.ui.m_xSpin.value(), self.ui.m_ySpin.value(), self.ui.m_wSpin.value(), self.ui.m_hSpin.value())
        if (not self.useReader):
            # PNM unsupported so write to temp file instead as TIFF can't be streamed
            self.scanProcess.setStandardOutputFile('temp.tiff')
            command += ' --format=tiff'
        self.scanProcess.start(command)

    def autocrop(self):
        #if (self.status != ScanStatus.invalid):
            command = "convert temp.tiff -virtual-pixel edge -blur 0X15 -fuzz 10% -trim -format '%wx%h%O' info:"
            self.cropProcess.start(command)
            self.cropProcess.waitForStarted(-1)
            self.cropProcess.waitForFinished(-1)
            if (self.cropProcess.exitCode() != 0):
                return
            size = str(self.cropProcess.readAllStandardOutput())
            self.showText(size)
            size = size.translate(None, "'")
            command = "convert temp.tiff -crop %s +repage temp_crop.tiff" % size
            self.showText(command)
            #command = "convert temp.tiff -virtual-pixel edge -blur 0X15 -fuzz 10% -trim -format '%wx%h%O' info:"
            self.cropProcess.start(command)
            self.cropProcess.waitForStarted(-1)
            self.cropProcess.waitForFinished(-1)
            if (self.cropProcess.exitCode() == 0):
                self.showText('Loading cropped image')
                self.scanPixmap.load('temp_crop.tiff')
                self.scanItem.setPixmap(self.scanPixmap)
                self.scene.setSceneRect(QtCore.QRectF(self.scanPixmap.rect()))
                self.scene.update()
                self.showText('Auto-crop process finished OK!')
                self.status = ScanStatus.scanned
            else:
                self.showText('Auto-crop process failed!')

    def save(self):
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

    def scanSave(self):
        self.scan()
        self.save()

    def all(self):
        self.scan()
        self.autocrop()
        self.save()

app = QtGui.QApplication(sys.argv)

my_mainWindow = ArkScan()
my_mainWindow.show()

sys.exit(app.exec_())
