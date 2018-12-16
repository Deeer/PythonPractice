import matplotlib.pyplot as plt 


x_values = list(range(1,1001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values,  y_values,c= y_values,cmap=plt.cm.Blues ,edgecolors='none' , s=40)
plt.title('Square Numsers', fontsize=24)
plt.xlabel("Value", fontsize = 12)
plt.ylabel("Square of Value", fontsize = 12)

plt.tick_params(axis='both', which="major",labelsize=12)

# plt.savefig('squres_plot.png',bbox_inches='tight')
plt.show()


