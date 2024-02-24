import sys
from PyQt5.QtWidgets import QMainWindow, QApplication , QPushButton , QLabel
from mainui import Ui_MainWindow
from PyQt5.QtGui import QPixmap, QIcon



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.dashboardbutton.setChecked(True)
        self.setWindowIcon(QIcon("C:/Users/4quin/OneDrive/Desktop/FinalThesisDesignShesh/LOGO/ACC_LOGO.jpg"))


      
      
    ##Qpush button chagne
    def on_stackedwidget_currentChanged(self, index):
        buttonlist = self.ui.icon_only_widget.findChildren(QPushButton) \
                     + self.ui.icons_details_widget.findChildren(QPushButton)
        
        
    ##funtion for changing  page
    def on_dashboardbutton_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashboardbutton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    
    def on_infobutton_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_infobutton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

              

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    window.setWindowTitle("Adaptive Classroom Control")
    
    sys.exit(app.exec())
