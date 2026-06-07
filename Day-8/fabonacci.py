def fab(a):
    if a==1:
        return 1
    elif a==0:
        return 0
    else:
        return fab(a-1)+fab(a-2)

for i in range(10):
    print(fab(i),end=" ")
