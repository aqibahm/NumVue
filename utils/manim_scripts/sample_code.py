import numpy as np
from manim import *
config.max_files_cached = 1000
from manim import *
import numpy as np

config.max_files_cached = 1000

class GeneratedCode(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            tips=True,
            axis_config={'include_numbers': True},
            y_axis_config={}
        )
        self.add(axes)

        parabola = self.get_parabola()
        self.play(Create(parabola))

        self.wait()

    def get_parabola(self):
        points = np.array([
            [x, x**2, 0]
            for x in np.arange(-5, 5, 0.1)
        ])
        parabola = Line()
        parabola.set_points(points)
        return parabola

GeneratedCode().render()