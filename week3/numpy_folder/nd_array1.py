import numpy as np

array1 = np.zeros(3)
print(f'Array1 = {array1}')

array2 = np.zeros((1, 4))
print(f'Array2 = {array2}')

array3 = np.zeros((2, 5))
print(f'Array3 = {array3}')





array1 = np.full((2, 4), 5)
print(array1)
array2 = np.full((1,5), 10)
# Here array2 is still a ndarray
print(array2)