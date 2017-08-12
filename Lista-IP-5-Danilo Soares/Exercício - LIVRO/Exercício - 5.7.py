x = (int(input("Tabuada começa em : ")))
n = (int(input("Tabuada do : ")))

while x <= 10:
     print("{} * {} = " .format(n,x),end="")
     print(n * x)
     x = x + 1
