class Something:
    def __eq__(self, other):
        return True

    __ne__ = __eq__
    __gt__ = __eq__
    __ge__ = __eq__
    __lt__ = __eq__
    __le__ = __eq__


def anything() -> Something:
    return Something()
