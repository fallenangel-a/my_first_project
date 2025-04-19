from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox
from random import shuffle

app = QApplication([])
main_win = QWidget()
main_win.cur_question = -1
main_win.setWindowTitle('карточки')
main_win.resize(300, 200)



label1 = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')
#RadioGroup = QButtonGroup()
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


ans_layout1 = QVBoxLayout()
ans_layout1.setSpacing(20)
ans_layout1.addWidget(rbtn_1, alignment=Qt.AlignCenter)
ans_layout1.addWidget(rbtn_2, alignment=Qt.AlignCenter)

ans_layout2 = QVBoxLayout()
ans_layout2.setSpacing(20)
ans_layout2.addWidget(rbtn_3, alignment=Qt.AlignCenter)
ans_layout2.addWidget(rbtn_4, alignment=Qt.AlignCenter)
ans_layout = QHBoxLayout()
ans_layout.addLayout(ans_layout1)
ans_layout.addLayout(ans_layout2)
RadioGroupBox.setLayout(ans_layout)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    label1.setText(q.question)
    is_correct.setText(q.right_answer)
    show_question()

def show_question():
    answer_group.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    
def show_result():
    answer_group.show()
    RadioGroupBox.hide()
    button.setText('Следующий вопрос')
    label1.setText('Самый сложный вопрос в мире!')
    

def click_OK():
    if button.text() == 'Следующий вопрос':
        next_question()
    else:
        show_result()

def next_question():
    main_win.cur_question = main_win.cur_question + 1
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = 0
    q = questions_list[main_win.cur_question]
    ask(q)
    

button = QPushButton('Ответить')

answer_group = QGroupBox('Результат теста')
right = QLabel('Правильно/Неправильно')
is_correct = QLabel('Смурфы')
answer_line = QVBoxLayout()
answer_line.addWidget(right)
answer_line.addWidget(is_correct, alignment=Qt.AlignCenter)
answer_group.setLayout(answer_line)
answer_group.hide()

line = QVBoxLayout()
line.addWidget(label1, alignment=Qt.AlignCenter)
line.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
line.addWidget(answer_group)
line.addWidget(button, alignment=Qt.AlignCenter)
line.setSpacing(20)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

questions_list = []
questions_list.append(Question('Какой национальности не существует?', 'Смурфы' ,'Энцы', 'Чулымцы', 'Алеуты'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зеленый' ,'Красный', 'Синий', 'Белый'))
questions_list.append(Question('Официальный язык Бразилии?', 'Португальский' ,'Бразильский', 'Французский', 'Русский'))

button.clicked.connect(click_OK)

next_question()
main_win.setLayout(line)
main_win.show()
app.exec_()