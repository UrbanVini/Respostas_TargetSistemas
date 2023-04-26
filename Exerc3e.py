a, b = 1, 2
fibonacci = [a, b]
while b < 100:  # ou qualquer limite desejado
    a, b = b, a + b
    fibonacci.append(b)

print(fibonacci)



