data = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
result = ""
n = input()

for index,item in enumerate(n[:-1]):
    num = int(item+("0"*(len(n[index+1:]))))
    print(num)