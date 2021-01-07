
num=int(input("enter number"))#9
flg=0
if num==1:
    print("not prime")
else:
    for i in range(2,num):#23

        if(num%i==0):#9%2==0 9%3==0
            flg=flg+1#flg=1
            break

        else:
            flg=0#=0

    if flg==0:
        print("prime")
    else:
        print("not prime")



#q1:
#low 5 upp=50 print all prime numbers between 5 to 50

#q2:
#read a num=3
#read low=3
#read upp=27
#1**3=1(3,27)
#2**3=8(3,27) 2
#3**3=27(3,27)
#1**2=1 (low,upp) 2**2=4(low,upp)2 3**2=9(4,30)=3 4**2=16(4,30)=4 5**2(4,30)5






