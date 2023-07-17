# 7/17/2023
# Margarita Chistiakova
# Vampire Numbers Project

def vampireNumber(fang1, fang2):
  fang1_str = str(fang1)
  fang2_str = str(fang2)
  product_str = str(fang1 * fang2) 
  if len(fang1_str) + len(fang2_str) != len(product_str):
        return False
  return True

print("Welcome to the 'Vampire numbers' project!\n")

print("""Here is an example of a vampire number:
15 * 93 = 1395
15 and 93 would be valid 'fangs' for a vampire number as the 
digits 1, 5, 9, and 3 are present in both the product and multiplication\n
""")

print("Now you can yourself try and check if two numbers form a vampire number!")
print("Please enter the first number: ")
fang1 = int(input())
print("Please enter the second number: ")
fang2 = int(input())


if vampireNumber(fang1, fang2):
    print(f"\n{str(fang1 * fang2)} is a vampire number.")
else:
    print(f"\n{str(fang1 * fang2)} is not a vampire number.")