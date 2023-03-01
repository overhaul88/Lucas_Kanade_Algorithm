import numpy as np
from OpticalFlow import Opticalflow

OF = Opticalflow()

# Here we are tracking the specific pixel with value 99. 
# In first frame it is located at 2,2. The second frame is shifted by 1 unit left.
# Thus the new location of this pixel must be 2,1.

f1 = np.array([[0.0, 1.0, 2.0, 4.0, 6.0],
                [1.0, 2.0, 4.0, 8.0, 16.0],
                [2.0, 4.0, 99.0, 12.0, 16.0,],
                [4.0, 8.0, 16.0, 32.0, 64.0],
                [8.0, 16.0, 32.0, 48.0, 64.0]])

f2 = np.array([[1.0, 2.0, 4.0, 6.0, 8.0],
                [2.0, 4.0, 8.0, 16.0,32.0],
                [4.0, 99.0, 12.0, 16.0, 20.0],
                [8.0, 16.0, 32.0, 64.0, 128.0],
                [16.0, 32.0, 48.0, 64.0, 80.0]])

x=2
y=2
w=2


print("Object to be tracked: ", f1[x][y])
print("Initial position: ",(x,y))

pt1 = np.array([[x,y]])
pt2 = OF.calc(f1,f2,pt1,w)
x,y = pt2.ravel()
x = np.round(x).astype("int")
y = np.round(y).astype("int")

print("Final position: ",(x,y)) 