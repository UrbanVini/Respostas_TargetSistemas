string = input("Digite uma string: ")
invert = ""

for i in range(len(string)-1, -1, -1):
    invert += string[i]

print("String invertida:", invert)