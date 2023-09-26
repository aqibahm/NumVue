from manim import *

class GeneratedCode(ThreeDScene):
    def construct(self):
        # Set up the axes
        axes = ThreeDAxes()
        self.add(axes)

        # Add coordinate labels
        axes.add_coordinates()

        # Create the sun
        sun = Sphere(radius=1, color=YELLOW)
        self.add(sun)

        # Create the planet's elliptical path
        a = 3  # Semi-major axis
        b = 2  # Semi-minor axis
        t = np.linspace(0, 2 * PI, 100)
        x = a * np.cos(t)
        y = b * np.sin(t)
        z = np.zeros_like(t)
        path = ParametricFunction(lambda t: np.array([x[t], y[t], z[t]]), t_range=[0, len(t) - 1], color=BLUE)
        self.add(path)

        # Create the planet
        planet = Sphere(radius=0.5, color=GREEN)
        self.add(planet)

        # Animate the planet's movement
        self.play(Create(path))
        self.play(MoveAlongPath(planet, path), run_time=5)

        self.wait()