#===============================================================================
# x = 3
# x = x*x
# print x
# n =  raw_input("Enter a number: ")
# print n
# 
# print("Enter a number: ")
# x = raw_input()
# y = int(x)
# if (y/2)*2 == y:
#     print "Even"
# else: print "Odd"
#===============================================================================
#===============================================================================
# text = str(raw_input("Type in text: "))
# number = int(raw_input("Type in number: "))
# print(text*number)
# 
# number = int(raw_input("Type in number: "))
# doubled = number * 2
# print(doubled)
#===============================================================================
x = int(raw_input("Enter a number: "))#find the square root for a perfect square.
ans = 0
if x >= 0:
    while ans * ans < x:
        ans = ans + 1
        #print ans
    if ans * ans !=x:
        print x, "is not a perfect square"
    else: 
        print ans, "is the square root!"
else: 
    print x,"is a negative number"
