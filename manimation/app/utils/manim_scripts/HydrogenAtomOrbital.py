from manim import *

class HydrogenAtomOrbital(Scene):
    def construct(self):
        # Define the electron and proton objects
        electron = Dot().set_color(BLUE).scale(0.5)
        proton = Dot().set_color(RED).scale(1)

        # Define the orbit path for the electron
        orbit = Circle(radius=2, color=WHITE, stroke_opacity=0.3)

        # Add objects to the scene
        self.add(orbit, electron, proton)

        # Animate the electron orbiting around the proton
        self.play(MoveAlongPath(electron, orbit), run_time=5)
        self.wait(2)