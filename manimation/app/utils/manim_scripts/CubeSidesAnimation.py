from manim import *

class CubeSidesAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        cube = Cube()
        self.play(Create(axes), Create(cube))

        for num_sides in range(7, 13):
            self.wait(1)

            # Update the shape with the desired number of sides
            shape = RegularPolygon(n=num_sides, radius=1.5, stroke_width=0.1).rotate(PI / num_sides, axis=OUT)
            modified_cube = self.convert_cube_to_shape(cube, shape)

            # Animate the camera orbiting around the origin
            self.set_camera_orientation(
                phi=75 * DEGREES, theta=(-45 + 2 * PI * num_sides / 10) * DEGREES
            )

            # Replace the shape with the updated one
            self.play(Transform(cube, modified_cube), run_time=1)

        self.wait(1)

    def convert_cube_to_shape(self, cube, shape):
        modified_cube = VGroup()
        for face in cube.split():
            modified_face = shape.copy()
            modified_face.match_face(face)
            modified_cube.add(modified_face)
        return modified_cube