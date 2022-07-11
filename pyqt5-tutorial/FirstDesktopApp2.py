# coding: utf8
# ===================================
# Author: yumingmin
# File: FirstDesktopApp.py
# Cate: PyQt5
# Create time: 2022/7/11 14:07
# Update time: 
# ===================================
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from FirstAppUIWithQtDesigner import Ui_MainWindow


if __name__ == '__main__':
    # 创建 QApplication 类的实例
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    # 向主窗口上添加空间
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
