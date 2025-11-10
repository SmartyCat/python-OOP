from functools import singledispatchmethod


class Processor:

    @singledispatchmethod
    @staticmethod
    def process(arg) -> None:
        raise TypeError("Аргумент переданного типа не поддерживается")

    @process.register(float)
    @process.register(int)
    def _from_int_float_process(arg) -> int:
        return arg * 2

    @process.register(str)
    def _from_str_process(arg) -> str:
        return arg.upper()

    @process.register(tuple)
    @process.register(list)
    def _from_tuple_list_process(arg) -> list | tuple:
        return arg[::-1]


print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process("hello"))
print(Processor.process((4, 3, 2, 1)))
print(Processor.process([3, 2, 1]))

try:
    Processor.process({1, 2, 3})
except TypeError as e:
    print(e)
