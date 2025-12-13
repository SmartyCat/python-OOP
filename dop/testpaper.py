"""В этой задаче вам необходимо реализовать класс Testpaper , который
позволит составлять экзаменационные тесты. Каждый тест должен
создаваться на основе темы, схемы верных ответов и минимального
процента верных решений:
testpaper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'],
'60%')
testpaper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
testpaper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D',
'6C', '7A'], '75%')
Созданные тесты должны сдаваться студентом — экземпляром
класса Student . Он должен иметь метод take_test() , который принимает в
качестве аргументов тест и ответы студента на этот тест:
student1 = Student()
student2 = Student()
student1.take_test(testpaper1, ['1A', '2D', '3D', '4A', '5A'])
student2.take_test(testpaper2, ['1C', '2D', '3A', '4C'])
student2.take_test(testpaper3, ['1A', '2C', '3A', '4C', '5D', '6C',
'7B'])
Результаты тестов должны быть доступны в виде словаря, ключом в котором
является тема теста, а значением — результат теста (сдан или не сдан), а
также процент верных решений:
print(student1.tests_taken)# {'Maths': 'Passed! (80%)'}
print(student2.tests_taken)
'Computing': 'Failed! (43%)'}# {'Chemistry': 'Failed! (25%)',
Если студент еще не сдал ни одного теста, атрибут tests_taken должен
содержать строку No tests taken :
student3 = Student()
print(student3.tests_taken)
# No tests takenПримечание 1. Округление процента верных решений должно происходить до
ближайшего целого числа."""


class Testpaper:
    def __init__(self, subject: str, answers: list[str], percent: str) -> None:
        self.subject, self.answers, self.percent = subject, answers, percent


class Student:
    def __init__(self) -> None:
        self.data = {}

    def take_test(self, test: Testpaper, answers: list[str]) -> None:
        result = sum(i[0] == i[1] for i in zip(test.answers, answers))
        result = round((result * 100) / len(test.answers))
        self.data[test.subject] = (
            f"Passed! ({result}%)"
            if result >= int(test.percent[:-1])
            else f"Failed! ({result}%)"
        )

    @property
    def tests_taken(self) -> dict:
        if self.data:
            return self.data
        return "No tests taken"
