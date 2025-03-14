import datetime

nom1=input("Quel est ton nom ?")
annee1=input("En quelle année es tu née ?")
annee1=int(annee1)
nom2=input("Quel est le nom de ton voisin ?")
annee2=input("En quelle année ton/ta voisin(e) est-il né(e) ?")
annee2=int(annee2)

now= datetime.datetime.now()
now_year=now.year
print(now)

age1=now_year-annee1
age2=now_year-annee2

print(nom1,"a",age1,"ans.")
print(nom2,"a",age2,"ans.")

if age1>age2:
  difference=age1-age2
  print(nom1, "est plus agé que",nom2)
  print(nom1,"a",difference,"années de plus que",nom2,)
  
elif age1==age2:
  print(nom1, "et",nom2, "ont le meme age")
  
elif age2>age1:
  difference=age2-age1
  print(nom2, "est plus agé que",nom1)
  print(nom2, "a",difference,"années de plus que",nom1,)

else:
  print("There seems to have been an error.")

if age1>age2:
  print(nom1, "est",annee1-annee2, "plus agé que",nom2)
elif age1==age2:
  print(nom1, "et", nom2, "ont 0 année(s) de difference")
elif age2>age1:
    print(nom2, "est" ,annee2-annee1,  "plus agé que", nom1)
else:
  print("There seems to have been an error")
  