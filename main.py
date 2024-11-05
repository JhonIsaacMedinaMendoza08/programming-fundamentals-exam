volt1 = int(input("enter voltage: "))
volt2 = int(input("enter voltage: "))
volt3 = int(input("enter voltage: "))
volt4 = int(input("enter voltage: "))
volt5 = int(input("enter voltage: "))
VoltajeFInal = ((volt1+volt2+volt3+volt4+volt5)/5)
if VoltajeFInal > 220:
    print ("HIGH VOLTAGE")
else:
    print ("CORRECT VOLTAGE")