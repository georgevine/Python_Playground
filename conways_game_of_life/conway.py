import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#use value to set color to represent 'on' cell state
ON = 255
#use calue to set color to represent 'off' cell state
OFF = 0
vals = [ON, OFF]

#return random grid of NxN values, either ON(20% probability) or OFF(%80 probability)
def randomGrid(N):
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)


#add glider to board with top left cell located at i, j
def addGlider(i, j, grid):
    glider = np.array([[0, 0, 255], [255, 0, 255], [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider

#grid-reference to the board array, N-side length of grid
def update(frameNum, img, grid, N):
    #create a copy of the grid so we can calculate new cell states first and then update all at once
    newGrid = grid.copy()
    #loop through all cells
    for i in range(N):
        for j in range(N):
            #compute 8-neighbor sum to determine next cell state
            # (neighbors wrap around board boundires)
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
            #apply game rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

            #update date
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

#main function
def main():
    #command line arguments are in sys.argv[1], sys.argv[2]....
    #parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation")
    #add args
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movFile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', dest='glider', required=False)
    parser.add_argument('--gosper', dest='store_true', required=False)
    args = parser.parse_args()

    #set grid size
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)

    #set animation update interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)

    #declare grid
    grid = np.array([])
    #check if glider desired
    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        addGlider(1, 1, grid)
    else:
        #populate grid with random cell states
        grid = randomGrid(N)


    #set up the animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
        frames = 10,
        interval = updateInterval,
        save_count = 50)


    #number of frames?
    #set output file
    if args.movFile:
        ani.save(args.movFile, fps = 30, extra_args=['-vcodec', 'libx264'])

    plt.show()


#call main
if __name__ == '__main__':
    main()
