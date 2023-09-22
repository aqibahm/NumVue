from manim import *

class PlanetMotion(Scene):
    def construct(self):
        # Create the sun and planet as circles
        sun = Circle(radius=0.5, color=YELLOW)
        planet = Circle(radius=0.2, color=BLUE)

        # Set the initial position of the planet
        planet.move_to([-3, 0, 0])

        # Create labels for the sun and planet
        sun_label = Text("Sun", color=YELLOW).next_to(sun, UP)
        planet_label = Text("Planet", color=BLUE).next_to(planet, UP)

        # Create the orbit path as a circle
        orbit = Circle(radius=3, color=GRAY, stroke_opacity=0.3)

        # Animation: Planet's motion around the sun
        self.play(Create(sun), Create(planet), Write(sun_label), Write(planet_label))
        self.play(Create(orbit))
        self.wait(1)

        # Animate the planet's motion around the sun
        orbit_points = [orbit.point_from_proportion(i / 100) for i in range(101)]
        planet_path = VMobject()
        planet_path.set_points_smoothly(orbit_points)

        self.play(MoveAlongPath(planet, planet_path), run_time=5, rate_func=linear)
        self.wait(1)