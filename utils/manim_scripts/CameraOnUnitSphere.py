from manim import *
import numpy as np
import random

class CameraOnUnitSphere(Scene):
    def construct(self):
        # Create a 3D unit sphere
        sphere = Sphere(radius=1, color=BLUE, fill_opacity=0.2)

        # Create random polygons for each direction
        polygons = []
        for _ in range(4):
            n_sides = random.randint(3, 7)  # Random number of sides
            radius = random.uniform(0.2, 0.5)  # Random radius
            polygon = RegularPolygon(n=n_sides, radius=radius, color=GREEN, fill_opacity=0.5)
            polygons.append(polygon)

        # Set camera orientation and positions
        self.set_camera_orientation(phi=PI/2, theta=0)
        self.add(sphere)  # Add the sphere to the scene

        # Rotate the camera to different directions
        directions = [(0, 0), (PI, 0)]  # Front and back
        for direction in directions:
            self.begin_3d_rotation_vector(*direction, rate=1)
            self.wait(1)

            # Add and animate random polygons
            for polygon in polygons:
                polygon.move_to(OUT)
                self.play(Create(polygon), run_time=1)
                self.wait(1)

            # Remove the polygons
            self.play(*[FadeOut(polygon) for polygon in polygons])
            self.wait(1)

        self.stop_3d_rotation()  # Stop camera rotation