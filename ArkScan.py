import sys
from PyQt4 import QtCore, QtGui
import ArkScanMainWindow

class ArkScan(QtGui.QMainWindow):

    useReader = False

    def __init__(self):
        super(ArkScan, self).__init__()
        self.ui = ArkScanMainWindow.Ui_ArkScanMainWindow()
        self.ui.setupUi(self)
        self.ui.m_siteEdit.setText('MNO12')
        self.ui.m_eastSpin.setValue(100)
        self.ui.m_northSpin.setValue(100)
        self.ui.m_contextSpin.setValue(1000)
        self.ui.m_previewButton.clicked.connect(self.preview)
        self.ui.m_defaultButton.clicked.connect(self.defaultArea)
        self.ui.m_scanButton.clicked.connect(self.scan)
        self.ui.m_autocropButton.clicked.connect(self.autocrop)
        self.ui.m_saveButton.clicked.connect(self.save)
        self.ui.m_scanSaveButton.clicked.connect(self.scanSave)
        self.ui.m_allButton.clicked.connect(self.all)
        self.scanPixmap = QtGui.QPixmap('logo.png')
        self.scene = QtGui.QGraphicsScene(self)
        self.scanItem = self.scene.addPixmap(self.scanPixmap)
        self.ui.m_scanView.setScene(self.scene)

        self.savePath = '/filebin/Development/'

        self.process = QtCore.QProcess()
        self.process.started.connect(self.processStarted)
        self.process.finished.connect(self.processFinished)
        self.process.error.connect(self.processError)
        self.process.readyReadStandardError.connect(self.showProcessError)
        self.showText('Supported Image Formats:')
        formats = ' '
        for format in QtGui.QImageReader.supportedImageFormats():
            formats += str(format)
            formats += ' '
        self.showText(formats)
        #TODO if list contains pnm then enable reader
        if (self.useReader):
            self.reader = QtGui.QImageReader(self.process)

    def showText(self, text):
        self.ui.m_outputText.append(text)

    def processStarted(self):
        self.showText('Scanning process started...')

    def processFinished(self):
        if (self.process.exitCode() == 0):
            self.showText('Loading scanned image')
            image = QtGui.QImage()
            if (self.useReader):
                image = self.reader.read()
            else:
                #image = QtGui.QImage.fromData(self.process.readAllStandardOutput())
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
                self.showText('Scanning process finished OK!')
        else:
            self.showText('Scanning process failed!')

    def processError(self):
        showProcessError()

    def showProcessOutput(self):
        self.showText(str(self.process.readAllStandardOutput()))

    def showProcessError(self):
        self.showText(str(self.process.readAllStandardError()))

    def preview(self):
        command = ''
        if (self.useReader):
            command = 'scanimage --mode Color --resolution 75'
        else:
            self.process.setStandardOutputFile('temp.tiff')
            command = 'scanimage --mode Color --resolution 75 --format=tiff'
        self.process.start(command)

    def defaultArea(self):
        return

    def scan(self):
        #command = 'scanimage --mode Color --resolution 300 --format=tiff -t 35 -y 330 > ' + filename
        command = ''
        if (self.useReader):
            command = 'scanimage --mode Color --resolution 300'
        else:
            self.process.setStandardOutputFile('temp.tiff')
            command = 'scanimage --mode Color --resolution 300 --format=tiff'
        self.process.start(command)
        #self.process.waitForStarted(-1);
        #self.process.waitForFinished(-1);

    def autocrop(self):
        command = "convert temp.tiff -crop `convert temp.tiff -virtual-pixel edge -blur 0x15 -fuzz 10% -trim -format '%wx%h%O' info:` +repage temp_crop.png"
        process = QtCore.QProcess(command)
        process.
        return

    def save(self):
        filename = self.savePath + self.ui.m_siteEdit.text() + '_' + str(self.ui.m_eastSpin.value()) + '_' + str(self.ui.m_northSpin.value()) + '.png'
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
