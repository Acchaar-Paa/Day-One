# ⚔️ WAR DRILL LEVEL 3: STRING TRANSFORMATION COMBAT
# 03.
# Rebuild this string "ry" in reverse — but without using:

# [::-1]

# reversed()

# .join()

# slicing at all

# ❗ You must do it only with loop logic.
# Then, explain why this works.
a = "legendary"
z = ""
for i in a:
    z = i+z
print(z)
# let me explain how its works firtly i make a and z variable a = legendary and z ="" empty tring for later to store value i run for loop i in a that how if a[0] = l then i = l then i say z = i+z if i = l and z is empty then its look like z = "l"+"" and then if i = e its look like z = "e"+"l" ="el" its how its works
