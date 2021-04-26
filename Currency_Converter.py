import time
print ("Welcome to the currency converter. In this currency converter you can choose to convert ($ to £) or (£ to $).")
print (" ")
time.sleep (1)
Choice1 = input ("What currency would you like to convert from? (GBP or USD): ")
print (" ")


if Choice1 == "GBP":
  GBP = float(input("Input your amount in Pounds: £"))
  USD = (GBP * 1.3887)
  Choice2 = input("Do you want that in USD? (yes or no): ")
  
  if Choice2 == ("Yes") or ("yes") or ("y"):
    print ("£",GBP, "is equal to:")
    print ("$", USD)

  elif Choice2 == ("No") or ("no") or ("n"):
    print ("Thank you for using my currency converter, come back next time :)")


elif Choice1 == "USD":
  USD = float(input("Input your amount in Dollars: $"))
  GBP = (USD * 0.72009793)
  Choice3 = input("Do you want that in GBP? (yes or no): ")

  if Choice3 == ("Yes") or ("yes") or ("y"):
    print ("$",USD, "is equal to:")
    print ("£", GBP)

  elif Choice3 == ("No") or ("no") or ("n"):
    print ("Thank you for using my currency converter, come back next time :)")
