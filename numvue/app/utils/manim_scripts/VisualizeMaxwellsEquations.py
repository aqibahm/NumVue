from manim import *

class VisualizeMaxwellsEquations(Scene):
    def construct(self):
        self.equation1()
        self.equation2()
        self.equation3()
        self.equation4()

    def equation1(self):
        equation = TexMobject(r"\nabla \cdot \textbf{E} = \frac{\rho}{\epsilon_0}")
        self.play(Write(equation))
        self.wait(1)
        self.play(FadeOut(equation))
        self.wait(1)

    def equation2(self):
        equation = TexMobject(r"\nabla \cdot \textbf{B} = 0")
        self.play(Write(equation))
        self.wait(1)
        self.play(FadeOut(equation))
        self.wait(1)

    def equation3(self):
        equation = TexMobject(r"\nabla \times \textbf{E} = - \frac{\partial \textbf{B}}{\partial t}")
        self.play(Write(equation))
        self.wait(1)
        self.play(FadeOut(equation))
        self.wait(1)

    def equation4(self):
        equation = TexMobject(r"\nabla \times \textbf{B} = \mu_0 \textbf{J} + \mu_0 \epsilon_0 \frac{\partial \textbf{E}}{\partial t}")
        self.play(Write(equation))
        self.wait(1)
        self.play(FadeOut(equation))
        self.wait(1)