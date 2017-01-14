import logging
import os

from PyQt5.QtCore import (QCoreApplication, QLocale, QSettings, QSize, Qt,pyqtSignal)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QCheckBox, QColorDialog, QComboBox, QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QVBoxLayout)

class OnkyoSettings(QDialog):
	applied_signal = pyqtSignal()

	def __init__(self, parent=None):
		super(OnkyoSettings, self).__init__(parent)
		self.layout = QVBoxLayout()

		# Host IP
		self.settings = QSettings('onkyoqt', 'settings')
		host = self.settings.value('host') or ''
		self.host_label = QLabel(QCoreApplication.translate('Get it from receiver settings','Receiver IP (Restart needed after change)', 'Settings dialogue'))
		self.host_text = QLineEdit()
		self.host_text.setText(host)
		self.host_text.textChanged.connect(self.host_changed)
		self.nohost_message = QCoreApplication.translate('Warning message after pressing Ok', 'Please enter your receiver IP address', 'Settings dialogue')

		# Hide main window on start to tray or not
		self.hide_label = QLabel(self.tr('Run in tray'))
		self.hide_checkbox = QCheckBox()
		self.hide_bool = self.settings.value('hide') or 'False'
		self.hide_bool = eval(self.hide_bool)
		self.hide_checkbox.setChecked(self.hide_bool)
		self.hide_checkbox.stateChanged.connect(self.hide)
		self.hide_changed = False

		# OK Cancel Apply Buttons
		self.buttonLayout = QHBoxLayout()
		self.buttonLayout.addStretch()
		self.buttonBox = QDialogButtonBox()
		self.buttonBox.setOrientation(Qt.Horizontal)
		self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Apply | QDialogButtonBox.Cancel)
		self.buttonBox.setContentsMargins(0, 30, 0, 0)
		self.buttonLayout.addWidget(self.buttonBox)
		self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.apply_settings)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)
		self.buttonBox.button(QDialogButtonBox.Apply).setEnabled(False)
		self.statusbar = QLabel()
		self.layout.addWidget(self.statusbar)

		self.panel = QGridLayout()
		self.panel.addWidget(self.hide_label, 0, 0)
		self.panel.addWidget(self.hide_checkbox, 0, 1)
		self.panel.addWidget(self.host_label, 1, 0)
		self.panel.addWidget(self.host_text, 1, 1)
		self.layout.addLayout(self.panel)
		self.layout.addLayout(self.buttonLayout)
		self.setLayout(self.layout)
		self.setWindowTitle(self.tr('Onkyo QT Configuration'))

	def apply_settings(self):
		self.accepted()

	def host_changed(self):
		self.buttonBox.button(QDialogButtonBox.Apply).setEnabled(True)

	def accepted(self):
		host = self.host_text.text()
		if host == '':
			self.statusbar.setText(self.nohost_message)
			return
		else:
			self.settings.setValue('host', str(self.host_text.text()))
		self.applied_signal.emit()

		if self.hide_changed:
			self.hide_apply()

	def hide(self, state):
		self.hide_state = state
		self.hide_changed = True
		self.buttonBox.button(QDialogButtonBox.Apply).setEnabled(True)

	def hide_apply(self):
		if self.hide_state == 2:
			self.settings.setValue('hide', 'True')
		elif self.hide_state == 0:
			self.settings.setValue('hide', 'False')
		else:
			return

