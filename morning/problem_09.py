# 🧨 PROBLEM 9: Loop Weapon Mix
s = "loops"
out = ""
i = 0
while i < len(s):
    if i % 2 == 0:
        out += s[i].upper()
    else:
        out += s[i]
    i += 1
print(out)
# 🧠: Predict the exact output. What logic is being used?
# this is the ans = LoOpS