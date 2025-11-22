class Atomic:
    def __init__(self, data: list | set | dict, deep: bool = False) -> None:
        if deep and isinstance(data, (list, set)):
            self.__first = [d.copy() if isinstance(d, (list, set)) else d for d in data]
        elif deep and isinstance(data, dict):
            self.__first = {
                d: data[d].copy() if isinstance(data[d], dict) else data[d]
                for d in data
            }
        else:
            self.__first = data.copy()
        self.__second = data

    def __enter__(self) -> list | set | dict:
        return self.__second

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if exc_value:
            self.__second.clear()
            for i in self.__first:
                if isinstance(self.__second, list):
                    self.__second.append(i)
                elif isinstance(self.__second, set):
                    self.__second.add(i)
                else:
                    self.__second[i] = self.__first[i]
        return True
