from manim import *

class GeneratedCode(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        # Start with a 2-dimensional triangle
        triangle = Polygon(
            ORIGIN, RIGHT, UP,
            color=BLUE
        )
        self.add(triangle)

        self.wait()

        # Transform the triangle into a square
        square = Polygon(
            ORIGIN, RIGHT, RIGHT+UP, UP,
            color=GREEN
        )
        self.play(Transform(triangle, square))

        self.wait()

        # Transform the square into a pentagon
        pentagon = Polygon(
            ORIGIN, RIGHT, RIGHT+UP, LEFT+2*UP, LEFT+UP,
            color=YELLOW
        )
        self.play(Transform(square, pentagon))

        self.wait()

        # Transform the pentagon into a hexagon
        hexagon = Polygon(
            ORIGIN, RIGHT, RIGHT+UP, LEFT+UP, LEFT, LEFT+DOWN,
            color=RED
        )
        self.play(Transform(pentagon, hexagon))

        self.wait()

        # Transform the hexagon into a septagon
        septagon = Polygon(
            ORIGIN, RIGHT, RIGHT+UP, LEFT+UP, LEFT, LEFT+DOWN, RIGHT+DOWN,
            color=ORANGE
        )
        self.play(Transform(hexagon, septagon))

        self.wait()

        # Transform the septagon into an octagon
        octagon = Polygon(
            ORIGIN, RIGHT, RIGHT+UP, LEFT+UP, LEFT, LEFT+DOWN, RIGHT+DOWN, RIGHT,
            color=PURPLE
        )
        self.play(Transform(septagon, octagon))

        self.wait()

        # Iteratively increase the polygon number of sides until a circle is approximated
        circle = Circle(radius=1, color=PINK)
        self.play(Transform(octagon, circle))

        self.wait()

        self.play(FadeOut(octagon))

        self.wait()