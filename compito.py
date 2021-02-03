#questo programma riordina in ordine crescente tre numeri
num1=int(input("inserisci il primo numero "))
num2=int(input("inserisci il secondo numero "))
num3=int(input("inserisci il terzo numero "))
if num1 >= num2:
    if num3 <= num2:
        print("l'ordine dei numeri è: ", num3, num2, num1)
    elif num3 >= num1:
        print("l'ordine dei numeri è: ", num2, num1, num3)
    else:
        print("l'ordine dei numeri è: ", num2, num3, num1)
else:
    if num3 <= num1:
        print("l'ordine dei numeri è: ", num3, num1, num2)
    elif num3 >= num2:
        print("l'ordine dei numeri è: ", num1, num2, num3)
    else:
        print("l'ordine dei numeri è: ", num1, num3, num2)