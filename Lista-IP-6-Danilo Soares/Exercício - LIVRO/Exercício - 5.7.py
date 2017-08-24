x = (int(input("Tabuada começa em = ")))
y = (int(input("Tabuada termina em = ")))
n = (int(input("Tabuada do número = ")))

while x <= y:
     print("{} * {} = " .format(n,x),end="")
     print(n * x)
     x = x + 1
