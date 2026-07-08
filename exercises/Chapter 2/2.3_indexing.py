import numpy as np

seq1 = np.linspace(0, 10, 11)
print(seq1)
seq1_a = np.linspace(0, 10, 13)
print(seq1_a)

seq2 = np.arange(0, 10)
print(seq2)
seq2_a = np.arange(0, 10, 1.1)
print(seq2_a)

A = np.array(np.arange(16)).reshape((4, 4))
print(A)

# selecting values, rows, and cols
print(A[1, 2])
print(A[[1, 3]])
print(A[:, [0, 2]])

# selecting a submatrix
print(A[[1, 3], [0, 2]]) # only selects (1,0) and (3,2)
print(A[[1, 3]][:, [0,2]]) # able to select submatrix of rows (1, 3), cols (0, 2)
print(A[1:4:2, 0:3:2]) # does the same thing with python slices

# boolean indexing
print("Boolean Indexing:")
keep_rows = np.zeros(A.shape[0], bool)
print(keep_rows)
keep_rows[[1, 3]] = True
print(keep_rows)
print(np.all(keep_rows == np.array([0, 1, 0, 1]))) # boolean arr is equivalent to 0/1 integers

print(A[keep_rows])

keep_cols = np.zeros(A.shape[1], bool)
keep_cols[[0, 2, 3]] = True
idx_bool = np.ix_(keep_rows, keep_cols) # create a mesh containing rows (1, 3) and cols (0, 2, 3)
print(A[idx_bool])
idx_mixed = np.ix_([1, 3], keep_cols) # create the same mesh, but mix array and np array
print(A[idx_mixed])

