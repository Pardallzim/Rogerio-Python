x = float(input("Salario atual do funcionario: "))

if x <= 500:
    x = (x * 1.15)
    print(x)
elif x > 500 and x <= 1000:
    x = (x * 1.1)
    print(x)
else:
    x = (x * 1.05)
    print(x)