from manim import *

class VisualizeAxioms(Scene):
    def construct(self):
        self.axiom1()
        self.axiom2()
        self.axiom3()

    def axiom1(self):
        line = Line(ORIGIN, RIGHT)
        self.play(Create(line))
        self.wait(1)
        self.play(FadeOut(line))
        self.wait(1)

    def axiom2(self):
        point1 = Dot()
        point2 = Dot().shift(RIGHT)
        line = Line(point1.get_center(), point2.get_center())
        self.play(Create(point1), Create(point2))
        self.play(Create(line))
        self.wait(1)
        self.play(FadeOut(point1), FadeOut(point2), FadeOut(line))
        self.wait(1)

    def axiom3(self):
        point1 = Dot()
        point2 = Dot().shift(RIGHT)
        line1 = Line(point1.get_center(), point2.get_center())
        point3 = Dot().shift(UP)
        line2 = Line(point2.get_center(), point3.get_center())
        self.play(Create(point1), Create(point2), Create(point3))
        self.play(Create(line1), Create(line2))
        self.wait(1)
        self.play(FadeOut(point1), FadeOut(point2), FadeOut(point3), FadeOut(line1), FadeOut(line2))
        self.wait(1)