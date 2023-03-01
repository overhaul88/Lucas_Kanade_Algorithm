import numpy as np

class Gradient:

    def I_x(self,grid,w):
        output = np.zeros((w,w))

        for i in range(w):
            for j in range(w):
                output[i][j] = grid[i][j+1]-grid[i][j]

        return output

    def I_y(self,grid,w):
        output = np.zeros((w,w))

        for i in range(w):
            for j in range(w):
                output[i][j] = grid[i+1][j]-grid[i][j]

        output = np.zeros((w,w))

        return output

    def I_t(self,grid1, grid2, w):
        output = np.zeros((w,w))

        for i in range(w):
            for j in range(w):
                output[i][j] = grid2[i][j]-grid1[i][j]
        return output