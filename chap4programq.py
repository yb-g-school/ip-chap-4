c = float(input("Enter the Cost Price: "))
s = float(input("Enter the Selling Price: "))

if(c<s):
    print("It's a profit of:", s-c,"!")
else:
    print("It's a loss of:", c-s,"!")
