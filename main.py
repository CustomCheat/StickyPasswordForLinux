import os


import PyQt5
from PyQt5.QtCore import QUrl

from PyQt5.QtWebEngineCore import QWebEngineHttpRequest
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import *
from PyQt5.QtWebEngine import *
from PyQt5.QtNetwork import *
from os.path import exists
import threading

import sys



class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()


        self.browser = QWebEngineView()
        profile = QWebEngineProfile("storage", self.browser)
        profile.setHttpUserAgent("Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0")
        profile.setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
        if not exists(str(os.getenv("HOME")) + "/.sticky"):
            os.mkdir(str(os.getenv("HOME")) + "/.sticky")
        profile.setCachePath(str(os.getenv("HOME")) + "/.sticky")
        profile.setPersistentStoragePath(str(os.getenv("HOME")) + "/.sticky")

        webpage = QWebEnginePage(profile, self.browser)
        self.browser.setPage(webpage)
        self.browser.load(QUrl("https://my.stickypassword.com/"))
        width = int(app.primaryScreen().size().width())
        heigth = int(app.primaryScreen().size().height())
        self.browser.setFixedSize(int(width / 1.5), int(heigth / 1.5))
        self.setFixedSize(int(width / 1.5), int(heigth / 1.5))



        self.setCentralWidget(self.browser)
        self.showMaximized()
        navbar = QToolBar()
        navbar.adjustSize()
        self.addToolBar(navbar)
        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)






app = QApplication(sys.argv)


QApplication.setApplicationName("Sticky Password")

window = MainWindow()



app.exec()
