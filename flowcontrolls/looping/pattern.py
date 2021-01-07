num=input("enter number") # "2"
i=1
data=0
pattern=""
while(i<=int(num)): #1<=2  2<=2 3<=2
    res=num*i#res="2"*1="2" "2"*2="22"

    pattern=pattern+"+"+res #+3+33+333+
    data+=int(res)#data=data+int(res) 0+2=2 2+int("22") 2+22=24

    i+=1#i=2 3
pattern=pattern.lstrip("+")#3+33+333+
print(pattern)
print("=",data)#24
#2 22