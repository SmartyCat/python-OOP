from functools import singledispatchmethod


class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(arg) -> None:
        raise TypeError("Аргумент переданного типа не поддерживается")

    @neg.register(int)
    @neg.register(float)
    def _neg_int_float(arg) -> int | float:
        return -1 * arg

    @neg.register(bool)
    def _neg_bool(arg) -> bool:
        return not arg
