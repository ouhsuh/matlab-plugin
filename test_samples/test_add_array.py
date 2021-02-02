import add_array_by_binary
import matlab
import time
import numpy as np
import os
import scipy.io

n = 8000

time_start = time.time()
# creating even magic matrix

M = np.empty([n, n], dtype=float)
M[:, :n//2] = np.arange(1, n**2//2+1).reshape(-1, n).T
M[:, n//2:] = np.flipud(M[:, :n//2]) + (n**2//2)
M[1:n//2:2, :] = np.fliplr(M[1:n//2:2, :])
M[n//2::2, :] = np.fliplr(M[n//2::2, :])

time_py_gen_magic = time.time()

time_before_save_mat = time.time()

large_array = M.tofile('temp.bin',sep="", format='float64')

time_after_save_mat = time.time()

file_path = os.getcwd().__add__('/temp.bin')


# initial matlab function
my_mat_fun = add_array_by_binary.initialize()
time_mat_init = time.time()

# pass large array to matlab and process (add all elements)
array_size, matlab_process_time, res = my_mat_fun.add_array_by_binary(file_path,n,n,nargout=3)

print(res)
time_end = time.time()

# print the results
print("Matrix size is:",array_size,"Mb",",dimesntion:",n,"x",n)
print("Time of python generating magic matrix:",time_py_gen_magic - time_start,"s")
print("Matlab Funtion Initialization time:",time_mat_init - time_py_gen_magic,"s")
print("Matlab process time:",matlab_process_time,"s")
print("Python-to-Matlab communication time:",time_end - time_mat_init - matlab_process_time,"s")
print("Total time:",time_end - time_start,"s")
print("Time to save mat:",time_after_save_mat - time_before_save_mat,"s")






