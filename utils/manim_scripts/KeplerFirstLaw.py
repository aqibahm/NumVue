from manim import *

class KeplerFirstLaw(Scene):
    def construct(self):
        # Create the ellipse representing the planet's orbit
        orbit = Ellipse(width=4, height=2, color=WHITE, stroke_opacity=0.7)

        # Create the Sun at one of the foci of the ellipse
        sun = Dot(point=orbit.get_start(), color=YELLOW)

        # Create labels for the Sun and the planet's orbit
        sun_label = Text("Sun", color=YELLOW).next_to(sun, UP)
        orbit_label = Text("Orbit", color=WHITE).next_to(orbit, UP)

        # Animate the display
        self.play(Create(orbit), Create(sun), Write(sun_label), Write(orbit_label))
        self.wait(2)