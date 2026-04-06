is_raining=True

if is_raining==True:
    print("It's raining, take an umbrella!")
else:
    print("It's not raining, enjoy your day!")


taka=int(input("Enter amount in taka: "))

if taka%2==0:
    print("Taka is even.")
elif taka<0:
    print("Taka is negative.")
else:
    print("Taka is odd.")


a=[1,2,3,4,5]
if 1 in a:
    print("1 is present in the list a")