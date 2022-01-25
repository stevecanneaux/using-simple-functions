#using simple functions
def calcsalestax(aPrice, aSalestax):
    total = aPrice+(aPrice * aSalestax/100)
    print("total cost: ", total)

calcsalestax(80.00, 10.00)
