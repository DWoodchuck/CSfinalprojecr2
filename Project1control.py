from PyQt5.QtWidgets import *
from Project1 import *
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow,Ui_StudentTestGUI):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.Calculatorbutton.clicked.connect(lambda: self.calculate())
        self.Clearbutton.clicked.connect(lambda: self.clear())


    def calculate(self) -> None:
        """
    Calculate the grades of students based on their scores.

    This function takes the number of students and their scores as input,
    and calculates the grade for each student based on their score and the max score in list grades.

    Returns:None
    """
        try:
            student = int(self.studentnuminput.text())
            number = (self.testscoresinput.text().split())
            grades = []
            for x in range(len(number)):
                number2 = float(number[x])
                grades.append(number2)
            if student < len(grades):
                grades = grades[:student]
            results = ""
            if student == len(grades):
                for i in range(student):
                    if grades[i] >= max(grades)-10:
                        letter_grade = "A"
                    elif grades[i] >= max(grades)-20:
                        letter_grade = "B"
                    elif grades[i] >= max(grades)-30:
                        letter_grade = "C"
                    elif grades[i] >= max(grades)-40:
                        letter_grade = "D"
                    else:
                        letter_grade = "F"
                    results += f'Student {i+1}\'s score is {grades[i]} and their grade is a {letter_grade}\n'
                    self.studentscoresprintlabel.setText(results)
            else:
                self.studentscoresprintlabel.setText('Number of students and number of grades do not match')
        except ValueError:
            self.studentscoresprintlabel.setText('Invalid values inputted')

    def clear(self) -> None:
        """
        clears the line edits and output text box inside the GUI
        :return:None
        """
        self.studentnuminput.setText("")
        self.testscoresinput.setText("")
        self.studentscoresprintlabel.setText("")




