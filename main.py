print ("Exercise 3 Voltages")
print ("Please, Enter different voltages")
volt1 = int(input("Enter voltage: "))
volt2 = int(input("Enter voltage: "))
volt3 = int(input("Enter voltage: "))

prom = (volt1+volt2+volt3)/3

if volt1 != volt2 and volt1 != volt3 and volt2 !=volt3:
    if prom < 115:
        print (f"CORRECT VOLTAGE {prom}")
    elif prom >115 and prom < 220:
        print (f"CORRECT VOLTAGE {prom}")
    else:
        print (f"DANGEROUS {prom}")
else:
    print ("Please, enter different voltages")
    