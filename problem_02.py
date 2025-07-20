# 🧨 PROBLEM 2: String Trap

# What's the final output? Explain why it's that and not something else.
msg = "AttackAtDawn"
print(msg[::2] + msg[::-2])
# 🧠: What's slicing doing here? What happens if we reverse with a step?

#          a   t  t  a c k a t d a w n
#          -12-11-10-9-8-7-6-5-4-3-2-1
#  a t t a c k a t d a w n
#  0 1 2 3 4 5 6 7 8 9 0 11
# atcadw + natkat
#  ans will be atcadwnatkat
#FOR THIS I UNDERSTAND HOW IT WORKS FIRST I TRY AND SEE OUTPUT THEN I KNOW WHERE I WAS UNDERSTAND INSTANTLY THEN I CORRECT MYSELF