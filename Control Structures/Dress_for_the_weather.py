# Dress for the Weather

temp = float(input("What is the temperature? "))

if temp < 40:
    print("Wear a coat.")
elif temp < 70:
    print("Wear a jacket.")
elif temp < 100:
    print("Wear something cool.")
elif temp >= 100:
    ac = input("Do you have air conditioning? (yes/no) ")
    if ac == "yes":
        print("Stay home.")
    else:
        print("Tuff.")
