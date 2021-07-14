def bubble(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print(a)
bubble([8,5,3,2,7,1])


