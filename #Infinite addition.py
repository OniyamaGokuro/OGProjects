#Infinite addition

x = int(input ("Tell me a number: "))
list = []
list.append(x)

while x != 0:
    x = int (input ("Tell me a number: "))
    list.append (x)

if x ==0:
    sum= sum(list)
    print (sum)




