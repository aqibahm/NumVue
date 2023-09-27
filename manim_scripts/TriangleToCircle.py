from manim import *

class TriangleToCircle(Scene):
    def construct(self):
        # Create the initial triangle
        triangle = RegularPolygon(n=3, start_angle=PI / 6, color=BLUE, fill_opacity=0.5)
        self.play(Create(triangle.scale(3)))
        self.wait(1)

        # Increase the number of sides to approximate a square
        for n in range(4, 31):
            if n % 2 == 1:
                color = BLUE
            else:
                color = RED
            new_polygon = RegularPolygon(n=n, start_angle=PI / 6, color= color, fill_opacity=0.5).scale(3)
            new_polygon.replace(triangle)
            self.play(Transform(triangle, new_polygon))

        # Wait for a few more seconds at the end
        self.wait(3)