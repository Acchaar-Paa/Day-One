# Q8: Why is the following code broken logic-wise? Explain.

def build():
    print("Building...")
    return

print(build() + " complete!")
#because we use print  and use retur with assigning any values its cause it broke