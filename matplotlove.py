import sympy
from sympy.plotting import plot, plot_implicit
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def mid_value(interval): return interval.mid


class Heart01:

    def __init__(self):
        self.x, self.y, self.a = sympy.symbols('x, y, a')
        self.eq = sympy.Eq((self.x**2 + self.y**2 - self.a)
                           ** 3 - self.x**2 * self.y**3, 0)
        self.fig, self.ax = self.plot_setup()

    def plot_setup(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.grid(False)
        ax.set_axis_off()
        return fig, ax

    def animate(self, constant):

        e = self.eq.subs({self.a: constant})
        p = plot_implicit(e, show=False)

        intervals = np.array(p[0].get_points()[0])
        px = tuple(map(mid_value, intervals[:, 0]))
        py = tuple(map(mid_value, intervals[:, 1]))
        points = np.array((px, py))

        heart = self.ax.scatter(*points)
        return heart,

    def show(self, frames=5, interval=10, blit=True):
        ani = animation.FuncAnimation(self.fig, self.animate, frames=frames,
                                      interval=interval, blit=blit)
        plt.show()


    e = heart_01.subs({a: constant})
    p = plot_implicit(e, show=False)

    intervals = np.array(p[0].get_points()[0])
    px = tuple(map(mid_value, intervals[:, 0]))
    py = tuple(map(mid_value, intervals[:, 1]))
    points = np.array((px, py))



ani = animation.FuncAnimation(fig, animate, frames=5, interval=10,
                              blit=True)
plt.show()
