import requests as req


from PyQt5 import QtWidgets, QtCore
from weath_des import Design


class MainWindow(QtWidgets.QMainWindow, Design):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.buttonGet.clicked.connect(self.pressed_get)
        self.button_close.clicked.connect(self.close)
        self.Favourites.clicked.connect(self.beta_Favour)
        self.five_day.clicked.connect(self.beta_five_day)

    def pressed_get(self):

        city = self.input_your_city.text()

        rs = req.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'q': city, 'lang': 'ru', 'units': 'metric', 'APPID': "9d0864cfefebb1ec3592e7379f7776af"})
        weath = rs.json()
        if "message" in weath.keys():
            try:
                if weath["cod"] == "404":
                    self.weather_in_city.setText("Вы ввели неверный город")

                elif weath["cod"] == "400":
                    self.weather_in_city.setText("Вы не ввели город")

                elif weath["cod"] == "429":
                    self.weather_in_city.setText("Ошибка приложения")

                else:
                    self.weather_in_city.setText("Ошибка сервера")

                self.temp.setText("--° C")
                self.temp.show()
                self.likes_temp.setText("По ощущениям --° C")
                self.likes_temp.show()
                self.pressure.setText("Атмосферное давление --- мм.рт.ст")
                self.pressure.show()
                self.humidity.setText("Влажность --- %")
                self.humidity.show()
                self.speed_wind.setText("Скорость ветра --- м/с")
                self.speed_wind.show()
                self.direction_wind.setText("Направление ветра ---")
                self.direction_wind.show()
                self.block_snow.show()
                self.snow_in_hour.setText("----")
                self.snow_in_hour.show()
                self.snow_3_hour.setText("----")
                self.snow_3_hour.show()
                self.groupBox_2.show()
                self.rain_hour.setText("----")
                self.rain_hour.show()
                self.rain_3_hour.setText("----")
                self.rain_3_hour.show()


            except KeyError:
                self.weather_in_city.setText("Ошибка приложения")
                self.temp.hide()
                self.likes_temp.hide()
                self.pressure.hide()
                self.humidity.hide()
                self.speed_wind.hide()
                self.direction_wind.hide()
                self.block_snow.hide()
                self.snow_in_hour.hide()
                self.snow_3_hour.hide()
                self.groupBox_2.hide()
                self.rain_hour.hide()
                self.rain_3_hour.hide()


        else:
            try:
                self.weather_in_city.setText("Погода " + str(weath["name"]))
            except KeyError:
                self.weather_in_city.setText("Погода неизвестна")
            finally:
                self.weather_in_city.show()

            try:
                self.temp.setText(str(weath["main"]["temp"]) + "° C")
            except KeyError:
                self.temp.setText("--° C")
            finally:
                self.temp.show()

            try:
                self.likes_temp.setText("По ощущениям " + str(weath["main"]["feels_like"]) + "° C")
            except KeyError:
                self.likes_temp.setText("По ощущениям --° C")
            finally:
                self.likes_temp.show()

            try:
                self.pressure.setText(
                    "Атмосферное давление " + str(round(weath["main"]["pressure"] * 0.75)) + " мм.рт.ст")
            except KeyError:
                self.pressure.setText("Атмосферное давление --- мм.рт.ст")
            finally:
                self.pressure.show()

            try:
                self.humidity.setText("Влажность " + str(weath["main"]["humidity"]) + " %")
            except KeyError:
                self.humidity.setText("Влажность --- %")
            finally:
                self.humidity.show()

            try:
                self.speed_wind.setText("Скорость ветра " + str(weath["wind"]["speed"]) + " м/с")
            except KeyError:
                self.speed_wind.setText("Скорость ветра --- м/с")
            finally:
                self.speed_wind.show()

            try:
                self.snow_in_hour.setText(str(weath["snow"]["1h"]) + "мм/ч")
            except KeyError:
                self.snow_in_hour.setText("--- мм/ч")
            finally:
                self.snow_in_hour.show()
                self.block_snow.show()

            try:
                self.snow_3_hour.setText(str(weath["snow"]["3h"]) + " мм/3ч")
            except KeyError:
                self.snow_3_hour.setText("--- мм/3ч")
            finally:
                self.snow_3_hour.show()
                self.block_snow.show()

            try:
                self.rain_hour.setText(str(weath["rain"]["1h"]) + "мм/ч")
            except KeyError:
                self.rain_hour.setText("--- мм/ч")
            finally:
                self.rain_hour.show()
                self.groupBox_2.show()

            try:
                self.rain_3_hour.setText(str(weath["rain"]["3h"]) + " мм/3ч")
            except KeyError:
                self.rain_3_hour.setText("--- мм/3ч")
            finally:
                self.rain_3_hour.show()
                self.groupBox_2.show()

    def beta_Favour(self):
        _translate = QtCore.QCoreApplication.translate
        self.Favourites.setText(_translate("weather_form", "В разработке"))

    def beta_five_day(self):
        _translate = QtCore.QCoreApplication.translate
        self.five_day.setText(_translate("weather_form", "В разработке"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
