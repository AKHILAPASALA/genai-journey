a=int(input("Enter a value: ")) #reading random input integer numbers
b=int(input("Enter b value: "))
print("The sum of a and b is {}".format(a+b)) #performed mathematical operation '+" and also used .format concept here to print the sum
print("product of a and b is {}".format(a*b))
print("the difference of a and b is {}".format(a-b))
print("The division of a and b is {}".format(a/b))
print("The modular division of a and b is {}".format(a%b))

print("Enter the names list: ",end=" ")
l=list(map(str, input().split(" ")))
print(l)

