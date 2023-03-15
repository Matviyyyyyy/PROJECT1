
import json #підключаю модуль json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import game2

app = QApplication([])
win_card = QWidget()
win_card.setWindowTitle('Загальне вікно гри') 
win_card.resize(400, 200)

app.setStyleSheet("""
        QWidget {
            background: #fffcad;
            border-radius: 11px;    

        }
        
        QPushButton{
            background: #b7ffad;
            color: #071bf5;
            border-radius: 11px;
            min-width: 6em;    
            min-height: 2em;
            font-family: Arial;
            font: bold 12px;      
        }
        
        QLineEdit{
            background: #f7cdd1;
            max-width: 20em;
        }

"""
)


oneline_edit = QLineEdit()
oneline_edit.setPlaceholderText("Логін:")
twoline_edit = QLineEdit()
twoline_edit.setPlaceholderText("Пароль:")
one_button = QPushButton("Логін")
two_button = QPushButton("Реєстрація")
three_button = QPushButton("Відміна")

hor_line = QHBoxLayout() 
ver_line = QVBoxLayout()

ver_line.addWidget(oneline_edit)
ver_line.addWidget(twoline_edit)
ver_line.addLayout(hor_line)
hor_line.addWidget(one_button)
hor_line.addWidget(two_button)
hor_line.addWidget(three_button)
 
def registration():
        dialog = QDialog()

        dialog.setStyleSheet("""
        QWidget {
            background: #ecf542;
        }
        
        QPushButton{    
            background: #cdf7dc;
            color: #0008f5;
            border-radius: 11px;
            min-width: 6em;    
            min-height: 2em;
            font-family: Arial;
            font: bold 12px;      
        }
        
        QLineEdit{
            background: #02fa0f;
            max-width: 20em;

        }
"""
)


        onepole = QLineEdit()
        onepole.setPlaceholderText("Username")
        
        twopole = QLineEdit()
        twopole.setPlaceholderText("Pasword")

        buto =  QPushButton('Зареєструвати')
        butt = QPushButton("Відміна")

        vertic = QVBoxLayout()
        horiz = QHBoxLayout()

        vertic.addWidget(onepole)
        vertic.addWidget(twopole)
        vertic.addLayout(horiz)
        horiz.addWidget(buto)
        horiz.addWidget(butt)
        def twofunction():
            with open("lonn.json", "r", encoding="utf-8") as file:
                json_data = json.load(file)
            username = onepole.text()
            password = twopole.text()
            json_data[username] = {
                "password": password
            }
            with open("lonn.json", "w", encoding="utf-8") as file:
                json.dump(json_data, file, ensure_ascii=False, indent=4)
            dialog.close()
        def abolition_pop():
            dalog.close()
        butt.clicked.connect(abolition_pop)
        buto.clicked.connect(twofunction)
        dialog.setLayout(vertic)
        dialog.show()
        dialog.exec_()
        
def playgame():
    with open("lonn.json", "r", encoding="utf-8") as file:
        json_data = json.load(file)
    username = oneline_edit.text()
    password = twoline_edit.text()
    if username in json_data and password == json_data[username]['password']:
        game2.play()
def abolition():
    app.quit()
three_button.clicked.connect(abolition)
one_button.clicked.connect(playgame)
two_button.clicked.connect(registration)
win_card.setLayout(ver_line)
win_card.show()
app.exec_()
