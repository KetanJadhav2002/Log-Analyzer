from PyQt5.QtWidgets import (
	QWidget, QApplication, QComboBox, QPushButton, QTextEdit, QLabel,
	QLineEdit
)
from PyQt5.QtGui import QIcon
import sys
import subprocess


class LogAnalyzer(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(50, 50, 500, 745)
		self.setFixedSize(500, 745)
		self.setWindowTitle("Windows Log Analysis")
		self.setStyleSheet("background-color:black")
		self.setWindowIcon(QIcon("Images/logo.png"))
		
	def log_area(self):
		self.log_area = QTextEdit(self)
		self.log_area.setGeometry(5, 5, 490, 500)
		self.log_area.setStyleSheet("border:1px solid red;color:red;")
		self.log_area.setReadOnly(True)
		self.log_area.show()
		
	def combo_box_label(self):
		self.label = QLabel(self)
		self.label.setText("Windows Log Type")
		self.label.setStyleSheet("color:red;")
		self.label.setGeometry(5, 505, 300, 30)
		self.label.show()
	
	def combo_box(self):
		types = ["Application", "Security", "Setup", "System"]
		self.combo_box = QComboBox(self)
		self.combo_box.setGeometry(5, 535, 350, 30)
		self.combo_box.setStyleSheet("border:1px solid red;color:red;")
		self.combo_box.setCurrentIndex(0)
		self.combo_box.setEditable(True)
		self.combo_box.addItems(types)
		self.combo_box.show()
	
	def get_log_button(self):
		self.get_log_btn = QPushButton(self)
		self.get_log_btn.setText("Get Log")
		self.get_log_btn.setGeometry(360, 535, 135, 30)
		self.get_log_btn.setStyleSheet("border:1px solid red;color:red;")
		self.get_log_btn.clicked.connect(self.get_logs)
		self.get_log_btn.show()
	
	def get_logs(self):
		log_type = self.combo_box.currentText().strip()

        # CMD command to query Windows Event Log
		cmd = f'wevtutil qe {log_type} /c:20 /f:text'
		
		try:
			result = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)
			self.log_area.setText(result)
		except subprocess.CalledProcessError as e:
			self.log_area.setText(e.output)
	
	def filter_label(self):
		self.filter_label = QLabel(self)
		self.filter_label.setText("Filtering")
		self.filter_label.setStyleSheet("color:red;")
		self.filter_label.setGeometry(5, 565, 200, 30)
		self.filter_label.show()
	
	def filters(self):
		self.filter_eventID = QLineEdit(self)
		self.filter_eventID.setPlaceholderText("EventID")
		self.filter_eventID.setGeometry(5, 570, 150, 30)
		self.filter_eventID.setStyleSheet("border:1px solid red;color:red;")
		self.filter_eventID.show()
		
		levels = ["Lavel", "1", "2", "3", "4", "5"]
		self.filter_level = QComboBox(self)
		self.filter_level.setGeometry(160, 570, 150, 30)
		self.filter_level.addItems(levels)
		self.filter_level.setStyleSheet("border:1px solid red;color:red;")
		self.filter_level.show()
		
		self.filter_timeCreated = QLineEdit(self)
		self.filter_timeCreated.setPlaceholderText("Time Created")
		self.filter_timeCreated.setGeometry(315, 570, 180, 30)
		self.filter_timeCreated.setStyleSheet("border:1px solid red;color:red;")
		self.filter_timeCreated.show()
		
		self.filter_providerName = QLineEdit(self)
		self.filter_providerName.setPlaceholderText("Provider Name")
		self.filter_providerName.setGeometry(5, 605, 150, 30)
		self.filter_providerName.setStyleSheet("border:1px solid red;color:red;")
		self.filter_providerName.show()
		
		self.filter_logName = QLineEdit(self)
		self.filter_logName.setPlaceholderText("Log Name")
		self.filter_logName.setGeometry(160, 605, 150, 30)
		self.filter_logName.setStyleSheet("border:1px solid red;color:red;")
		self.filter_logName.show()
		
		self.filter_task = QLineEdit(self)
		self.filter_task.setPlaceholderText("Task")
		self.filter_task.setGeometry(315, 605, 180, 30)
		self.filter_task.setStyleSheet("border:1px solid red;color:red;")
		self.filter_task.show()
		
		self.filter_opcode = QLineEdit(self)
		self.filter_opcode.setPlaceholderText("OPcode")
		self.filter_opcode.setGeometry(5, 640, 150, 30)
		self.filter_opcode.setStyleSheet("border:1px solid red;color:red;")
		self.filter_opcode.show()
		
		self.filter_keyword = QLineEdit(self)
		self.filter_keyword.setPlaceholderText("Keyword")
		self.filter_keyword.setGeometry(160, 640, 150, 30)
		self.filter_keyword.setStyleSheet("border:1px solid red;color:red;")
		self.filter_keyword.show()
		
		self.filter_recordID = QLineEdit(self)
		self.filter_recordID.setPlaceholderText("RecordID")
		self.filter_recordID.setGeometry(315, 640, 180, 30)
		self.filter_recordID.setStyleSheet("border:1px solid red;color:red;")
		self.filter_recordID.show()
		
		self.filter_computer = QLineEdit(self)
		self.filter_computer.setPlaceholderText("Computer")
		self.filter_computer.setGeometry(5, 675, 150, 30)
		self.filter_computer.setStyleSheet("border:1px solid red;color:red;")
		self.filter_computer.show()
		
		self.filter_processID = QLineEdit(self)
		self.filter_processID.setPlaceholderText("ProcessID")
		self.filter_processID.setGeometry(160, 675, 100, 30)
		self.filter_processID.setStyleSheet("border:1px solid red;color:red;")
		self.filter_processID.show()
		
		self.filter_threadID = QLineEdit(self)
		self.filter_threadID.setPlaceholderText("ThreadID")
		self.filter_threadID.setGeometry(265, 675, 100, 30)
		self.filter_threadID.setStyleSheet("border:1px solid red;color:red;")
		self.filter_threadID.show()
		
		self.filter_version = QLineEdit(self)
		self.filter_version.setPlaceholderText("Version")
		self.filter_version.setGeometry(370, 675, 125, 30)
		self.filter_version.setStyleSheet("border:1px solid red;color:red;")
		self.filter_version.show()
		
		self.filter_button = QPushButton(self)
		self.filter_button.setText("Filter")
		self.filter_button.setGeometry(5, 710, 490, 30)
		self.filter_button.setStyleSheet("border:1px solid red;color:red;")
		self.filter_button.clicked.connect(self.filter_log)
		self.filter_button.show()
		
		
	def filter_log(self):
		try:
			log_type = self.combo_box.currentText().strip()

			# ===== Collect filter values =====
			eventID = self.filter_eventID.text().strip()
			level = self.filter_level.currentText().strip()
			timeCreated = self.filter_timeCreated.text().strip()
			provider = self.filter_providerName.text().strip()
			logname = self.filter_logName.text().strip()
			task = self.filter_task.text().strip()
			opcode = self.filter_opcode.text().strip()
			keyword = self.filter_keyword.text().strip()
			recordID = self.filter_recordID.text().strip()
			computer = self.filter_computer.text().strip()
			processID = self.filter_processID.text().strip()
			threadID = self.filter_threadID.text().strip()
			version = self.filter_version.text().strip()

			# ===== Build XML filter for wevtutil =====
			system_conditions = []

			if eventID:
				system_conditions.append(f"EventID={eventID}")

			if level and level.lower() != "lavel":
				system_conditions.append(f"Level={level}")

			if provider:
				system_conditions.append(f"Provider[@Name='{provider}']")

			if recordID:
				system_conditions.append(f"EventRecordID={recordID}")

			if version:
				system_conditions.append(f"Version={version}")

			if computer:
				system_conditions.append(f"Computer='{computer}'")

			if timeCreated:
				system_conditions.append(f"TimeCreated[@SystemTime>='{timeCreated}']")

			if processID:
				system_conditions.append(f"Execution[@ProcessID='{processID}']")

			if threadID:
				system_conditions.append(f"Execution[@ThreadID='{threadID}']")

			# NOTE:
			# Task, Opcode, Keywords are not always available in XML simple filter
			# but we include if user provides
			if task:
				system_conditions.append(f"Task={task}")

			if opcode:
				system_conditions.append(f"Opcode={opcode}")

			if keyword:
				system_conditions.append(f"Keywords={keyword}")

			# ===== Join conditions =====
			if system_conditions:
				system_query = " and ".join(system_conditions)
				query = f"*[System[{system_query}]]"
			else:
				query = "*"

			# ===== CMD command =====
			cmd = f'wevtutil qe {log_type} /q:"{query}" /f:text /c:50'

			# ===== Execute =====
			result = subprocess.check_output(
				cmd,
				shell=True,
				text=True,
				stderr=subprocess.STDOUT
			)

			self.log_area.setText(result if result else "No matching logs found.")

		except subprocess.CalledProcessError as e:
			self.log_area.setText("CMD ERROR:\n" + e.output)

		except Exception as e:
			self.log_area.setText("UNEXPECTED ERROR:\n" + str(e))

		
		
		
		
		
		
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	gui = LogAnalyzer()
	gui.log_area()
	gui.combo_box_label()
	gui.combo_box()
	gui.get_log_button()
	gui.filter_label()
	gui.filters()
	gui.show()
	sys.exit(app.exec_())

