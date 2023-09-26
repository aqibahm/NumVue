from manim import *

class Tesseract(Scene):
    def construct(self):
        axes = ThreeDAxes()
        self.play(Create(axes))

        vertices = [
            [-1, -1, -1, -1], [-1, -1, -1, 1], [-1, -1, 1, -1], [-1, -1, 1, 1], 
            [-1, 1, -1, -1], [-1, 1, -1, 1], [-1, 1, 1, -1], [-1, 1, 1, 1], 
            [1, -1, -1, -1], [1, -1, -1, 1], [1, -1, 1, -1], [1, -1, 1, 1],
            [1, 1, -1, -1], [1, 1, -1, 1], [1, 1, 1, -1], [1, 1, 1, 1]
        ]

        edges = [
            (0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7), 
            (4, 5), (4, 6), (5, 7), (6, 7), (8, 9), (8, 10), (8, 12), (9, 11), 
            (9, 13), (10, 11), (10, 14), (11, 15), (12, 13), (12, 14), (13, 15), (14, 15),
            (0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15)
        ]

        tesseract = [
            Dot3D(point=vertices[i]) for i in range(16)
        ]

        tesseract_edges = [
            Line3D(start=tesseract[edge[0]], end=tesseract[edge[1]]) for edge in edges
        ]

        self.play(*[Create(dot) for dot in tesseract], *[Create(line) for line in tesseract_edges])
        self.wait()