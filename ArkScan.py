import sys
from PyQt4 import QtCore, QtGui
import ArkScanMainWindow

class ArkScan(QtGui.QMainWindow):
    def __init__(self):
        super(ArkScan, self).__init__()
        self.ui = ArkScanMainWindow.Ui_ArkScanMainWindow()
        self.ui.setupUi(self)
        self.ui.m_previewButton.clicked.connect(self.preview)
        self.ui.m_defaultButton.clicked.connect(self.defaultArea)
        self.ui.m_scanButton.clicked.connect(self.scan)
        self.ui.m_autocropButton.clicked.connect(self.autocrop)
        self.ui.m_autoscanButton.clicked.connect(self.autoscan)
        self.scanPixmap = QtGui.QPixmap('logo.png')
        self.scene = QtGui.QGraphicsScene(self)
        self.scanItem = self.scene.addPixmap(self.scanPixmap)
        self.ui.m_scanView.setScene(self.scene)

        self.savePath = '/filebin/Development/'
        self.saveName = 'test'

        self.process = QtCore.QProcess()
        self.process.started.connect(self.processStarted)
        self.process.finished.connect(self.processFinished)
        self.process.error.connect(self.processError)
        self.process.readyReadStandardError.connect(self.showProcessError)

    def showText(self, text):
        self.ui.m_outputText.append(text)

    def processStarted(self):
        self.showText('Scanning process started...')

    def processFinished(self):
        if (self.process.exitCode() == 0):
            self.showText('Scanning process finished OK!')
            output = self.process.readAllStandardOutput()
            image = QtGui.QImage.fromData(output)
            if (image.isNull()):
                self.showText('Invalid image conversion')
            else:
                self.scanPixmap.convertFromImage(image)
            #buffer = QtCore.QBuffer(output)
            #reader = QtGui.QImageReader(buffer, 'tiff')
            #img = reader.read()
            #if (img.isNull()):
            #    self.ui.m_outputText.append(reader.errorString())
        else:
            self.showText('Scanning process failed!')

    def processError(self):
        showProcessError()

    def showProcessOutput(self):
        self.showText(str(self.process.readAllStandardOutput()))

    def showProcessError(self):
        self.showText(str(self.process.readAllStandardError()))

    def preview(self):
        return

    def defaultArea(self):
        return

    def scan(self):
        filename = self.savePath + self.saveName + '.tiff'
        #command = 'scanimage --mode Color --resolution 300 --format=tiff -t 35 -y 330 > ' + filename
        args = ['--format=tiff', '-x 10', '-y 10']
        #args = ['--mode Color', '--resolution 300', '--format=tiff', '-t 35', '-y 330']
        self.process.setWorkingDirectory(self.savePath)
        #process.start(command)
        self.process.start('scanimage', args)
        self.process.waitForStarted(-1);
        self.process.waitForFinished(-1);

    def autocrop(self):
        return

    def autoscan(self):
        self.scan()
        self.autocrop()

app = QtGui.QApplication(sys.argv)

my_mainWindow = ArkScan()
my_mainWindow.show()

sys.exit(app.exec_())
