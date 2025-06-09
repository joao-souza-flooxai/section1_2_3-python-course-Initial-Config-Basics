
import decimal
numero_1 = 0.1
numero_2 = decimal.Decimal(0.7) #erro
numero_3 = numero_1 + 0.2
print (numero_3)
print(f'{numero_3:.2f}') 
print(round(numero_3, 2))
print(numero_2)
numero_2 = decimal.Decimal("0.7") #correto
print(numero_2)