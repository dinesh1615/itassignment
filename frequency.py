import numpy as np
n=[]
l=int(input("enter the length of the array:"))
i=0
while(i<=l):
	x=int(input("enter the array numbers:"))
	n.append(x)
	i=i+1
arr=np.array(n)
print(arr)

count=1

for i in range(l):
	count=1
	for j in range(l):
			if(n[i]==n[j]):
				count=count+1
				
				
	
	print(n[i],"is",count,"times")
	
