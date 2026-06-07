def fact(a):
    if a==1 or a==0:
        return 1
    else:
        return a*fact(a-1)
    
print("The factorial of 4 is:",fact(4))

