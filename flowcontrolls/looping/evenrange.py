limit=int(input("enter limit"))#
#print all even numbers bw low to  uplimit

i=1
while(i<=limit): #1<=5 2<=5 3<=5 4<=5 5<=5 6<=5
    # print(i) #1,2,3,4,5,6,7,8 we have to chk for each i is even for that
    if(i%2==0):#1%2==0 2%2==0 3%2==0 4%2==0 5%2==0
        print(i)#2 4
    i+=1#i=2 3 4 5 6
