from manim import *

class GeneratedCode(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        parabola = ParametricFunction(
            lambda t: np.array([
                t,
                t**2,
                0
            ]),
            t_range=np.linspace(-2, 2, 100),
            color=YELLOW
        )

        self.add(parabola)

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(2)