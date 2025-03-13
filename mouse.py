import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QEvent
import random

class MouseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.mainUI()

    def mainUI(self):
        width = 600
        height = 600
        self.setGeometry(100, 100, width, height)
        self.setWindowTitle("Tugas 2 Week 3 - Raizul Furkon (F1D0222024)")
        self.label = QLabel("x: 0, y: 0", self)
        self.label.setStyleSheet("""font-size: 14px; 
                                 font-weight: bold; 
                                 background-color: lightgray; 
                                 padding: 5px; 
                                 border-radius: 5px"""
                                )
        self.label.move(20, 20)
        self.label.setMinimumSize(100, 30)
        self.setMouseTracking(True)
        self.label.installEventFilter(self)
        self.label.setAttribute(Qt.WA_Hover, True)
    
    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        self.label.setText(f"x: {x}, y: {y}") 
        self.label.adjustSize()

    def eventFilter(self, obj, e):
        if obj == self.label and e.type() == QEvent.HoverEnter:
            maxHeight = self.width() - self.label.width()
            maxWidth = self.height() - self.label.height()

            new_x = random.randint(0, maxHeight)
            new_y = random.randint(0, maxWidth)
            self.label.move(new_x, new_y)
        return super().eventFilter(obj, e)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MouseWindow()
    window.show()
    sys.exit(app.exec_())

