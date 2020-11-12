age = int(input("Quel est votre age?"))

if age >= 18:
    print("Vous êtes majeur")

else:
    print("Vous êtes mineur")

table = int(input("De Quelle nombre voulez vous la table de multiplication?"))

i = 0
while i < 10:
    i+= 1
    if i <= 10:
        print(i,"x",table,"=",i * table)

table2 = int(input("De Quelle nombre voulez vous la table de multiplication?"))


for i in range(1,11):
    print(i,"x",table2,"=",i * table2)