# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


Certas expressões podem ser simplificadas sem alterar o comportamento do programa.

Tente lembrar-se de como o Python interpreta a verdade de uma condição e observe que estas duas formas são equivalentes:

while number != 0: e while number:.

A condição que verifica se um número é ímpar também pode ser codificada nestas formas equivalentes:

if number % 2 == 1: e if number % 2:.


Usar uma variável counter para sair de um loop
Veja o snippet abaixo:

counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)


Este código destina-se a imprimir a string "Inside the loop." e o valor armazenado na variável counter durante um determinado loop exatamente cinco vezes. Uma vez que a condição não foi atendida (a variável counter atingiu 0), o loop é encerrado, e a mensagem "Outside the loop." bem como o valor armazenado em counter é impresso.

Mas há uma coisa que pode ser escrita de forma mais compacta - a condição do loop while .

Consegue ver a diferença?

counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)
