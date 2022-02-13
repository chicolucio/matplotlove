import sympy
from sympy.plotting import plot, plot_implicit
import matplotlib.pyplot as plt
import numpy as np

x, y, t, a, b = sympy.symbols('x, y, t, a, b')

heart_01 = sympy.Eq((x**2 + y**2 - a)**3 - x**2 * y**3, 0)
heart_01

mid_value = lambda interval: interval.mid
plots_heart_01 = []

for constant in range(1, 6):
    e = heart_01.subs({a: constant})
    p = plot_implicit(e, show=False)

    intervals = np.array(p[0].get_points()[0])
    px = tuple(map(mid_value, intervals[:, 0]))
    py = tuple(map(mid_value, intervals[:, 1]))
    points = np.array((px, py))
    plots_heart_01.append(points)

fig, ax = plt.subplots()

for i, p in enumerate(plots_heart_01, 1):
    ax.scatter(*p, label=f'a = {i}')
    # ax.set_ylim(0, 10)
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')

plt.show()
