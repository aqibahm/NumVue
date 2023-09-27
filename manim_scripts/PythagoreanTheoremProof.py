from manim import *

class PythagoreanTheoremProof(Scene):
    def construct(self):
        # Create the triangle
        a = np.array([0, 0, 0])
        b = np.array([1, 0, 0])
        c = np.array([0, 1, 0])
        triangle = Polygon(a, b, c, color=BLACK)
        self.add(triangle)

        # Draw the square on the hypotenuse
        square = Polygon(c, c + np.array([1, 0, 0]), c + np.array([1, 1, 0]), c + np.array([0, 1, 0]), color=RED)
        self.add(square)

        # Draw the two squares on the legs
        square1 = Polygon(a, a + np.array([0, 1, 0]), a + np.array([1, 1, 0]), a + np.array([1, 0, 0]), color=BLUE)
        square2 = Polygon(b, b + np.array([0, 1, 0]), b + np.array([1, 1, 0]), b + np.array([1, 0, 0]), color=GREEN)
        self.add(square1, square2)

        # Animate the squares moving together
        self.play(
            square1.move_to(c),
            square2.move_to(c),
            square.scale(1 / 2),
            square.move_to(c / 2),
        )

        # Wait for a bit
        self.wait(1)

        # Remove the squares
        self.remove(square1, square2, square)

        # Draw the final triangle
        self.add(triangle)

        # Wait for a bit
        self.wait(1)