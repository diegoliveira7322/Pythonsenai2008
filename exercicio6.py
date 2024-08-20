m = float(input("Digite o primeiro número (m): "))

# Solicita ao usuário que insira o segundo número
n = float(input("Digite o segundo número (n): "))

# Calcula o produto dos dois números
produto = m * n

# Verifica se o produto é positivo, negativo ou zero
if produto > 0:
    print("O produto de", m, "e", n, "é positivo.")
elif produto < 0:
    print("O produto de", m, "e", n, "é negativo.")
else:
    print("O produto de", m, "e", n, "é zero.")