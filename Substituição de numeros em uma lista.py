hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

n = int(input("Digite um valor inteiro:"))
hat_list[2] = n
del hat_list [-1]
print ("Tamanho da lista: ", len(hat_list))
print(hat_list)
