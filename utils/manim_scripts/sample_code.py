from manim import *

class GeneratedCode(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        # Plotting a parabola point by point
        points = []
        for x in np.arange(-5, 5, 0.1):
            y = x**2
            point = Dot([x, y, 0], color=RED)
            points.append(point)
            self.add(point)

        parabola = VGroup(*points)
        self.play(Create(parabola))

        self.wait()