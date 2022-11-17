from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt


class Design(object):
    def setupUi(self, weather_form):
        weather_form.setWindowFlags(Qt.FramelessWindowHint)
        weather_form.setWindowTitle('Погода')
        weather_form.setObjectName("weather_form")
        weather_form.resize(1000, 900)
        weather_form.setTabletTracking(True)
        weather_form.setFocusPolicy(QtCore.Qt.ClickFocus)

        weather_form.setWindowOpacity(1.0)
        weather_form.setLayoutDirection(QtCore.Qt.LeftToRight)
        weather_form.setStyleSheet("QWidget {\n"
                                   "    background-color:#006400;\n"
                                   "}")

        self.input_your_city = QtWidgets.QLineEdit(weather_form)
        self.input_your_city.setGeometry(QtCore.QRect(100, 60, 542, 62))
        font = QtGui.QFont()
        font.setFamily("Gotham Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.input_your_city.setFont(font)
        self.input_your_city.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.input_your_city.setAcceptDrops(False)
        self.input_your_city.setStyleSheet("QLineEdit {\n"
                                           "    background-color: /*#00FFFF*/#00FFFF;\n"
                                           "    /*border: 1px solid rgb(0, 85, 255);*/\n"
                                           "    border-radius: 3px;\n"
                                           "    color: #000000;\n"
                                           "    font: 30pt \"Gotham Pro\";\n"
                                           "    padding-left: 10px;\n"
                                           "    padding-right: 10px;\n"
                                           "}\n"
                                           "\n"
                                           "QLineEdit:focus {\n"
                                           "    border: 1px solid #727173;\n"
                                           "}")
        self.input_your_city.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_your_city.setInputMask("")
        self.input_your_city.setFrame(True)
        self.input_your_city.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_your_city.setDragEnabled(False)
        self.input_your_city.setReadOnly(False)
        self.input_your_city.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.input_your_city.setClearButtonEnabled(False)
        self.input_your_city.setObjectName("inputCity")
        self.Favourites = QtWidgets.QPushButton(weather_form)
        self.Favourites.setGeometry(QtCore.QRect(750, 200, 201, 35))
        self.Favourites.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Favourites.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Favourites.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Favourites.setCheckable(False)
        self.Favourites.setAutoRepeat(False)
        self.Favourites.setAutoExclusive(False)
        self.Favourites.setAutoRepeatDelay(304)
        self.Favourites.setObjectName("Favourites")
        self.Favourites.setStyleSheet("QPushButton {\n"
                                      "    background-color: /*#000000*/#FF4500;\n"
                                      "    border-radius: 3px;\n"
                                      "    color: #DDA0DD;\n"
                                      "    font: 12pt \"Gotham Pro\";\n"
                                      "    padding-left: 6px;\n"
                                      "    padding-right: 6px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    border: 1px solid #727173;\n"
                                      "}")
        self.five_day = QtWidgets.QPushButton(weather_form)
        self.five_day.setGeometry(QtCore.QRect(750, 550, 201, 35))
        self.five_day.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.five_day.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.five_day.setInputMethodHints(QtCore.Qt.ImhNone)
        self.five_day.setCheckable(False)
        self.five_day.setAutoRepeat(False)
        self.five_day.setAutoExclusive(False)
        self.five_day.setAutoRepeatDelay(304)
        self.five_day.setObjectName("Favourites")
        self.five_day.setStyleSheet("QPushButton {\n"
                                    "    background-color: /*#000000*/#FF4500;\n"
                                    "    border-radius: 3px;\n"
                                    "    color: #DDA0DD;\n"
                                    "    font: 12pt \"Gotham Pro\";\n"
                                    "    padding-left: 6px;\n"
                                    "    padding-right: 6px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    border: 1px solid #727173;\n"
                                    "}")
        self.buttonGet = QtWidgets.QPushButton(weather_form)
        self.buttonGet.setGeometry(QtCore.QRect(260, 160, 222, 62))
        self.buttonGet.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.buttonGet.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.buttonGet.setAutoFillBackground(False)
        self.buttonGet.setStyleSheet("QPushButton {\n"
                                     "    background-color: /*#B8CCD5*/#FCFAF7;\n"
                                     "    border-radius: 3px;\n"
                                     "    color: #727173;\n"
                                     "    font: 12pt \"Gotham Pro\";\n"
                                     "    padding-left: 6px;\n"
                                     "    padding-right: 6px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    border: 1px solid #727173;\n"
                                     "}")

        self.buttonGet.setInputMethodHints(QtCore.Qt.ImhNone)
        self.buttonGet.setCheckable(False)
        self.buttonGet.setAutoRepeat(False)
        self.buttonGet.setAutoExclusive(False)
        self.buttonGet.setAutoRepeatDelay(304)
        self.buttonGet.setObjectName("buttonGet")
        self.weather_in_city = QtWidgets.QLabel(weather_form)
        self.weather_in_city.setGeometry(QtCore.QRect(120, 240, 502, 42))
        self.weather_in_city.setStyleSheet("QLabel {\n"
                                           "    color: white;\n"
                                           "    font: 20pt \"Gotham Pro Narrow\";\n"
                                           "}\n"
                                           "")
        self.weather_in_city.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.weather_in_city.setFrameShadow(QtWidgets.QFrame.Plain)
        self.weather_in_city.setTextFormat(QtCore.Qt.AutoText)
        self.weather_in_city.setScaledContents(False)
        self.weather_in_city.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_in_city.setWordWrap(False)
        self.weather_in_city.setObjectName("text_weather_in_city")
        self.temp = QtWidgets.QLabel(weather_form)
        self.temp.setGeometry(QtCore.QRect(20, 380, 702, 102))
        self.temp.setStyleSheet("QLabel {\n"
                                "    color: white;\n"
                                "    font: 56pt \"Gotham Pro Narrow\";\n"
                                "}\n"
                                "")
        self.temp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.temp.setFrameShadow(QtWidgets.QFrame.Plain)
        self.temp.setTextFormat(QtCore.Qt.AutoText)
        self.temp.setScaledContents(False)
        self.temp.setAlignment(QtCore.Qt.AlignCenter)
        self.temp.setWordWrap(False)
        self.temp.setObjectName("text_temp")

        self.likes_temp = QtWidgets.QLabel(weather_form)
        self.likes_temp.setGeometry(QtCore.QRect(20, 480, 702, 82))
        self.likes_temp.setStyleSheet("QLabel {\n"
                                      "    color: white;\n"
                                      "    font: 34px \"Gotham Pro Narrow\";\n"
                                      "}\n"
                                      "")
        self.likes_temp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.likes_temp.setFrameShadow(QtWidgets.QFrame.Plain)
        self.likes_temp.setTextFormat(QtCore.Qt.AutoText)
        self.likes_temp.setScaledContents(False)
        self.likes_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.likes_temp.setWordWrap(False)
        self.likes_temp.setObjectName("text_temp_likes")
        self.pressure = QtWidgets.QLabel(weather_form)
        self.pressure.setGeometry(QtCore.QRect(20, 560, 702, 62))
        self.pressure.setStyleSheet("QLabel {\n"
                                    "    color: white;\n"
                                    "    font: 20pt \"Gotham Pro Narrow\";\n"
                                    "}\n"
                                    "")
        self.pressure.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pressure.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pressure.setTextFormat(QtCore.Qt.AutoText)
        self.pressure.setScaledContents(False)
        self.pressure.setAlignment(QtCore.Qt.AlignCenter)
        self.pressure.setWordWrap(False)
        self.pressure.setObjectName("text_pressure")
        self.humidity = QtWidgets.QLabel(weather_form)
        self.humidity.setGeometry(QtCore.QRect(20, 620, 702, 40))
        self.humidity.setStyleSheet("QLabel {\n"
                                    "    color: white;\n"
                                    "    font: 30pt \"Gotham Pro Narrow\";\n"
                                    "}\n"
                                    "")
        self.humidity.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.humidity.setFrameShadow(QtWidgets.QFrame.Plain)
        self.humidity.setTextFormat(QtCore.Qt.AutoText)
        self.humidity.setScaledContents(False)
        self.humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity.setWordWrap(False)
        self.humidity.setObjectName("text_humidity")
        self.speed_wind = QtWidgets.QLabel(weather_form)
        self.speed_wind.setGeometry(QtCore.QRect(20, 660, 702, 40))
        self.speed_wind.setStyleSheet("QLabel {\n"
                                      "    color: white;\n"
                                      "    font: 30pt \"Gotham Pro Narrow\";\n"
                                      "}\n"
                                      "")
        self.speed_wind.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.speed_wind.setFrameShadow(QtWidgets.QFrame.Plain)
        self.speed_wind.setTextFormat(QtCore.Qt.AutoText)
        self.speed_wind.setScaledContents(False)
        self.speed_wind.setAlignment(QtCore.Qt.AlignCenter)
        self.speed_wind.setWordWrap(False)
        self.speed_wind.setObjectName("text_speed_wind")
        self.direction_wind = QtWidgets.QLabel(weather_form)
        self.direction_wind.setGeometry(QtCore.QRect(20, 700, 702, 40))
        self.direction_wind.setStyleSheet("QLabel {\n"
                                          "    color: white;\n"
                                          "    font: 24pt \"Gotham Pro Narrow\";\n"
                                          "}\n"
                                          "")
        self.direction_wind.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.direction_wind.setFrameShadow(QtWidgets.QFrame.Plain)
        self.direction_wind.setTextFormat(QtCore.Qt.AutoText)
        self.direction_wind.setScaledContents(False)
        self.direction_wind.setAlignment(QtCore.Qt.AlignCenter)
        self.direction_wind.setWordWrap(False)
        self.direction_wind.setObjectName("text_direction_wind")
        self.block_snow = QtWidgets.QGroupBox(weather_form)
        self.block_snow.setGeometry(QtCore.QRect(40, 760, 162, 102))
        self.block_snow.setStyleSheet("QGroupBox {\n"
                                      "    color:#006400;\n"
                                      "    font: 24px \"Gotham Pro Medium\";\n"
                                      "}")
        self.block_snow.setAlignment(QtCore.Qt.AlignCenter)
        self.block_snow.setObjectName("block_snow")
        self.snow_in_hour = QtWidgets.QLabel(self.block_snow)
        self.snow_in_hour.setGeometry(QtCore.QRect(20, 36, 124, 22))
        self.snow_in_hour.setStyleSheet("QLabel {\n"
                                     "    color: white;\n"
                                     "    font: 19pt \"Gotham Pro Narrow\";\n"
                                     "}\n"
                                     "")
        self.snow_in_hour.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.snow_in_hour.setFrameShadow(QtWidgets.QFrame.Plain)
        self.snow_in_hour.setTextFormat(QtCore.Qt.AutoText)
        self.snow_in_hour.setScaledContents(False)
        self.snow_in_hour.setAlignment(QtCore.Qt.AlignCenter)
        self.snow_in_hour.setWordWrap(False)
        self.snow_in_hour.setObjectName("text_snow_hour")
        self.snow_3_hour = QtWidgets.QLabel(self.block_snow)
        self.snow_3_hour.setGeometry(QtCore.QRect(20, 64, 124, 22))
        self.snow_3_hour.setStyleSheet("QLabel {\n"
                                       "    color: white;\n"
                                       "    font: 19pt \"Gotham Pro Narrow\";\n"
                                       "}\n"
                                       "")
        self.snow_3_hour.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.snow_3_hour.setFrameShadow(QtWidgets.QFrame.Plain)
        self.snow_3_hour.setTextFormat(QtCore.Qt.AutoText)
        self.snow_3_hour.setScaledContents(False)
        self.snow_3_hour.setAlignment(QtCore.Qt.AlignCenter)
        self.snow_3_hour.setWordWrap(False)
        self.snow_3_hour.setObjectName("text_snow_3_hour")
        self.groupBox_2 = QtWidgets.QGroupBox(weather_form)
        self.groupBox_2.setGeometry(QtCore.QRect(540, 760, 162, 102))
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
                                      "    color:#006400;\n"
                                      "    font: 24px \"Gotham Pro Medium\";\n"
                                      "}")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.rain_hour = QtWidgets.QLabel(self.groupBox_2)
        self.rain_hour.setGeometry(QtCore.QRect(20, 36, 124, 22))
        self.rain_hour.setStyleSheet("QLabel {\n"
                                     "    color: white;\n"
                                     "    font: 19pt \"Gotham Pro Narrow\";\n"
                                     "}\n"
                                     "")
        self.rain_hour.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rain_hour.setFrameShadow(QtWidgets.QFrame.Plain)
        self.rain_hour.setTextFormat(QtCore.Qt.AutoText)
        self.rain_hour.setScaledContents(False)
        self.rain_hour.setAlignment(QtCore.Qt.AlignCenter)
        self.rain_hour.setWordWrap(False)
        self.rain_hour.setObjectName("text_rain_hour")
        self.rain_3_hour = QtWidgets.QLabel(self.groupBox_2)
        self.rain_3_hour.setGeometry(QtCore.QRect(20, 64, 124, 22))
        self.rain_3_hour.setStyleSheet("QLabel {\n"
                                       "    color: white;\n"
                                       "    font: 19pt \"Gotham Pro Narrow\";\n"
                                       "}\n"
                                       "")
        self.rain_3_hour.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rain_3_hour.setFrameShadow(QtWidgets.QFrame.Plain)
        self.rain_3_hour.setTextFormat(QtCore.Qt.AutoText)
        self.rain_3_hour.setScaledContents(False)
        self.rain_3_hour.setAlignment(QtCore.Qt.AlignCenter)
        self.rain_3_hour.setWordWrap(False)
        self.rain_3_hour.setObjectName("text_rain_3_hour")

        self.button_close = QtWidgets.QPushButton(weather_form)
        self.button_close.setGeometry(QtCore.QRect(950, 8, 40, 40))
        self.button_close.setStyleSheet("QPushButton {\n"
                                        "    background-color: /*#A52A2A*/#A52A2A;\n"
                                        "    border:none;\n"
                                        "    font: 19pt \"Arial Black\";\n"
                                        "    color: white;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border: 2px solid red;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border: 2px solid red;\n"
                                        "    color: red;\n"
                                        "}")
        self.button_close.setCheckable(False)
        self.button_close.setDefault(True)
        self.button_close.setFlat(True)
        self.button_close.setObjectName("button_close")

        self.retranslateUi(weather_form)
        QtCore.QMetaObject.connectSlotsByName(weather_form)

    def retranslateUi(self, weather_form):
        _translate = QtCore.QCoreApplication.translate
        weather_form.setWindowTitle(_translate("weather_form", "Weather_finder"))
        self.input_your_city.setPlaceholderText(_translate("weather_form", "Введите город"))
        self.buttonGet.setText(_translate("weather_form", "Получить"))
        self.weather_in_city.setText(_translate("weather_form", "Погода -"))
        self.temp.setText(_translate("weather_form", "-"))
        self.Favourites.setText(_translate("weather_form", "Добавить в избранное"))
        self.likes_temp.setText(_translate("weather_form", "По ощущениям -"))
        self.pressure.setText(_translate("weather_form", "Атмосферное давление -"))
        self.humidity.setText(_translate("weather_form", "Влажность -"))
        self.speed_wind.setText(_translate("weather_form", "Скорость ветра -"))

        self.block_snow.setTitle(_translate("weather_form", "СНЕГ"))
        self.snow_in_hour.setText(_translate("weather_form", "- мм/час"))
        self.snow_3_hour.setText(_translate("weather_form", "- мм/3ч"))
        self.groupBox_2.setTitle(_translate("weather_form", "Дождь"))
        self.rain_hour.setText(_translate("weather_form", "- мм/час"))
        self.rain_3_hour.setText(_translate("weather_form", "- мм/3ч"))
        self.button_close.setText(_translate("weather_form", "X"))
        self.five_day.setText(_translate("weather_form", "Прогноз на 5 дней"))
