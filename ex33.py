i = 0
numbers = []

def loop(max, step):
    global i
    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


print(f"The numbers: ")

loop(10, 2)
for num in numbers:
    print(num)
