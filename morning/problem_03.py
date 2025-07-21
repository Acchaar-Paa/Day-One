# 🧨 PROBLEM 3: Loop Cipher
x = [10, 20, 30, 40]
y = 0
for i in x:
    y += i
    if y > 50:
        break
    else:
        y += 5
print(y)
# 🧠: What's the final output? Break down how break and else work together.

# 10 +5 =15
# 35 +5 = 40
# 40 + 30 = 70 which is greater than 50 then it will break it 
#corrected