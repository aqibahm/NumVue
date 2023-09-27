from manim import *

class CubeSidesAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        cube = Cube()
        self.play(Create(axes), Create(cube))

        for num_sides in range(3, 13):
            self.wait(1)

            # Update the shape with the desired number of sides
            shape = RegularPolygon(n=num_sides).scale(2)

            # Animate the camera orbiting around the origin
            self.play(self.camera.animate.rotate_about_z(2 * PI / 10), run_time=1)

            # Replace the shape with the updated one
            self.play(Transform(cube, shape), run_time=1)

        self.wait(1)
