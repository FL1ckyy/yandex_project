import sqlite3
from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import *
from main_weath import MainWindow

db = sqlite3.connect('databaselogin.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS user(
        login TEXT,
        password TEXT
        )""")
db.commit()


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(425, 350)

        Login.setStyleSheet("QWidget {\n"
                            "    background-color:#556B2F;\n"
                            "}")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(150, 200, 201, 35))
        self.LoginButton.setStyleSheet("QPushButton {\n"
                                       "    background-color: /*#B8CCD5*/#FCFAF7;\n"
                                       "    border-radius: 3px;\n"
                                       "    color: #727173;\n"
                                       "    font: 18pt \"Gotham Pro\";\n"
                                       "    padding-left: 6px;\n"
                                       "    padding-right: 6px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    border: 1px solid #727173;\n"
                                       "}")
        self.LoginButton.setObjectName("LoginButton")
        self.LoginEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LoginEdit.setGeometry(QtCore.QRect(150, 135, 201, 20))
        self.LoginEdit.setStyleSheet("QLineEdit {\n"
                                     "    background-color: /*#FF0000*/#FF0000;\n"
                                     "    /*border: 1px solid rgb(0, 85, 255);*/\n"
                                     "    border-radius: 3px;\n"
                                     "    color: #FFFFFF;\n"
                                     "    font: 12pt \"Gotham Pro\";\n"
                                     "    padding-left: 10px;\n"
                                     "    padding-right: 10px;\n"
                                     "}\n"
                                     "\n"
                                     "QLineEdit:focus {\n"
                                     "    border: 1px solid #727173;\n"
                                     "}")
        self.LoginEdit.setObjectName("LoginEdit")
        self.PasswordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordEdit.setGeometry(QtCore.QRect(150, 165, 201, 20))
        self.PasswordEdit.setStyleSheet("QLineEdit {\n"
                                        "    background-color: /*#FF0000*/#FF0000;\n"
                                        "    /*border: 1px solid rgb(0, 85, 255);*/\n"
                                        "    border-radius: 3px;\n"
                                        "    color: #FFFFFF;\n"
                                        "    font: 12pt \"Gotham Pro\";\n"
                                        "    padding-left: 10px;\n"
                                        "    padding-right: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QLineEdit:focus {\n"
                                        "    border: 1px solid #727173;\n"
                                        "}")
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.RegisterButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterButton.setGeometry(QtCore.QRect(150, 242, 201, 35))
        self.RegisterButton.setStyleSheet("QPushButton {\n"
                                          "    background-color: /*#B8CCD5*/#FCFAF7;\n"
                                          "    border-radius: 3px;\n"
                                          "    color: #727173;\n"
                                          "    font: 18pt \"Gotham Pro\";\n"
                                          "    padding-left: 6px;\n"
                                          "    padding-right: 6px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    border: 1px solid #727173;\n"
                                          "}")
        self.RegisterButton.setObjectName("RegisterButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 135, 100, 20))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
                                    "    background-color: /*#FF0000*/#FF0000;\n"
                                    "    /*border: 1px solid rgb(0, 85, 255);*/\n"
                                    "    border-radius: 3px;\n"
                                    "    color: #FFFAFA;\n"
                                    "    font: 12pt \"Gotham Pro\";\n"
                                    "    padding-left: 10px;\n"
                                    "    padding-right: 10px;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:focus {\n"
                                    "    border: 1px solid #727173;\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 165, 100, 20))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                      "    background-color: /*#FF0000F*/#FF0000;\n"
                                      "    /*border: 1px solid rgb(0, 85, 255);*/\n"
                                      "    border-radius: 3px;\n"
                                      "    color: #FFFAFA;\n"
                                      "    font: 12pt \"Gotham Pro\";\n"
                                      "    padding-left: 10px;\n"
                                      "    padding-right: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:focus {\n"
                                      "    border: 1px solid #727173;\n"
                                      "}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.LoginEdit.raise_()
        self.PasswordEdit.raise_()
        self.LoginButton.raise_()
        self.RegisterButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.LoginButton.setText(_translate("Login", "Login"))
        self.RegisterButton.setText(_translate("Login", "Register"))
        self.lineEdit.setText(_translate("Login", "Login"))
        self.lineEdit_2.setText(_translate("Login", "Password"))


class Window2(MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.buttonGet.clicked.connect(self.pressed_get)
        self.button_close.clicked.connect(self.close)
        self.Favourites.clicked.connect(self.beta_Favour)
        self.five_day.clicked.connect(self.beta_five_day)


class Ui_MainWindow(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.LoginButton.clicked.connect(
            lambda: self.message(self.LoginEdit.text(), self.PasswordEdit.text()))
        self.RegisterButton.clicked.connect(
            lambda: self.message2(self.LoginEdit.text(), self.PasswordEdit.text()))

    def message(self, LoginEdit, passwordEdit):
        user_login = LoginEdit
        user_password = passwordEdit
        if not user_login or not user_password:
            msg = QMessageBox.information(
                self,
                'error',
                'Что-то пошло не так. Проверьте логин и пароль'
            )
            return

        error = QMessageBox()
        sql.execute(
            "SELECT login FROM user WHERE login=? AND password=?",
            (user_login, user_password))
        count = sql.fetchone()
        db.commit()

        if not count:
            error = QMessageBox()
            error.setWindowTitle('error')
            error.setText('Что-то пошло не так. \n'
                          'Проверьте свое имя пользователя и пароль или   \n'
                          'Попробуйте зарегистрироваться')
            error.exec_()
        else:

            self.window2 = Window2()
            self.window2.show()
            self.hide()

    def message2(self, loginEdit, passwordEdit):
        user_login = loginEdit
        user_password = passwordEdit
        if not user_login or not user_password:
            msg = QMessageBox.information(
                self,
                'error',
                'Что-то пошло не так. Проверьте свое имя пользователя и пароль'
            )
            return

        sql.execute("SELECT login FROM user WHERE login = ?", (user_login,))

        if sql.fetchone() is None:
            sql.execute(
                "INSERT INTO user (login, password) VALUES (?,?)",
                (user_login, user_password,)
            )

            msg = QMessageBox.information(
                self,
                'Успешно',
                'Вы зарегистрировались!'
            )
        else:
            print('Логин уже зарегистрирован')
            msg = QMessageBox.information(
                self,
                'error',
                'Что-то пошло не так.\n'
                'Этот логин уже существует.'
                'Попробуйте войти в систему.'
            )
            return

        db.commit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Ui_MainWindow()
    w.show()
    sys.exit(app.exec_())
