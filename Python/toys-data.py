# Application Title
print("")
print("Children's Toy Store ")
print("********************************************")
print("")

# Enter Purchase Data
buyerName = str(input("Enter Buyer Name : "))
toycode = str(input("Enter game code : "))
toyprice = int(input("Enter Price : "))
purchaseAmount = int(input("Enter Purchase Amount : "))
totalPay = toyprice * purchaseAmount

# Display Barrier
print("")
print("==============================================" )
print("")

# Print Purchase Data Input Results
print("Buyer Name =", buyerName)
print("Toy Code =",toycode)
print("Price=",toyprice)
print("Amount of Purchase=", purchaseAmount)
print("Amount = ", totalPay)
print("")
