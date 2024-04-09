#Fibonacci

n =int(input("What number are you looking for?"))
x = 0
y = 1
for i in range (1,n):
    print(f"{i}:{x}")
    x = x + y  
    y = x - y
    i+=1
    if i == n:
        print(i,x)
        break

