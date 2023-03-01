import numpy as np

class Gradient:

    def I_x(self,grid,w):
        return grid[1:w+1,:w] - grid[:w, :w]

    def I_y(self,grid,w):
        return grid[:w,1:w+1] - grid[:w, :w]

    def I_t(self,grid1, grid2, w):
        return grid2[:w,:w]-grid1[:w,:w]
