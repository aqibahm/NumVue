from manim import *

class SolarSystem(Scene):
    def construct(self):
        # Create the sun
        sun = Dot(color=YELLOW)
        sun_label = Text("Sun").next_to(sun, UP)

        # Create the planet
        planet = Dot(color=BLUE).scale(0.5)
        planet_label = Text("Planet").next_to(planet, UP)

        # Define the ellipse
        a = 3  # semi-major axis
        b = 1  # semi-minor axis
        ellipse = Ellipse(width=a*2, height=b*2)

        # Create the animated planet path
        planet_path = Ellipse(width=a*2, height=b*2).set_stroke(GRAY)
        planet_path.add_updater(lambda m: m.move_to(ellipse.point_from_proportion(self.time % 1)))

        # Animate the planet
        self.play(Create(planet_path), Create(ellipse), Create(sun), Create(planet))
        self.wait(1)
        self.play(Write(sun_label), Write(planet_label))
        self.wait(1)
        self.play(MoveAlongPath(planet, planet_path, run_time=5, rate_func=linear))
        self.wait(1)

        # Add labels to the animation elements
        sun_with_label = Group(sun, sun_label)
        planet_with_label = Group(planet, planet_label)

        self.add(sun_with_label, planet_with_label)
        self.wait(2)