import matplotlib.pyplot as plt
import csv
from random_walker import RandomWalk 

while True: 
      rw = RandomWalk(50000)
      rw.fill_walk()
      plt.figure(dpi = 128,figsize=(10,6))
      pointe_numbers = list(range(rw.num_pointers))
      plt.scatter(rw.x_values, rw.y_values,c=pointe_numbers,cmap=plt.cm.Blues,edgecolors='none', s=1)
      plt.scatter(0,0,c='green',edgecolors='none',s=100)
      plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none', s=100)
      

      plt.axes().get_xaxis().set_visible(False)
      plt.axes().get_yaxis().set_visible(False)
      plt.show()

      keep_running = input("make another walk?(y/n): ")
      if keep_running == 'n':
          break