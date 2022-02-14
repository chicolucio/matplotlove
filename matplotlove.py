import sympy
from sympy.plotting import plot, plot_implicit
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

x, y, t, a, b = sympy.symbols('x, y, t, a, b')

heart_01 = sympy.Eq((x**2 + y**2 - a)**3 - x**2 * y**3, 0)


def mid_value(interval): return interval.mid


fig, ax = plt.subplots(figsize=(8, 8))
ax.grid(False)
ax.set_axis_off()


def animate(constant):

    e = heart_01.subs({a: constant})
    p = plot_implicit(e, show=False)

    intervals = np.array(p[0].get_points()[0])
    px = tuple(map(mid_value, intervals[:, 0]))
    py = tuple(map(mid_value, intervals[:, 1]))
    points = np.array((px, py))

    heart = ax.scatter(*points)
    return heart,


ani = animation.FuncAnimation(fig, animate, frames=5, interval=10,
                              blit=True)
plt.show()
