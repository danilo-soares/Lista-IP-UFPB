numeroa=(float(input("Digite o número = ")))
numerob=(float(input("Digite o número = ")))
numeroc=(float(input("Digite o número = ")))

if (numeroa > numerob and numeroa > numeroc ):
    print(" {} é maior que {} e {} " .format(numeroa,numerob,numeroc))
elif(numerob > numeroa and numerob > numeroc):
    print(" {} é maior que {} e {} " .format(numerob,numeroa,numeroc))
else :
    print(" {} é maior que {} e {} " .format(numeroc,numerob,numeroa))
