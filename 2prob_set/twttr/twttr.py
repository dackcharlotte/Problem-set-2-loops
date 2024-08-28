s = input("Input: ")

vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

print("Output: ", end="")

temp = ""

for i in s:
    if i not in vowels:
        print(i, end="")
        temp = temp + i

print(temp)


