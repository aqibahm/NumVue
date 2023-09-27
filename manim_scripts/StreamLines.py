from manim import *
import numpy as np

class StreamLines(Scene):
    def construct(self):
        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos)
        mob = StreamLines(func, x_range=[-5, 5, 1], y_range=[-5, 5, 1], stroke_width=3)
        self.add(mob)
        self.play(GrowFromCenter(mob))
