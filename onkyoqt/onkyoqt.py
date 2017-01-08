#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import eiscp
import signal
import platform
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QSettings, Qt, QCoreApplication
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox, QComboBox,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QMessageBox, QMenu, QPushButton, QSpinBox, QStyle, QSystemTrayIcon,
        QTextEdit, QVBoxLayout, QWidget, QShortcut, QMainWindow)

try:
	import about_dlg
except:
	from onkyoqt import about_dlg

signal.signal(signal.SIGINT, signal.SIG_DFL)

host = "192.168.1.9"
#settings = QSettings("~/.onkyoqt.ini", QSettings.IniFormat)
#host = settings.value('host', type=str)
receiver = eiscp.eISCP(host)

class Onkyo(QMainWindow):

	def __init__(self):
		super(Onkyo, self).__init__()
		self.initUI()
			
	def btn_inputpc_click(self):
		try:
			receiver.command('input-selector=pc')
		except Exception as e:
			self.createTrayError(e)

	def btn_inputusb_click(self):
		try:
			receiver.command('input-selector=usb')
		except Exception as e:
			self.createTrayError(e)

	def btn_volumeup_click(self):
		try:
			volume_now = receiver.command('volume=level-up')
			self.sendTextToStatusBar(volume_now)
		except Exception as e:
			self.createTrayError(e)

	def btn_volumedown_click(self):
		try:
			volume_now = receiver.command('volume=level-down')
			self.sendTextToStatusBar(volume_now)
		except Exception as e:
			self.createTrayError(e)

	def btn_usbstop_click(self):
		try:
			receiver.command('network-usb=stop')
		except Exception as e:
			self.createTrayError(e)

	def btn_usbplay_click(self):
		try:
			receiver.command('network-usb=play')
		except Exception as e:
			self.createTrayError(e)

	def btn_usbpause_click(self):
		try:
			receiver.command('network-usb=pause')
		except Exception as e:
			self.createTrayError(e)

	def btn_usbprew_click(self):
		try:
			receiver.command('network-usb=trdn')
		except Exception as e:
			self.createTrayError(e)

	def btn_usbnext_click(self):
		try:
			receiver.command('network-usb=trup')
		except Exception as e:
			self.createTrayError(e)

	def btn_poweroff_click(self):
		try:
			receiver.command('system-power=standby')
		except Exception as e:
			self.createTrayError(e)

	def btn_mute_click(self):
		try:
			volume_now = receiver.command('volume=0')
			self.sendTextToStatusBar(volume_now)
		except Exception as e:
			self.createTrayError(e)
	
	def initUI(self):
	
		btn_inputpc = QPushButton('PC', self)
		btn_inputpc.move(10, 10)
		btn_inputpc.setMaximumWidth(85)
	
		btn_inputusb = QPushButton('USB', self)
		btn_inputusb.move(10, 40)
		btn_inputusb.setMaximumWidth(85)

		btn_volumeup = QPushButton('Vol +', self)
		btn_volumeup.move(125, 10)
		btn_volumeup.setMaximumWidth(85)
	
		btn_volumedown = QPushButton('Vol -', self)
		btn_volumedown.move(125, 40)
		btn_volumedown.setMaximumWidth(85)

		btn_usbstop = QPushButton('Stop', self)
		btn_usbstop.move(10, 70)
		btn_usbstop.setMaximumWidth(40) 

		btn_usbplay = QPushButton('Play', self)
		btn_usbplay.move(50, 70)
		btn_usbplay.setMaximumWidth(40) 
	
		btn_usbpause = QPushButton('Pause', self)
		btn_usbpause.move(90, 70)
		btn_usbpause.setMaximumWidth(40) 

		btn_usbprew = QPushButton('Prew', self)
		btn_usbprew.move(130, 70)
		btn_usbprew.setMaximumWidth(40)

		btn_usbnext = QPushButton('Next', self)
		btn_usbnext.move(170, 70)
		btn_usbnext.setMaximumWidth(40)

		btn_poweroff = QPushButton('Power OFF', self)
		btn_poweroff.move(10, 100)
		btn_poweroff.setMaximumWidth(80)

		btn_mute = QPushButton('Mute', self)
		btn_mute.move(90, 100)
		btn_mute.setMaximumWidth(40)

		btn_quit = QPushButton('Quit', self)
		btn_quit.move(130, 100)
		btn_quit.setMaximumWidth(80)

		btn_inputpc.clicked.connect(self.btn_inputpc_click)
		btn_inputusb.clicked.connect(self.btn_inputusb_click)
		btn_volumeup.clicked.connect(self.btn_volumeup_click)
		btn_volumedown.clicked.connect(self.btn_volumedown_click)
		btn_usbstop.clicked.connect(self.btn_usbstop_click)
		btn_usbplay.clicked.connect(self.btn_usbplay_click)
		btn_usbpause.clicked.connect(self.btn_usbpause_click)
		btn_usbprew.clicked.connect(self.btn_usbprew_click)
		btn_usbnext.clicked.connect(self.btn_usbnext_click)
		btn_poweroff.clicked.connect(self.btn_poweroff_click)
		btn_quit.clicked.connect(QApplication.instance().quit)
		btn_mute.clicked.connect(self.btn_mute_click)

		self.setWindowIcon(QIcon('/usr/share/icons/onkyo.png'))
		self.setFixedSize(220, 160)
		self.setWindowTitle('Onkyo Control') 
		self.show()

		self.createActions()
		self.createTrayIcon()
		self.createShortcuts()
		self.trayIcon.show()
		self.statusBar()

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

def main():
	app = QApplication(sys.argv)
	QApplication.setQuitOnLastWindowClosed(False)
	ex = Onkyo()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()



