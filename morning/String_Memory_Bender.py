# 🔥 Q3: String Memory Bender
s = "hehhlo"
ind =s.index("h")
# s[0] = "H"
# print(s)
# Will this work? Why or why not?
# Then, fix it without using slicing or replace — but by rebuilding manually.
#it wont work because string a immutable
x = ""
for i in s :
    if "h" == s[0]:
        x += i.upper()
    else:
        x +=i
s =x 
print(s)