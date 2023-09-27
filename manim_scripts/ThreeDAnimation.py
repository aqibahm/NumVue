from manim import *

class ThreeDAnimation(ThreeDScene):
    def construct(self):
        # Set the camera orientation
        self.set_camera_orientation(phi=45 * DEGREES, theta=45 * DEGREES)

        # Create a 3D cube
        cube = Cube(side_length=2, color=BLUE)

        # Create 3D axes
        axes = ThreeDAxes()

        # Add the cube and axes to the scene
        self.add(cube, axes)

        # Animate the cube (e.g., rotation)
        self.play(Rotate(cube, axis=OUT, radians=PI/2), run_time = 4)