from manim import *

class GeneratedCode(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        # Plotting the parabola point by point
        parabola = ParametricFunction(lambda t: [t, t**2, 0], t_range=[-2, 2], color=YELLOW)
        self.play(Create(parabola))

        # Adding coordinate labels
        axes.add_coordinates()

        self.wait()