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

    def show(self, frames=range(1, 6), interval=1, blit=True):
        ani = animation.FuncAnimation(self.fig, self.animate, frames=frames,
                                      interval=interval, blit=blit)
        plt.show()


class Heart02(Heart01):

    def show(self):
        super().show(blit=False)


class Heart03(Heart01):

    def __init__(self):
        super().__init__()
        self.eq = sympy.Eq(
            self.x**2 + (self.y - sympy.sqrt(sympy.Abs(self.x)))**2 - self.a, 0)


class Heart04(Heart03):

    def show(self):
        super().show(blit=False)


class Heart05(Heart01):

    def __init__(self):
        super().__init__()
        self.eq = sympy.Eq(self.x**2 + self.a*(sympy.Rational(3, 5)
                           * (self.x**2)**sympy.Rational(1, 3) - self.y)**2 - 1, 0)


class Heart06(Heart05):

    def show(self):
        super().show(blit=False)


class Heart07(Heart01):

    def __init__(self):
        super().__init__()
        self.eq = sympy.Eq(self.x**2 + 2*(sympy.Rational(3, 5) *
                           (self.x**2)**sympy.Rational(1, 3) - self.y)**2 - self.a, 0)


class Heart08(Heart07):

    def show(self):
        super().show(blit=False)


if __name__ == "__main__":
    heart01 = Heart01()
    heart01.show(interval=1)
    heart02 = Heart02()
    heart02.show(interval=1)

# TODO new heart shapes
# TODO readme
