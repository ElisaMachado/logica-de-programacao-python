n1 = float(input("Qual foi a sua 1ª nota?"))
n2 = float(input("Qual foi a sua 2ª nota?"))

m = (n1 + n2) / 2

print(f"Sua média é de {m:.2f}")

if 9 <= m <= 10:
    print("Você tirou nota A!")
    
elif m >= 8:
    print("Você tirou nota B!")

elif m >= 7:
    print("Você tirou nota C!")

elif m >= 6:
    print("Você tirou nota D!")

elif m >= 5:
    print("Você tirou nota E!")

else:
    print("Você tirou nota F!") 
