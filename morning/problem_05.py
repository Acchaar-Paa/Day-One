# 🧨 PROBLEM 5: Nested Chaos

matrix = [[1,2],[3,4],[5,6]]
flat = []
for row in matrix:
    for num in row:
        if num % 2 == 0:
            continue
        flat.append(num*10)
print(flat)
# 🧠: Predict exact output. Explain logic of inner loop + continue.
# the ans is 10 30 50 in list becuase we use nested loop and we say if num % 2 is equal to 0 then skip that value if not then multiple that number with 10 and add it in flat list