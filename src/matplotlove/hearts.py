import sympy
from sympy.plotting import plot_implicit
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


class Heart3d01:

    def __init__(self):
        self.fig, self.ax = self.plot_setup()

    def plot_setup(self):
        fig = plt.figure(figsize=(8, 8))
        fig.tight_layout(pad=0)
        ax = fig.add_subplot(111, projection='3d')
        return fig, ax

    def plot_implicit(self, fn, bbox=(-2.5, 2.5), resolution=100, slices=30,
                      colormap=plt.cm.Reds):
        """Create a plot of an implicit function fn
        Adapted from https://stackoverflow.com/a/4687582/8706250

        Parameters
        ----------
        fn : function
            implicit funcion with fn == 0
        bbox : tuple, optional
            x, y, z limits, by default (-2.5, 2.5)
        resolution : int, optional
            number of points, by default 100
        slices : int, optional
            number of countour planes, by default 30
        colormap : _type_, optional
            Matplotlib colormap to be used, by default plt.cm.Reds
        """

        xmin, xmax, ymin, ymax, zmin, zmax = bbox * 3
        A = np.linspace(xmin, xmax, resolution)
        B = np.linspace(xmin, xmax, slices)
        A1, A2 = np.meshgrid(A, A)
        colors = [colormap(i) for i in np.linspace(0.0, 1.0, slices)]

        for z, color in zip(B, colors):  # plot contours in the XY plane
            X, Y = A1, A2
            Z = fn(X, Y, z)
            self.ax.contour(X, Y, Z+z, [z], zdir='z',
                            colors=np.array(color).reshape(-1, 4))

        for y, color in zip(B, colors):  # plot contours in the XZ plane
            X, Z = A1, A2
            Y = fn(X, y, Z)
            self.ax.contour(X, Y+y, Z, [y], zdir='y',
                            colors=np.array(color).reshape(-1, 4))

        for x, color in zip(B, colors):  # plot contours in the YZ plane
            Y, Z = A1, A2
            X = fn(x, Y, Z)
            self.ax.contour(X+x, Y, Z, [x], zdir='x',
                            colors=np.array(color).reshape(-1, 4))

        self.ax.set_zlim3d(zmin, zmax)
        self.ax.set_xlim3d(xmin, xmax)
        self.ax.set_ylim3d(ymin, ymax)
        self.ax.grid(False)
        self.ax.set_axis_off()

    @staticmethod
    def heart3D(x, y, z, n=0):
        return (x**2 + (9/4) * y**2 + z**2 - 1)**3 - x**2 * z**3 - (9/80) * y**2 * z**3 < n

    def animate(self, i):
        self.ax.view_init(elev=30, azim=3.6*i)
        return self.fig,

    def show(self):
        self.plot_implicit(self.heart3D, bbox=(-1.3, 1.3),
                           colormap=plt.cm.PuRd, slices=50)
        ani = animation.FuncAnimation(self.fig, self.animate,
                                      frames=100, interval=10, blit=False)

        plt.tight_layout()
        plt.show()


class Heart3d02(Heart3d01):

    def __init__(self):
        super().__init__()
        self.ax.view_init(elev=30, azim=90)

    def animate(self, i):
        self.ax.dist = i
        return self.fig,

    def show(self):
        self.plot_implicit(self.heart3D, bbox=(-1.3, 1.3),
                           colormap=plt.cm.PuRd, slices=50)
        ani = animation.FuncAnimation(self.fig, self.animate, frames=(10, 20),
                                      interval=300, blit=False)

        plt.tight_layout()
        plt.show()
