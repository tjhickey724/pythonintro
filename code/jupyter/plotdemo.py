from matplotlib import pyplot as plt

xs = list(range(-10,11))
ys = [x*x for x in xs]
plt.plot(xs,ys,label="y = x^2")
plt.grid()
plt.title("parabola y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.show()