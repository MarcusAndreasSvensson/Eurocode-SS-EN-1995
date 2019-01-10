import sys
from PySide2.QtWidgets import QApplication, QLabel



app = QApplication(sys.argv)
label = QLabel("Hello World")
label.show()
sys.exit(app.exec_())

