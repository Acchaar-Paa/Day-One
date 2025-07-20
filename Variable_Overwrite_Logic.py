x = [20]

def change():
    x[0] = 10  # ← Mutates global list content

change()
print(x)  # Output: [10]
