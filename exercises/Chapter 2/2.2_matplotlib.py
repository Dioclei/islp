import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(3)

fig, ax = plt.subplots(figsize=(8,8))
x = rng.standard_normal(100)
y = rng.standard_normal(100)

# line plot
# ax.plot(x, y)

# scatter plot
# ax.plot(x, y, 'o')
ax.scatter(x, y, marker='o')

# title and axis
ax.set_xlabel("this is the x-axis")
ax.set_ylabel("this is the y-axis")
ax.set_title("Plot of X vs Y")

fig.set_size_inches(12, 3)
print(fig)

# 2 x 3 plot
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15,5))
axes[0, 1].plot(x, y, 'o')
axes[1, 2].scatter(x, y, marker='+')
# fig.savefig("Figure.pdf", dpi=200)
# fig.savefig("Figure.png", dpi=400)

axes[0,1].set_xlim([-1, 1])
# fig.savefig("Figure_updated.jpg")

# more sophisticated plotting
fig, ax = plt.subplots(figsize=(8, 8))
x = np.linspace(-np.pi, np.pi, 50)
y = x
f = np.multiply.outer(np.cos(y), 1 / (1 + x**2))
ax.contour(x, y, f)

fig, ax = plt.subplots(figsize=(8, 8))
ax.contour(x, y, f, levels=45)

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(f)

plt.show()