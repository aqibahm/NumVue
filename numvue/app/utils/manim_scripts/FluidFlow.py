from manim import *

class FluidFlow(Scene):
    def construct(self):
        # Create a 2D grid to represent the scene
        grid = NumberPlane(x_range=(-5, 5), y_range=(-3, 3))

        # Create a list of fluid vectors with positions and directions
        fluid_vectors = [
            {"position": (-3, 1), "direction": [1, 0]},
            {"position": (1, 2), "direction": [0, -1]},
            {"position": (0, 0), "direction": [1, 1]},
            {"position": (-4, -2), "direction": [-1, 1]},
            {"position": (2, -1), "direction": [1, -1]},
        ]

        # Create and add fluid vector arrows to the scene
        fluid_arrows = VGroup()
        for vector_data in fluid_vectors:
            position = vector_data["position"]
            direction = vector_data["direction"]
            vector_arrow = Arrow(
                start=position,
                end=np.add(position, direction),
                buff=0.1,
                color=BLUE,
                stroke_width=2,
            )
            fluid_arrows.add(vector_arrow)

        # Animate the fluid vectors
        self.play(Create(grid), Create(fluid_arrows))
        self.wait(2)