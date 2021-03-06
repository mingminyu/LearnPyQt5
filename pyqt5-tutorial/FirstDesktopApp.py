# coding: utf8
# ===================================
# Author: yumingmin
# File: FirstDesktopApp.py
# Cate: PyQt5
# Create time: 2022/7/11 14:07
# Update time: 
# ===================================
import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    # 创建 QApplication 类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口的尺寸
    w.resize(400, 200)
    # 移动窗口
    w.move(300, 300)
    # 设置窗口的标题
    w.setWindowTitle("第一个基于PyQt5的桌面应用")
    # 显示窗口
    w.show()

    # 进入程序主循环，并通过 exit 函数确保主循环安全结束
    sys.exit(app.exec_())
