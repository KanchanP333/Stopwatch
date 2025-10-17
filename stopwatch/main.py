#Python PyQt5 Stopwatch
#Testing the stopwatch

import sys #Used to handle comand line arguments
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, 
                            QVBoxLayout, QVBoxLayout, QHBoxLayout)
#Imports necessary widgets and layout managers

from PyQt5.QtCore import QTimer, QTime, Qt
#QTimer allows schedulin functions at intervals (to update the stopwatch)
#QTime stores and manipulates time values
#Qt provides constans for alignments

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__() #Calls the constructor of the base
        self.time=QTime(0,0,0,0) #StopWatch time
        self.time_label=QLabel("00:00:00:00",self) #Used as placeholder
        self.start_button = QPushButton("START",self) #Each button is a child widget of the main stopwatch
        self.stop_button = QPushButton("STOP",self)
        self.reset_button = QPushButton("RESET", self)
        self.timer=QTimer(self) #Creates an object that will emit a signal at intervals to update the stopwatch display

        self.initUI() #Contains the interface setup logic
    
    def initUI(self): #Where we design the UI
        self.setWindowTitle("Stopwatch")
        self.setGeometry(700,400,500,300)
        
        vbox = QVBoxLayout() #Vertical box layout manager
        vbox.addWidget(self.time_label) 

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox=QHBoxLayout() #Creates a horizontal box layout manager
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox) #Places the buttons below the time display

        self.setStyleSheet("""
            QLabel {
            font-size: 80px;
            font-family: 'Courier New';
            color: #ffffff;
            background-color: #1e1e2f; /*Dark Blue*/
            border: 2px solid #4fc3f7;
            border-radius: 25px;
            padding: 25px;
            qproperty-alignment: 'AlignCenter';
        }

            QPushButton {
            font-size: 28px;
            padding: 15px 30px;
            border-radius: 20px;
            font-family: 'Segoe UI';
            color: white;
            background-color: #2196f3; /*Light blue*/
            border: none;
        }
            QPushButton:hover {
            background-color: #12121c; /*Darker Blue*/
        }

            QPushButton:pressed {
                background-color: #0288d1; /*Light blue*/
            }
        """)

        #Connects buttons to click signals to respective methods
        self.start_button.clicked.connect(self.start) 
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        #Connects the timeout signal to the update display, which updates the displayed time
        self.timer.timeout.connect(self.update_display)


    def start(self):
        self.timer.start(10) #10 milliseconds
        #Calling the start method of the QTimer object

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop() #Calls the stop method of the QTimer object
        self.time=QTime(0,0,0,0) #Resets time back to 0
        self.time_label.setText(self.format_time(self.time)) #Updates the label with the new time

    def format_time(self, time):
        #Receives a QTime object and returns a string format
        hours=time.hour()
        minutes=time.minute()
        seconds=time.second()
        milliseconds=time.msec()//10 #To show only two digits
        return (f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}")

    def update_display(self):
        self.time=self.time.addMSecs(10) #Adds 10ms by the timer and adds 10ms to the curernt self.time
        self.time_label.setText(self.format_time(self.time)) #Updates the label text with the new formatted text string




if __name__=="__main__":
    app=QApplication(sys.argv) #Manages application level resources
    stopwatch=Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_()) #Starts the main event loop and handles events
