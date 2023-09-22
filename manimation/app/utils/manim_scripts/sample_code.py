from manim import *

class GeneratedCode(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        square = Square(fill_color=RED, fill_opacity=1)
        self.add(square)

        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)

        self.play(Rotate(square, 2 * PI, axis=OUT, run_time=2))

        self.wait()