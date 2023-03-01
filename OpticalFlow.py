import numpy as np
# from gradients import Gradient
from grads import Gradient

class Opticalflow:

    def calc(self, f1, f2, pt1, w):

        x, y = pt1.ravel()
        x = np.round(x).astype("int")
        y = np.round(y).astype("int")

        cropped_t1 = f1[(x-w):(x+w+1), (y-w):(y+w+1)]
        cropped_t2 = f2[(x-w):(x+w+1), (y-w):(y+w+1)]

        lucas_kanade = Gradient()
        changes_x = lucas_kanade.I_x(cropped_t1, 2*w)
        changes_y = lucas_kanade.I_y(cropped_t1, 2*w)
        changes_t = lucas_kanade.I_t(cropped_t1, cropped_t2, 2*w)

        flatten_x = changes_x.flatten()
        transpose_changes_x = np.array([flatten_x]).transpose()

        flatten_y = changes_y.flatten()
        transpose_changes_y = np.array([flatten_y]).transpose()

        flatten_t = changes_t.flatten()
        transpose_changes_t = np.array([flatten_t]).transpose()

        s_matrix = np.concatenate(np.array([transpose_changes_x, transpose_changes_y]), axis=1)
        s_matrix_transpose = s_matrix.transpose()
        t_matrix = transpose_changes_t
        st_s = np.matmul(s_matrix_transpose, s_matrix)
        st_s = st_s - 0.5*np.identity(st_s.shape[0])
        st_s_inv = np.linalg.inv(st_s)
        temp_matrix = np.matmul(st_s_inv, s_matrix_transpose)
        velocity_vector_arr = np.matmul(temp_matrix, t_matrix)

        u,v = -1*velocity_vector_arr.ravel()
        # print(u,v)
        pt2  = np.array([[x+u,y+v]], dtype=np.float32)

        return pt2
