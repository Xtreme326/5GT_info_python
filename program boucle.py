choix="o"
while choix=="o":
  print("Bonjour")
  choix=input("Voulez-vous continuer ?")

while choix not in ["o","n"]:
 print("Veuillez répondre par oui(o) ou non(n)")
 choix=input("Voulez-vous continuer ?")

print("Au revoir")