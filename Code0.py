# Set up a proportion:
# n1/d1 = n2/d2
# Put a zero in for the unkown value
n1 = input("Enter your n1 :  ")
d1 = input("Enter your d1 :  ")
n2 = input("Enter your n2 :  ")
d2 = input("Enter your d2 :  ")
n1 = int(n1)
d1 = int(d1)
n2 = int(n2)
d2 = int(d2)
if n1 == 0:
  awnser = d1 * n1 / d2
  print(f"{awnser}/{d1} = {n2}/{d2}") 
if d1 == 0:
  awnser = n1 * d2 / n2
  print(f"{n1}/{awnser} = {d1}/{d2}")
if n2 == 0:
  awnser = d2 * n1 / d1
  print(f"{n1}/{d1} = {awnser}/{d2}")
if d2 == 0:
  awnser = n2 * d1 / n1
  print(f"{n1}/{d1} = {n2}/{awnser}")
