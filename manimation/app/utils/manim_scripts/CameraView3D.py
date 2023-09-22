from manim import *

class CameraView3D(Scene):
    def construct(self):
        # Create a 3D unit circle
        unit_circle = Circle(radius=1, color=WHITE, fill_opacity=0.2)
        self.add(unit_circle)

        # Define camera positions
        camera_positions = [
            [0, 0, 1],  # Front
            [0, 0, -1],  # Back
            [1, 0, 0],  # Right
            [-1, 0, 0],  # Left
            [0, 1, 0],  # Up
            [0, -1, 0]  # Down
        ]

        for position in camera_positions:
            # Set the camera's orientation
            self.renderer.camera.set_rotation_matrix(np.eye(3))
            self.renderer.camera.set_position(position)

            # Create a random polygon within the scene
            num_sides = np.random.randint(3, 7)  # Random number of sides (3 to 6)
            polygon = RegularPolygon(n=num_sides, radius=0.5, color=BLUE, fill_opacity=0.5)
            self.add(polygon)

            # Stay on each direction for 1 second
            self.wait(1)

            # Remove the polygon before changing the camera view
            self.remove(polygon)