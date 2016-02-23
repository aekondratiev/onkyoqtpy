#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import eiscp
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

host = '192.168.1.3'
receiver = eiscp.eISCP(host)

class Onkyo(QtGui.QWidget):
    
	def __init__(self):
		super(Onkyo, self).__init__()
		self.initUI()
			
	@pyqtSlot()
	def btn_inputpc_click(self):
		receiver.command('input-selector=pc')

	@pyqtSlot()
	def btn_inputusb_click(self):
		receiver.command('input-selector=usb')
 
	@pyqtSlot()
	def btn_volumeup_click(self):
		receiver.command('volume=level-up')

	@pyqtSlot()
	def btn_volumedown_click(self):
		receiver.command('volume=level-down')

	@pyqtSlot()
	def btn_usbstop_click(self):
		receiver.command('network-usb=stop')

	@pyqtSlot()
	def btn_usbplay_click(self):
		receiver.command('network-usb=play')

	@pyqtSlot()
	def btn_usbpause_click(self):
		receiver.command('network-usb=pause')

	@pyqtSlot()
	def btn_usbprew_click(self):
		receiver.command('network-usb=trdn')

	@pyqtSlot()
	def btn_usbnext_click(self):
		receiver.command('network-usb=trup')

	@pyqtSlot()
	def btn_poweroff_click(self):
		receiver.command('system-power=standby')
	
	def initUI(self):
	
		btn_inputpc = QPushButton('PC', self)
		btn_inputpc.move(10, 10)
	
		btn_inputusb = QPushButton('USB', self)
		btn_inputusb.move(10, 40)	 
	
		btn_volumeup = QPushButton('Vol +', self)
		btn_volumeup.move(125, 10)
	
		btn_volumedown = QPushButton('Vol -', self)
		btn_volumedown.move(125, 40)	 

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

		trayIcon = SystemTrayIcon(QtGui.QIcon("bomb.xpm"), self)
  
		self.setGeometry(300, 300, 220, 140)
		self.setWindowTitle('Onkyo Control') 
		self.show()
		trayIcon.show()


class SystemTrayIcon(QtGui.QSystemTrayIcon):

	def __init__(self, icon, parent=None):
		QtGui.QSystemTrayIcon.__init__(self, icon, parent)
		menu = QtGui.QMenu(parent)
		exitAction = menu.addAction("Exit")
		self.setContextMenu(menu)
    
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Onkyo()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
