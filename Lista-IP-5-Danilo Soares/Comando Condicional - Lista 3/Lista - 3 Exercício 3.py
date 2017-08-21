quantidade= (int(input("Digite a quantidade de pessoas = ")))
totalpessoas = quantidade

cpbus= 42
cpvan= 20

precobus= 350
precovan= 200


nbus = totalpessoas // cpbus
numpessoas = totalpessoas % cpbus

nvans = numpessoas // cpvan
numpessoas = numpessoas % cpvan

if numpessoas > 0:
    nvans += 1

print("{} onibus e {} vans" .format(nbus,nvans))

valortotal =((nbus*precobus) + (nvans*precovan))/totalpessoas

print("R$ {} por pessoa" .format(valortotal))
