num=int(input("enter num")) #123
res=""
while(num>0):#123>0 12>0
    digit=num%10#digit=123%10=3 12%10=2
    # res=res*10+digit #0*10+3=3 3*10+2=32
    res=res+str(digit)
    num=num//10#123//10=12
print("res=",res)
# multiply with 10 +digit


#123
#1*1*1+2*2*2+3*3*3=1+8+27=36




