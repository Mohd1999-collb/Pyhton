import numpy as np 
import statistics as stats

l1 = (2, 3, 5, 1)
l2 = [4, 8, 65, 9]

matrix1 = [
           [ 10,  40,  90],
           [ 40, 100, 180],
           [ 70, 348, 270]
        ]

matrix2 = [
            [ 11,  44,  99],
            [ 5, 10, 80],
            [ 7, 1, 20]
        ]

arr1 = np.array(l1) # Converts a list (or other iterable) to a NumPy array
arr2 = np.array(l2)
mat1 = np.array(matrix1)
mat2 = np.array(matrix2)

# Common array method or operation

# Slicing of matrix from row one to index 0 to 1
slice_array = mat1[1, 0:2]

# Give the dimension of the matrix in form of (row, column)
dim = np.shape(mat1)

# Give the total number of element in the matrix
element_count = np.size(mat1)

# Give the dimension of the matrix
dimension = np.ndim(mat1)

# Give the data type of the array
arrType = mat1.dtype;

# Convert the matrix data type from integer  to float
convert_data_type = mat1.astype(float)

# Concatenate matrix if axis = 0 thats means concatenate the matrix vertically and axis = 1 means concatenate the matrix horizontally
concat_matrix = np.concatenate((mat1, mat2), axis=1)

# Append the value at the last
app_matrix = np.append(mat1, 60)

# Inset the value at given index
insert_matrix = np.insert(mat1, 1, 2000,axis=1)

# Delete the element at given index
delete_matrix = np.delete(insert_matrix, 2, axis=1)

# Sort the matrix
arr = np.sort(mat1)

# Search the element in the matrix
index = np.where(mat1 == 10)  # Returns the indices of elements equal to 5

# Compute the comulutive sum
cum_sum = np.cumsum(mat1, axis=1)  # Compute the cumulative sum along the specified axis

# Compute the comulutive product
cum_prod = np.cumprod(mat1, axis=1)  # Compute the cumulative prod along the specified axis

# 1. Array Creation Methods ------
print(type(arr1))

# Creates an array filled with zeros
zeroArr = np.zeros((2, 3)) # 2 rows, 3 columns of zeros

# Creates an array filled with ones
onesArr = np.ones((2, 3)) # 2 rows, 3 columns of zeros

# Creates an identity matrix.
identityMat = np.eye(3)  # 3x3 identity matrix

# Creates a sequence of evenly spaced numbers over a specified interval
lSpace = np.linspace(0, 10, 5)  # 5 evenly spaced values between 0 and 10

# Creates an array with regularly spaced values.
spaceArr = np.arange(0, 12, 2)  # array: [0, 2, 4, 6, 8]

# 2. Array Shape Methods:--------------------

# Reshapes an array to a new dimension
reshapeArr = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)  # Reshape to 2x3 matrix

# Transposes the array (i.e., swaps rows and columns).
originalArr = np.array([[1, 2], [3, 4]])
tarnsposeArr = originalArr.transpose()  # Output: [[1, 3], [2, 4]]

# 3. Array Math Operations:--------------------

# Adds arrays element-wise
addArr = np.add([1, 2], [3, 4])  # Output: [4, 6]

# Subtracts arrays element-wise
subArr = np.subtract([5, 6], [2, 1])  # Output: [3, 5]

# Multiplies arrays element-wise
mulArr = np.multiply([[1, 2], [3, 4]], [[2, 5], [3, 4]])  # Output: [3, 8]

#  Computes the dot product of two arrays
dotProArr = np.dot([1, 2], [3, 4])  # Output: 11 (1*3 + 2*4)

#  Divides arrays element-wise.
divideArr = np.divide([6, 8], [2, 4])  # Output: [3.0, 2.0]

# Raises each element to a specified power
powerArr = np.power([2, 3], 2)  # Output: [4, 9]

# 4. Statistical Methods:
# Calculates the mean (average) of the elements
m_arr = np.array([1, 2, 3])
mean_value = np.mean(m_arr)  # Output: 2.0

# Calculates the median of the elements
median_value = np.median(m_arr)  # Output: 2
# Computes the mode of the elements
mode_value = stats.mode([1, 2, 2, 3, 3])  # Output: ModeResult(mode=[2], count=[3])

# Computes the sum of array elements
total = np.sum([1, 2, 3, 4])  # Output: 10

# Returns the minimum and maximum values
min_value = np.min([1, 2, 3, 4])  # Output: 1
max_value = np.max([1, 2, 3, 4])  # Output: 3

# Calculates the standard deviation
std_dev = np.std([1, 2, 3])  # Output: 0.816

# Calculates the variance
variance = np.var([1, 2, 3])
# 5. Indexing and Slicing:------------------
# Array Indexing:
indexArr = np.array([1, 2, 3, 4, 5])
element = indexArr[2]  # Output: 3

# Array Slicing
SliceArr = np.array([1, 20, 32, 40, 56])
slice_arr = SliceArr[1:4]  # Output: [20, 32, 40]

# 6. Concatenation and Splitting:

arr1 = np.array([[1, 2], [13, 44]])
arr2 = np.array([[3, 4], [4, 5]])
# axis = 1 --> concatenation of array columns wise and axis = 0 --> concatenation of rows wise(default)
combined = np.concatenate((arr1, arr2), axis=1)

# Splits an array into multiple sub-arrays.
arr = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.split(arr, 3)  # Output: [array([1, 2]), array([3, 4]), array([5, 6])]

# 7. Sorting :--------------------------------------

# Sorts the elements of an array
arr = np.array([3, 1, 2])
sorted_arr = np.sort(arr)  # Output: [1, 2, 3]

# 8. Other Useful Methods: -------------------------

# Finds the unique elements of an array
arr = np.array([1, 2, 2, 3])
unique_values = np.unique(arr)  # Output: [1, 2, 3]

# Returns the index of the maximum value.
arr = np.array([1, 3, 8])
max_index = np.argmax(arr)  # Output: 2

# Returns the index of the minimum value
min_index = np.argmin(arr)  # Output: 0

# 9. Advanced Indexing & Boolean Masking: --------------

# Select elements based on a condition
arr = np.array([1, 2, 3, 4, 5, 12])
condition = arr > 3
filtered_arr = arr[condition]

# Use arrays as indices to extract multiple elements.
arr = np.array([10, 20, 30, 40, 50])
indices = [1, 3]
selected_elements = arr[indices]  # Output: [20, 40]

# 10. Broadcasting

# Broadcasting allows NumPy to perform operations on arrays of different shapes.
arr = np.array([1, 2, 3])
arr_broadcast = arr + 10  # Output: [11, 12, 13]

# Element-wise operations on mismatched dimensions.
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])
result = arr1 + arr2  # Broadcasts arr2 to match arr1

# 11. Mathematical Functions:------------------------------

# np.sin(), np.cos(), np.tan(): Apply trigonometric functions.
arr = np.array([0, np.pi/2, np.pi])
sine_values = np.sin(arr)  # Output: [0.0, 1.0, 0.0]

# Computes the exponential (e^x) of all elements in the array.
arr = np.array([1, 2, 3])
exp_values = np.exp(arr)  # Output: [2.71828183, 7.3890561 , 20.08553692]

# Computes the natural logarithm of all elements.
arr = np.array([1, np.e, np.e**2])
log_values = np.log(arr)  # Output: [0.0, 1.0, 2.0]

# Computes the square root of all elements.
arr = np.array([1, 4, 9])
sqrt_values = np.sqrt(arr)  # Output: [1.0, 2.0, 3.0]

# 12. Random Functions: ---------------------------

# Creates an array of the given shape with random values from a uniform distribution over [0, 1).
random_array = np.random.rand(3, 3)

# Generates random integers within a given range.
random_integers = np.random.randint(0, 10, (3, 3))  # Random integers between 0 and 9

# Returns a sample (or samples) from a normal (Gaussian) distribution.
normal_values = np.random.normal(loc=0, scale=1, size=10)  # Mean 0, Std. deviation 1

# 13. Linear Algebra Methods: ------------------------

# Computes the inverse of a square matrix.
matrix = np.array([[1, 2], [3, 4]])
inverse_matrix = np.linalg.inv(matrix)

# Computes the determinant of a matrix.
matrix = np.array([[1, 2], [3, 4]])
determinant = np.linalg.det(matrix)  # Output: -2.0

# Computes the dot product of two arrays (or matrices).
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
dot_product = np.dot(arr1, arr2)

# Computes the eigenvalues and eigenvectors of a matrix.
matrix = np.array([[1, 2], [2, 1]])
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# 14. Flattening and Reshaping:------------------------------

# Converts a multi-dimensional array into a 1D array.
arr = np.array([[1, 2], [3, 4]])
flat_arr = arr.flatten()  # Output: [1, 2, 3, 4]

# Returns a flattened 1D array but tries to avoid copying the data when possible.
arr = np.array([[1, 2], [3, 4]])
ravel_arr = arr.ravel()  # Output: [1, 2, 3, 4]

# Reshapes an array without changing its data.
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)  # Output: [[1, 2, 3], [4, 5, 6]]

# 15. Where Function: --------------------------------------

#  Returns the indices of elements that meet a condition.
arr = np.array([10, 20, 30, 40])
result = np.where(arr > 20)  # Output: (array([2, 3]),)

# It can also be used to replace values based on a condition.
arr = np.array([10, 20, 30, 40])
replaced = np.where(arr > 20, arr, -1)  # Output: [-1, -1, 30, 40]

# 16. Stacking and Splitting Arrays: ------------------------

# Stacks arrays vertically (row-wise).
arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
vstacked = np.vstack((arr1, arr2))  # Output: [[1, 2], [3, 4]]

# Stacks arrays horizontally (column-wise).
hstacked = np.hstack((arr1, arr2))  # Output: [1, 2, 3, 4]

# Splits an array into multiple sub-arrays.
arr = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.split(arr, 3)  # Output: [array([1, 2]), array([3, 4]), array([5, 6])]

# 17. NaN and Infinite Values Handling:------------------------------------

# Detects NaN (Not a Number) values.
arr = np.array([1, np.nan, 3])
isnan_result = np.isnan(arr)  # Output: [False, True, False]

# Detects infinite values.
arr = np.array([1, np.inf, 3])
isinf_result = np.isinf(arr)  # Output: [False, True, False]

#  Replaces NaNs with a specified number (usually 0).
arr = np.array([1, np.nan, 3])
replaced_arr = np.nan_to_num(arr)  # Output: [1.0, 0.0, 3.0]

# 18. Saving and Loading Arrays:

#  Saves an array to a .npy file.
arr = np.array([1, 2, 3])
# np.save('my_array.npy', arr)

# Loads an array from a .npy file.
# loaded_arr = np.load('my_array.npy')

# Saves an array to a text file.
# np.savetxt('my_array.txt', arr)

# Loads an array from a text file.
# arr_from_txt = np.loadtxt('my_array.txt')
print(replaced_arr)
