from string import ascii_letters
from typing import Callable


"""Реализуйте класс CaesarCipher для шифровки и дешифровки текста с
помощью шифра Цезаря. При создании экземпляра
класса CaesarCipher должен указываться сдвиг, который будет
использоваться при шифровке и дешифровке. За операцию шифрования
должен отвечать метод encode() , за операцию дешифрования — decode() :
cipher = CaesarCipher(5)
print(cipher.encode('Beegeek'))# Gjjljjp
print(cipher.decode('Gjjljjp'))# Beegeek
Обратите внимание, что при шифровке сдвиг должен происходить вправо,
также заметьте, что регистр букв при шифровке и дешифровке должен
сохраняться.
Шифровке и дешифровке должны подвергаться только буквы латинского
алфавита, все остальные символы, если они присутствуют, должны
оставаться неизменными:
print(cipher.encode('Биgeek123'))# Биljjp123
print(cipher.decode('Биljjp123'))# Биgeek123
Примечание 1. Гарантируется, что сдвигом является число из диапазона [1;
26] ."""


class CaesarCipher:
    def __init__(self, n: int) -> None:
        self.n = n

    @staticmethod
    def support(func: Callable, string: str, n: int) -> str:
        result = []
        for i in string:
            if i in ascii_letters:
                if func.__name__ == "encode":
                    result.append(
                        ascii_letters[(ascii_letters.index(i) + n) % len(ascii_letters)]
                    )
                elif func.__name__ == "decode":
                    result.append(
                        ascii_letters[(ascii_letters.index(i) - n) % len(ascii_letters)]
                    )
            else:
                result.append(i)
        return "".join(result)

    def encode(self, string: str) -> str:
        return CaesarCipher.support(self.encode, string, self.n)

    def decode(self, string: str) -> str:
        return CaesarCipher.support(self.decode, string, self.n)
