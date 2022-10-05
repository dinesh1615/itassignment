from matplotlib import pyplot as plt
k={'dinesh':314,'laddu':400,'nani':430,'karthik':245}
l=list(k.keys())
m=list(k.values())
plt.figure(figsize=(30,30))
plt.pie(m,labels=l,autopct='%0.0f%%',shadow='true')
plt.show()
