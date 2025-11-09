class HourClock:
    def __init__(self, hours: int) -> None:
        self.hours = hours

    @property
    def hours(self) -> int:
        return self.hour

    @hours.setter
    def hours(self, new_hour: int) -> None:
        if not isinstance(new_hour, int) or new_hour not in range(1, 13):
            raise ValueError("Некорректное время")
        self.hour = new_hour


# INPUT DATA:

# TEST_1:
time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)

# TEST_2:
time = HourClock(7)

try:
    time.hours = 15
except ValueError as e:
    print(e)

# TEST_3:
try:
    HourClock("pizza time 🕷")
except ValueError as e:
    print(e)

# TEST_4:
try:
    HourClock(0)
except ValueError as e:
    print(e)

# TEST_5:
try:
    HourClock("ten o`clock")
except ValueError as e:
    print(e)

# TEST_6:
time = HourClock(1)

print(time.hours)
for _ in range(11):
    time.hours += 1
    print(time.hours)

# TEST_7:
time = HourClock(1)
print(hasattr(HourClock, "hours"))
