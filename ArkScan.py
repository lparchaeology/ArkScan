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
        self.ui.m_saveButton.clicked.connect(self.save)
        self.ui.m_scanSaveButton.clicked.connect(self.scanSave)
        self.ui.m_allButton.clicked.connect(self.all)
        self.scanPixmap = QtGui.QPixmap('logo.png')
        self.scene = QtGui.QGraphicsScene(self)
        self.scanItem = self.scene.addPixmap(self.scanPixmap)
        self.ui.m_scanView.setScene(self.scene)

        self.savePath = '/home/odysseus/'

        self.process = QtCore.QProcess()
        self.process.started.connect(self.processStarted)
        self.process.finished.connect(self.processFinished)
        self.process.error.connect(self.processError)
        self.process.readyReadStandardError.connect(self.showProcessError)
        self.reader = QtGui.QImageReader(self.process)

    def showText(self, text):
        self.ui.m_outputText.append(text)

    def processStarted(self):
        self.showText('Scanning process started...')

    def processFinished(self):
        if (self.process.exitCode() == 0):
            self.showText('Loading scanned image')
            #image = QtGui.QImage.fromData(self.process.readAllStandardOutput())
            image = self.reader.read()
            if (image.isNull()):
                self.showText('Scanning failed: invalid image conversion')
            else:
                self.scanPixmap.convertFromImage(image)
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
        command = 'scanimage --mode Color --resolution 75'
        self.process.start(command)

    def defaultArea(self):
        return

    def scan(self):
        #command = 'scanimage --mode Color --resolution 300 --format=tiff -t 35 -y 330 > ' + filename
        command = 'scanimage --mode Color --resolution 300'
        self.process.setWorkingDirectory(self.savePath)
        self.process.start(command)
        #self.process.waitForStarted(-1);
        #self.process.waitForFinished(-1);

    def autocrop(self):
        return

    def save(self):
        filename = self.savePath + self.ui.m_siteEdit.text() + '_' + str(self.ui.m_eastSpin.value()) + '_' + str(self.ui.m_northSpin.value()) + '_' + '.png'
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
