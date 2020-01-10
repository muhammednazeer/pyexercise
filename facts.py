def factors(num):
    for i in range (1, num+1):
        if num % i == 0:
            print (i)

num = float(input("Enter your Number please: "))
if num > 0 and num.is_integer():
    factors(int(num))
else:
    print ("Please enter a positive integer")
