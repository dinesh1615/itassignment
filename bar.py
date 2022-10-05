
from matplotlib import pyplot as plt
d1={'dinesh':8.81,'pavan':8.32,'pranav':9.8}
student=list(d1.keys())
marks=list(d1.values())
plt.bar(student,marks)
print(plt.show())
