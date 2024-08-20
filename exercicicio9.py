

quantidade = int(input("Digite a quantidade de fotocópias realizadas: "))

#valor da fatura
fatura = 0.0


if quantidade <= 10:
    fatura = quantidade * 0.25
if quantidade <= 20:
    fatura = (10 * 0.25) + ((quantidade - 10) * 0.20)
else:
    fatura = (10 * 0.25) + (20 * 0.10) + ((quantidade - 20) * 0.10)

#valor da fatura
print(f"O valor da fatura para {quantidade} fotocópias é R$ {fatura:.2f}")