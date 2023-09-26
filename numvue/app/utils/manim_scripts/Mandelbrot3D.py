import numpy as np
import matplotlib.pyplot as plt
from manim import *

class Mandelbrot3D(ThreeDScene):
    def construct(self):
        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Create a 3D plot of the Mandelbrot set
        mandelbrot_plot = self.create_mandelbrot_plot()

        # Display the 3D plot
        self.play(ShowCreation(mandelbrot_plot))
        self.wait(4)

    def create_mandelbrot_plot(self):
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection='3d')

        x = np.linspace(-2, 2, 800)
        y = np.linspace(-2, 2, 800)
        X, Y = np.meshgrid(x, y)
        Z = self.mandelbrot(X, Y)

        ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none')
        ax.set_axis_off()

        return plt_to_tikz_image(fig, scale=0.2)

    def mandelbrot(self, x, y, max_iterations=100):
        c = complex(x, y)
        z = 0
        for i in range(max_iterations):
            z = z * z + c
            if abs(z) > 2:
                return i / max_iterations
        return 0
