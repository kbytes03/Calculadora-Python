#calculadora
#Pode adicionar, subtrair, multiplar e dividir

print("Selecione uma operacao:")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

operation = input()

if operation == "1":
	num1 = input("Seu primeiro numero:")
	num2 = input("Seu segundo numero:")
	print("A soma e " + str(int(num1) + int(num2)))

elif operation == "2":
	num1 = input("Seu primeiro numero:")
	num2 = input("Seu segundo numero:")
	print("A diferenca e " + str(int(num1) - int(num2)))


elif operation == "3":
	num1 = input("eSeu primeiro numero:")
	num2 = input("Seu segundo numero:")
	print("A multiplicacao e " + str(int(num1) * int(num2)))


elif operation == "4":
	num1 = input("Seu primeiro numero:")
	num2 = input("Seu segundo :")
	print("A divisao e" + str(int(num1) / int(num2)))


else:
	print("Entrada invalida")
