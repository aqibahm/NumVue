from manim import *

class GeneratedCode(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        # Parameters for the Gaussian distribution
        mu = 0
        sigma = 1

        # Generate the Gaussian curve
        x = np.linspace(-5, 5, 100)
        y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

        # Plot the Gaussian curve
        curve = axes.plot(x, y, color=BLUE)

        # Number of dots to generate
        num_dots = 100

        # Generate random x-coordinates for the dots
        x_coords = np.random.normal(mu, sigma, num_dots)

        # Generate the falling dots
        dots = VGroup()
        for x_coord in x_coords:
            dot = Dot(radius=0.05, color=RED)
            dot.move_to(axes.c2p(x_coord, 5, 0))  # Start the dots at the top of the scene
            dots.add(dot)

        # Animate the falling dots
        self.play(Create(curve))
        self.play(Create(dots))
        self.play(dots.animate.arrange(DOWN, buff=0.1).shift(UP * 5), run_time=3)

        self.wait()from manim import *
import numpy as np