#(&,|,^)
print(True&True)#True
print(True&False)#False
print(True&True&False)#false
#rule of & if is one End is False Entire Term is become False
print(True|False)#true
print(True|True)#True
#rule of \ if is one End is True Entire Term is become True
print(True ^ True)#false
print(False ^ False)#false
print(True ^ False)#True

#rule of ^ if both end are same bit itwill return False 0
#rule of ^ if both end are different bit itwill return True 1

print(2^4)
#0010
#0100
#====
#0110=>6