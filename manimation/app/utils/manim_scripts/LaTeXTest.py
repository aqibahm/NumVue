from manim import *

class LaTeXTest(Scene):
    def construct(self):
        tex = MathTex(r"\frac{\pi}{2} = 90^\circ")
        self.play(Create(tex))
        self.wait(2)