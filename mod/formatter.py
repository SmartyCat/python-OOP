from functools import singledispatchmethod


class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(arg) -> None:
        raise TypeError("Аргумент переданного типа не поддерживается")

    @format.register(int)
    @format.register(float)
    def _format_int_float(arg) -> None:
        print(
            f"{"Целое число" if isinstance(arg,int) else "Вещественное число"}: {arg}"
        )

    @format.register(list)
    @format.register(tuple)
    def _format_list_tuple(arg) -> None:
        print(
            f"{"Элементы списка" if isinstance(arg,list) else "Элементы кортежа"}: {", ".join(f"'{a}'" if isinstance(a,str) else str(a) for a in arg)}"
        )

    @format.register(dict)
    def _format(arg) -> None:
        print(f"Пары словаря: {", ".join(str(a) for a in arg.items())}")
