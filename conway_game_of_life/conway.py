import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


x = np.array([[0, 0, 255], [255, 255, 0], [0, 255, 0]])
plt.imshow(x, interpolation='nearest')
plt.show()


print np.random.choice([0, 255], 4*4, p=[0.1, 0.9]).reshape(4,4)



#add a glider pattern to the simulation with the top left at the cell at i,j
def addGlider(i, j, grid):
    glider = np.array([[0, 0, 255], [255, 0, 255], [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider
