#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import eiscp
import signal
import platform
import logging
import logging.handlers
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QSettings, Qt, QCoreApplication, QTimer
from PyQt5.QtGui import QIcon, QKeySequence, QWheelEvent
from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox, QComboBox,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QMessageBox, QMenu, QPushButton, QSpinBox, QStyle, QSystemTrayIcon,
        QTextEdit, QVBoxLayout, QWidget, QShortcut, QMainWindow, QTabWidget, QFormLayout)

try:
	import about_dlg
	import settings
except:
	from onkyoqt import settings
	from onkyoqt import about_dlg

signal.signal(signal.SIGINT, signal.SIG_DFL)

class Onkyo(QMainWindow):

	def __init__(self):
		super(Onkyo, self).__init__()
		self.initUI()
		self.settings = QSettings('onkyoqt', 'settings')
		self.host = self.settings.value('host', type=str)
		self.receiver = eiscp.eISCP(self.host)

	def btn_inputpc_click(self):
		try:
			self.receiver.command('input-selector=pc')
		except Exception as e:
			self.createTrayError(e)

	def btn_inputusb_click(self):
		try:
			self.receiver.command('input-selector=usb')
		except Exception as e:
			self.createTrayError(e)

	def btn_volumeup_click(self):
		try:
			volume_now = self.receiver.command('volume=level-up')
			self.sendTextToStatusBar(volume_now)
		except Exception as e:
			self.createTrayError(e)

	def btn_volumedown_click(self):
		try:
			volume_now = self.receiver.command('volume=level-down')
			self.sendTextToStatusBar(volume_now)
		except Exception as e:
			self.createTrayError(e)

	def btn_usbstop_click(self):
		try:
			self.receiver.command('network-usb=stop')
		except Exception as e:
			self.createTrayError(e)

	def btn_usbplay_click(self):
		try:
			self.receiver.command('network-usb=play')
		except Exception as e:
			self.createTrayError(e)

	def btn_usbpause_click(self):
		try:
			self.receiver.command('network-usb=pause')
		except Exception as e:
			self.createTrayError(e)

	def btn_usbprew_click(self):
		try:
			self.receiver.command('network-usb=trdn')
		except Exception as e:
			self.createTrayError(e)

	def btn_usbnext_click(self):
		try:
			self.receiver.command('network-usb=trup')
		except Exception as e:
			self.createTrayError(e)

	def btn_poweroff_click(self):
		try:
			self.receiver.command('system-power=standby')
		except Exception as e:
			pass

	def btn_mute_click(self):
		try:
			volume_now = self.receiver.command('volume=0')
			self.sendTextToStatusBar(volume_now)
		except Exception as e:
			self.createTrayError(e)

	def initUI(self):

		self.settings = QSettings('onkyoqt', 'settings')
		self.hide_window = self.settings.value('hide') or 'False'
		self.hide_window = eval(self.hide_window)

		self.btn_inputpc = QPushButton('PC', self)
		self.btn_inputusb = QPushButton('USB', self)
		self.btn_volumeup = QPushButton('Vol +', self)
		self.btn_volumedown = QPushButton('Vol -', self)
		self.btn_usbstop = QPushButton('Stop', self)
		self.btn_usbplay = QPushButton('Play', self)
		self.btn_usbpause = QPushButton('Pause', self)
		self.btn_usbprew = QPushButton('Prew', self)
		self.btn_usbnext = QPushButton('Next', self)
		self.btn_poweroff = QPushButton('Power OFF', self)
		self.btn_mute = QPushButton('Mute', self)
		self.btn_quit = QPushButton('Quit', self)

		self.btn_inputpc.clicked.connect(self.btn_inputpc_click)
		self.btn_inputusb.clicked.connect(self.btn_inputusb_click)
		self.btn_volumeup.clicked.connect(self.btn_volumeup_click)
		self.btn_volumedown.clicked.connect(self.btn_volumedown_click)
		self.btn_usbstop.clicked.connect(self.btn_usbstop_click)
		self.btn_usbplay.clicked.connect(self.btn_usbplay_click)
		self.btn_usbpause.clicked.connect(self.btn_usbpause_click)
		self.btn_usbprew.clicked.connect(self.btn_usbprew_click)
		self.btn_usbnext.clicked.connect(self.btn_usbnext_click)
		self.btn_poweroff.clicked.connect(self.btn_poweroff_click)
		self.btn_quit.clicked.connect(QApplication.instance().quit)
		self.btn_mute.clicked.connect(self.btn_mute_click)

		self.mainWidget = QWidget(self)
		self.mainLayout = QGridLayout(self.mainWidget)
		self.mainLayout.addWidget(self.btn_inputpc, 0, 0, 1, 2)
		self.mainLayout.addWidget(self.btn_volumeup, 0, 3, 1, 2)
		self.mainLayout.addWidget(self.btn_inputusb, 1, 0, 1, 2)
		self.mainLayout.addWidget(self.btn_volumedown, 1, 3, 1, 2)
		self.mainLayout.addWidget(self.btn_usbstop, 2, 0)
		self.mainLayout.addWidget(self.btn_usbplay, 2, 1)
		self.mainLayout.addWidget(self.btn_usbpause, 2, 2)
		self.mainLayout.addWidget(self.btn_usbprew, 2, 3)
		self.mainLayout.addWidget(self.btn_usbnext, 2, 4)
		self.mainLayout.addWidget(self.btn_poweroff, 4, 0, 1, 2)
		self.mainLayout.addWidget(self.btn_mute, 3, 3, 1, 2)
		self.mainLayout.addWidget(self.btn_quit, 4, 3, 1, 2)

		self.mainWidget.setLayout(self.mainLayout)

		self.setCentralWidget(self.mainWidget)
		self.setWindowIcon(QIcon('/usr/share/icons/onkyo.png'))
		self.setFixedSize(280, 200)
		self.setWindowTitle('Onkyo Control')

		if self.hide_window:
			self.hide()
		else:
			self.show()

		self.createActions()
		self.createTrayIcon()
		self.createShortcuts()
		self.trayIcon.show()
		self.statusBar()
		self.createMenu()

	def createShortcuts(self):
		self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
		self.shortcut.activated.connect(QApplication.instance().quit)
		self.shortcut = QShortcut(QKeySequence("Ctrl+M"), self)
		self.shortcut.activated.connect(self.btn_mute_click)

	def createActions(self):
		self.minimizeAction = QAction("Mi&nimize", self, triggered=self.hide)
		self.maximizeAction = QAction("Ma&ximize", self, triggered=self.showMaximized)
		self.restoreAction = QAction(QIcon('/usr/share/icons/onkyo_restore.png'), "&Restore", self, triggered=self.showNormal)
		self.quitAction = QAction(QIcon('/usr/share/icons/onkyo_exit.png'), "&Quit", self, triggered=QApplication.instance().quit)
		self.PoweroffAction = QAction(QIcon('/usr/share/icons/onkyo_poweroff.png'), "&Power OFF", self, triggered=self.btn_poweroff_click)
		self.MuteAction = QAction(QIcon('/usr/share/icons/onkyo_mute.png'), "&Mute", self, triggered=self.btn_mute_click)
		self.VolumeupAction = QAction(QIcon('/usr/share/icons/onkyo_volumeup.png'), "&Volume UP", self, triggered=self.btn_volumeup_click)
		self.VolumedownAction = QAction(QIcon('/usr/share/icons/onkyo_volumedown.png'), "&Volume Down", self, triggered=self.btn_volumedown_click)
		self.aboutAction = QAction(QIcon('/usr/share/icons/onkyo_about.png'),"&About", self, triggered=self.about)
		self.settingsAction = QAction(QIcon('/usr/share/icons/onkyo_settings.png'), "&Settings", self, triggered=self.config)

	def createTrayIcon(self):
		self.trayIconMenu = QMenu(self)
		self.trayIconMenu.addAction(self.restoreAction)
		self.trayIconMenu.addSeparator()
		self.trayIconMenu.addAction(self.VolumeupAction)
		self.trayIconMenu.addAction(self.VolumedownAction)
		self.trayIconMenu.addAction(self.MuteAction)
		self.trayIconMenu.addSeparator()
		self.trayIconMenu.addAction(self.PoweroffAction)
		self.trayIconMenu.addSeparator()
		self.trayIconMenu.addAction(self.aboutAction)
		self.trayIconMenu.addAction(self.quitAction)
		self.trayIcon = QSystemTrayIcon(QIcon("/usr/share/icons/onkyo.png"), self)
		self.trayIcon.setContextMenu(self.trayIconMenu)

	def createMenu(self):
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(self.settingsAction)
		fileMenu.addAction(self.quitAction)
		helpMenu = menubar.addMenu('&Help')
		helpMenu.addAction(self.aboutAction)

	def sendTextToStatusBar(self, text):
		self.statusBar().showMessage(str(text))

	def createTrayError(self, e):
		return self.trayIcon.showMessage('Error', 'Send command to receiver failed:\n' + str(e), QSystemTrayIcon.Critical, 5 * 1000)

	def about(self):
		title = self.tr("""<b>Onkyo QT</b>
			<br/>License: GPLv3
			<br/>Python {0} - on {1}""").format(platform.python_version(), platform.system())
		image = ':/logo'
		text = self.tr("""<p>Author: Andry Kondratiev <a href="mailto:andry.kondratiev@gmail.com">andry.kondratiev@gmail.com</a>
						<p>Website: <a href="https://github.com/massdest/onkyoqtpy">
						https://github.com/massdest/onkyoqtpy</a>
						""")
		contributors = QCoreApplication.translate("About dialog", """
			Author: Andry Kondratiev<br/>
			""", "List of contributors")

		dialog = about_dlg.AboutDialog(title, text, image, contributors, self)
		dialog.exec_()

	def config(self):
		dialog = settings.OnkyoSettings(self)
		dialog.applied_signal.connect(self.config_save)
		if dialog.exec_() == 1:
			self.config_save()

	def config_save(self):
		logging.debug('Config saving...')
		self.host = self.settings.value('host')

def main():
	app = QApplication(sys.argv)
	QApplication.setQuitOnLastWindowClosed(False)
	ex = Onkyo()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()



