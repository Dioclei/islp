import numpy as np

x = np.array([3, 4, 5])
y = np.array([4, 9, 7])

print(x + y)

z = np.array([
    [1, 2, 3],
    [3, 4, 5]
])

print(z)
print(f"ndim: {z.ndim}")
print(f"dtype of z: {z.dtype}")

z_float = np.array(z, float)
print(f"dtype of z_float: {z_float.dtype}")

print(f"shape: {z.shape}")

a = np.array([1, 2, 3, 4])
print(a.sum())
print(np.sum(a))

b = np.array([1, 2, 3, 4, 5, 6])
b_reshape = b.reshape((2, 3))
print("before reshape:")
print(b)
print(b_reshape)
print(b_reshape[0,0])
print(b_reshape[1,2])

b_reshape[0,0] = 5
print("after reshape:")
print(b)
print(b_reshape)
print(b_reshape[0,0])
print(b_reshape[1,2])
# note that modifying b_reshape also modifies b: 
# - the .reshape method does not create a new object
# - the values occupy the same memory space

print("some operations on arrays:")
print(np.sqrt(b))
print(b**2)
print(b**0.5)

# Generating random data
print("generating random data:")
x = np.random.normal(size=50) # N(0,1), 50 values
print(x)
y = x + np.random.normal(loc=50, scale=1, size=50)
print(y)
print(np.corrcoef(x, y))

# Using a seed to ensure results are replicable
print("using a seed:")
rng = np.random.default_rng(1303)
print(rng.normal(scale=5, size=2))
rng2 = np.random.default_rng(1303)
print(rng2.normal(scale=5, size=2))
print(rng2.normal(scale=5, size=2))

# Computing mean, variance, std dev
print("mean, variance and std dev:")
rng = np.random.default_rng(3)
y = rng.standard_normal(10)
# mean
print(np.mean(y))
print(y.mean())
# variance
print(np.var(y))
print(y.var())
print(np.mean((y - y.mean())**2))
# std dev
print(np.sqrt(np.var(y)))
print(np.std(y))
# we can also do matrices of random values
X = rng.standard_normal((10, 3))
print(X)
print(X.mean(axis=0))
print(X.mean(0))
