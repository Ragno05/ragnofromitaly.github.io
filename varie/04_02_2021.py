#verificatore numeri primi
numero=int(input("inserisci un numero"))
divisore = 1
divisori = 0
while numero >= divisore:
      if numero % divisore == 0:
            divisori = divisori + 1
      divisore = divisore + 1
if divisori == 2:
      print("il numero è primo")
else:
      print("il numero non è primo")
