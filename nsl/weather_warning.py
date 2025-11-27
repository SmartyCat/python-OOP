from datetime import date

"""Реализуйте класс WeatherWarning , описывающий объект, предупреждающий о
погодных изменениях. При создании экземпляра класс не должен принимать
никаких аргументов.
Класс WeatherWarning должен иметь три метода экземпляра:
•
rain() — метод, выводящий текст:
Ожидаются сильные дожди и ливни с грозой
•
snow() — метод, выводящий текст:
Ожидается снег и усиление ветра
•
low_temperature() — метод, выводящий текст:
Ожидается сильное понижение температуры
Также реализуйте класс WeatherWarningWithDate , наследника
класса WeatherWarning , описывающий объект, предупреждающий о погодных
изменениях с указанием даты. Процесс создания экземпляра
класса WeatherWarningWithDate должен совпадать с процессом создания
экземпляра класса WeatherWarning .
Класс WeatherWarningWithDate должен иметь три метода экземпляра:
•
rain() — метод, принимающий в качестве аргумента дату (тип date ) и
выводящий текст:
•
<дата в формате DD.MM.YYYY>
Ожидаются сильные дожди и ливни с грозой
•
snow() — метод, принимающий в качестве аргумента дату (тип date ) и
выводящий текст:
•
<дата в формате DD.MM.YYYY>
Ожидается снег и усиление ветра
•
low_temperature() — метод, принимающий в качестве аргумента дату
(тип date ) и выводящий текст:
•
<дата в формате DD.MM.YYYY>Ожидается сильное понижение температуры
Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными
данными.
Примечание 2. Никаких ограничений касательно реализации классов нет, она
может быть произвольной."""


class WeatherWarning:
    def rain(self) -> None:
        print("Ожидаются сильные дожди и ливни с грозой")

    def snow(self) -> None:
        print("Ожидается снег и усиление ветра")

    def low_temperature(self) -> None:
        print("Ожидается сильное понижение температуры")


class WeatherWarningWithDate(WeatherWarning):
    default = "%d.%m.%Y"

    def rain(self, d: date) -> None:
        print(d.strftime(WeatherWarningWithDate.default))
        super().rain()

    def snow(self, d: date) -> None:
        print(d.strftime(WeatherWarningWithDate.default))
        super().snow()

    def low_temperature(self, d: date) -> None:
        print(d.strftime(WeatherWarningWithDate.default))
        super().low_temperature()
