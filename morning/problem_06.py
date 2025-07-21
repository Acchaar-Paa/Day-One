# 🧨 PROBLEM 6: Variable Hijack

x = 10
def hijack():
    x = x + 1
    return x
print(hijack())
# 🧠: Will this crash or run? Why? Which chapter concept is violated?
# it will crash because we dont assagi x before use it if we want to use it we need to assign it first 
# its variable chapter