"""С помощью наследования и приведенной ниже схемы постройте
иерархию пустых классов:"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(A):
    pass


class E(B, D):
    pass


# TEST_4:
print(issubclass(E, A))
