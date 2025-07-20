# 🧨 PROBLEM 1: Set Fusion Weapon
# What will be the output of this? Explain why.
a = {1, 2, 3}
b = {3, 4, 5}
c = a & b #this is AND and its give that value which is IN A AND ALSO IN b 
d = a | b #this is OR its give me that valuse which is  a and also in b without repeating
e = a - b # its minis that valuse which is in a and b
print(sorted(list(c + d - e)))
# 🧠: Explain each operation (&, |, -) and why this fails or passes.
# becasue of + we can + two sets without add we can use .add 
#FOR THIS I NEED TO SEE THE OUTPUT 