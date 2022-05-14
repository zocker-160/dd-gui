#!/usr/bin/env python3

# import modules
import os, os.path, sys, shutil
try:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
except:
    os.system("pip install PyQt5")
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *

# dd path
try:
    DD_PATH = sys.argv[1]
except:
    DD_PATH = "dd"

def browse_if():
    global IF_ISO
    try:
        IF_ISO = QFileDialog.getOpenFileName(WINDOW, "Open file", '.', "All files (*.*)")
    except:
        print("Unable to open file")

    INPUT_IF.setText(IF_ISO[0])

def browse_of():
    global OF_ISO
    try:
        OF_ISO = QFileDialog.getOpenFileName(WINDOW, "Open file", os.getcwd(), "All files (*.*)")
    except:
        print("Unable to open file")

    INPUT_OF.setText(OF_ISO[0])

def write_start():
    if not os.path.exists(INPUT_IF.text()):
        print("The input file does not exist")
        sys.exit(1)
    if CB_BS.isChecked() == True:
        WRITE_BS = f"bs={INPUT_BS.text()}"
    else:
        WRITE_BS = ""
    if CB_COUNT.isChecked() == True:
        WRITE_COUNT = f"count={INPUT_COUNT.text()}"
    else:
        WRITE_COUNT = ""
    if CB_SKIP.isChecked() == True:
        WRITE_SKIP = f"skip={INPUT_SKIP.text()}"
    else:
        WRITE_SKIP = ""
    if TEXT_CONV.isChecked() == True:
        WRITE_CONV = f"conv={DRP_CONV.currentText()}"
    else:
        WRITE_CONV = ""
    
    EXEC_CMD = f"{DD_PATH} if='{INPUT_IF.text()}' of='{INPUT_OF.text()}' {WRITE_BS} {WRITE_COUNT} {WRITE_SKIP} {WRITE_CONV}"
    print(f"Command to be executed: {EXEC_CMD}")
    
    os.system(EXEC_CMD)

def main():
    app = QApplication(sys.argv)
    
    global WINDOW, WIDTH, HEIGHT, CAPTION, INPUT_IF, INPUT_OF, STATUS, CB_BS, CB_COUNT, CB_SKIP, TEXT_CONV, INPUT_BS, INPUT_COUNT, INPUT_SKIP, DRP_CONV
    
    WIDTH = 500
    HEIGHT = 200
    CAPTION = "dd-gui v0.1"
    STATUS = "idle"
    
    WINDOW = QWidget()
    WINDOW.setGeometry(100,100,WIDTH,HEIGHT)
    WINDOW.setWindowTitle(CAPTION)
    
    TEXT_IF = QLabel(WINDOW)
    TEXT_IF.setText("Input file:")
    TEXT_IF.move(1,30)
    
    INPUT_IF = QLineEdit(WINDOW)
    INPUT_IF.resize(300,20)
    INPUT_IF.setText("/path/to/image.iso")
    INPUT_IF.move(WIDTH - 401,28)
    
    BUTT_IF = QPushButton(WINDOW)
    BUTT_IF.setText("Browse")
    BUTT_IF.resize(100,20)
    BUTT_IF.move(WIDTH - 100,28)
    BUTT_IF.clicked.connect(browse_if)
    
    TEXT_OF = QLabel(WINDOW)
    TEXT_OF.setText("Output file:")
    TEXT_OF.move(1,55)
    
    INPUT_OF = QLineEdit(WINDOW)
    INPUT_OF.resize(300,20)
    INPUT_OF.setText("/dev/sdXX")
    INPUT_OF.move(WIDTH - 401, 53)
    
    BUTT_OF = QPushButton(WINDOW)
    BUTT_OF.setText("Browse")
    BUTT_OF.resize(100,20)
    BUTT_OF.move(WIDTH - 100, 53)
    BUTT_OF.clicked.connect(browse_of)
    
    CB_BS = QCheckBox(WINDOW)
    CB_BS.setText("Block size:")
    CB_BS.move(1,75)
    
    INPUT_BS = QLineEdit(WINDOW)
    INPUT_BS.setText("1m")
    INPUT_BS.resize(100,20)
    INPUT_BS.move(WIDTH - 401,73)
    
    CB_COUNT = QCheckBox(WINDOW)
    CB_COUNT.setText("Count:")
    CB_COUNT.move(WIDTH - 300, 73)
    
    INPUT_COUNT = QLineEdit(WINDOW)
    INPUT_COUNT.setText("512")
    INPUT_COUNT.resize(100,20)
    INPUT_COUNT.move(WIDTH - 240, 73)
    
    CB_SKIP = QCheckBox(WINDOW)
    CB_SKIP.setText("Skip:")
    CB_SKIP.move(WIDTH - 139, 73)
    
    INPUT_SKIP = QLineEdit(WINDOW)
    INPUT_SKIP.setText("12")
    INPUT_SKIP.resize(90,20)
    INPUT_SKIP.move(WIDTH - 90, 73)
    
    TEXT_CONV = QCheckBox(WINDOW)
    TEXT_CONV.setText("Convert:")
    TEXT_CONV.move(1,95)
    
    DRP_CONV = QComboBox(WINDOW)
    DRP_CONV.resize(100,20)
    DRP_CONV.move(WIDTH - 401,95)
    DRP_CONV.addItem("ascii")
    DRP_CONV.addItem("block")
    DRP_CONV.addItem("ibm")
    DRP_CONV.addItem("fdatasync")
    DRP_CONV.addItem("fsync")
    DRP_CONV.addItem("lcase")
    DRP_CONV.addItem("pareven")
    DRP_CONV.addItem("noerror")
    DRP_CONV.addItem("notrunc")
    DRP_CONV.addItem("osync")
    DRP_CONV.addItem("sparse")
    DRP_CONV.addItem("swab")
    DRP_CONV.addItem("sync")
    DRP_CONV.addItem("ucase")
    DRP_CONV.addItem("unblock")
    
    BUTT_WRITE = QPushButton(WINDOW)
    BUTT_WRITE.setText("Write")
    BUTT_WRITE.resize(100,20)
    BUTT_WRITE.move(WIDTH - 100, HEIGHT - 20)
    BUTT_WRITE.clicked.connect(write_start)
    
    TEXT_STATUS = QLabel(WINDOW)
    TEXT_STATUS.setText(f"Status: {STATUS}")
    TEXT_STATUS.move(1,HEIGHT - 20)
    
    WINDOW.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
