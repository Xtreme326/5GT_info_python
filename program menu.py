print("Welcome to my restaurant!")
print("For a hamburger press 1")
print("For a pizza press 2")
print("For a salad press 3")
order=input("What will you choose ?")
order=int(order)


while order not in [1,2,3]:
  print("Please choose the right number")
  order=input("What will you choose ?")
  order=int(order)

if order==1:
  print("You have ordered a hamburger.")
elif order==2:
  print("You have ordered a pizza.")
elif order==3:
  print("You have ordered a salad.")