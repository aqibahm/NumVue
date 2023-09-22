import manim
import numpy as np

class MandelbrotSet3D(manim.ThreeDScene):
    def construct(self):
        # Define the Mandelbrot fractal.
        def mandelbrot(c):
            z = 0
            for i in range(100):
                z = z ** 2 + c
                if abs(z) > 2:
                    return i
            return 0

        # Create a 3D grid of Mandelbrot fractal values.
        mandelbrot_grid = np.zeros((200, 200))
        for x in range(200):
            for y in range(200):
                c = complex(-2 + 2 * x / 200, -1.2 + 1.2 * y / 200)
                mandelbrot_grid[x, y] = mandelbrot(c)

        # Create a 3D surface from the Mandelbrot fractal values.
        mandelbrot_surface = manim.ThreeDObject(
            points=mandelbrot_grid,
            colors=manim.interpolate_color([1, 0, 0], [0, 0, 1], mandelbrot_grid),
            shape="surface",
        )

        # Add the Mandelbrot surface to the scene.
        self.add(mandelbrot_surface)

        # Rotate the Mandelbrot surface around the y-axis.
        self.play(manim.Rotate(mandelbrot_surface, axis=(0, 1, 0), angle=2 * np.pi, run_time=10))

        # Wait for the animation to finish.
        self.wait()