from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right triangle
        triangle = Polygon(ORIGIN, RIGHT * 3, UP * 4, fill_opacity=0.5)
        a_label = Text("a").next_to(triangle, RIGHT)
        b_label = Text("b").next_to(triangle, UP)
        c_label = Text("c").next_to(triangle.get_center(), UL, buff=0.2)

        # Display the triangle
        self.play(Create(triangle))
        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait(1)

        # Create a square using 4 copies of the triangle
        square = Square(side_length=7).move_to(triangle.get_corner(DL)).shift(DOWN + LEFT)
        triangles = [
            triangle.copy(),
            triangle.copy().rotate(PI/2).next_to(square, UP, buff=0),
            triangle.copy().rotate(PI).next_to(square, LEFT, buff=0),
            triangle.copy().rotate(3*PI/2).next_to(square, DOWN, buff=0)
        ]
        inner_square = Square(side_length=3*2**0.5).move_to(square.get_center())
        
        # Display the larger square formed by 4 triangles and a smaller square
        self.play(
            Create(square),
            *[Create(t) for t in triangles],
            Create(inner_square)
        )
        self.wait(2)

        # Highlight the areas
        area_c = SurroundingRectangle(inner_square, color=YELLOW)
        area_a = SurroundingRectangle(triangle, color=BLUE)
        area_b = SurroundingRectangle(triangles[1], color=RED)

        area_text = MathTex("c^2", "=", "a^2", "+", "b^2").scale(0.75).next_to(square, RIGHT, buff=1)
        self.play(Create(area_c))
        self.play(Write(area_text[0]))
        self.play(Create(area_a), Create(area_b))
        self.play(Write(area_text[2]), Write(area_text[3]), Write(area_text[4]))
        self.wait(2)

        # Conclusion
        self.play(FadeOut(area_c), FadeOut(area_a), FadeOut(area_b))
        conclusion = Text("Pythagorean Theorem Proved!").scale(0.75).next_to(area_text, DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)
