low=int(input("enter lowerlimit")) #5
upper=int(input("enter upperlimit"))#17

for num in range(low,(upper+1)):#num=5
    flg=0
    for i in range(2,num):
        if(num%i==0):
            flg=flg+1
            break
        else:
            flg=0
    if(flg==0):
        print(num)

