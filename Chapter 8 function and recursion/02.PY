def blast(power, mode="focus"):
    return f"{power} — {mode}"

x = blast("Speed")
y = blast("Logic", "Overdrive")
# IF WE PRINT x THEN OUTPUT WOULD BE : speed — focus 
# IF WE PRINT y THEN OUTPUT WOULD BE : Logic  — focus
print(x,y)