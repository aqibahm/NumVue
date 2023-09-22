from manim import *

class CubeRotation(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES)

        axes = ThreeDAxes()
        cube = Cube()

        self.play(Create(axes), Create(cube))
        self.wait(1)

        self.play(Rotate(cube, angle=PI/2, axis=UP), run_time=1)
        self.wait(1)

        self.play(Rotate(cube, angle=PI/2, axis=RIGHT), run_time=1)
        self.wait(1)

        self.play(Rotate(cube, angle=PI/2, axis=OUT), run_time=1)
        self.wait(1)

        self.play(Rotate(cube, angle=PI/2, axis=UP), run_time=1)
        self.wait(1)

        self.play(Rotate(cube, angle=PI/2, axis=RIGHT), run_time=1)
        self.wait(1)

        self.play(Rotate(cube, angle=PI/2, axis=OUT), run_time=1)
        self.wait(1)

        self.play(Rotate(cube, angle=PI/2, axis=UP), run_time=1)
        self.wait(1)

        self.play(Rotate(cube, angle=PI/2, axis=RIGHT), run_time=1)
        self.wait(1)

        self.play(Rotate(cube, angle=PI/2, axis=OUT), run_time=1)
        self.wait(1)

        self.wait(2)  # Optional wait at the end

        self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES)  # Reset camera