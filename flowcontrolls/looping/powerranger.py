# 2
# low=4
# upper=30
num=int(input("enter number"))#3

low=int(input("enter lowerlimit"))#3
upper=int(input("enter upperlimit"))#28

for i in range(1,(upper+1)):# 1,28 ,=1
    res=i**num
    if(res>=low) &(res<=upper):
        print(i)
