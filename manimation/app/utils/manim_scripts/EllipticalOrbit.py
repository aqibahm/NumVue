from manim import *

class EllipticalOrbit(Scene):
    def construct(self):
        # Creating the sun
        sun = Circle(radius=1, color=YELLOW)
        sun_label = Tex("Sun").next_to(sun, UP)
        self.play(Create(sun), Write(sun_label))

        # Creating the planet
        planet = Dot(radius=0.2, color=BLUE).move_to(2 * RIGHT)
        planet_label = Tex("Planet").next_to(planet, RIGHT)
        self.play(Create(planet), Write(planet_label))

        # Creating the orbit
        orbit = Ellipse(width=4, height=2, color=WHITE)
        self.play(Create(orbit))

        # Creating the animation of planet's orbit
        orbit_animation = MoveAlongPath(planet, orbit, rate_func=linear)
        self.play(orbit_animation, run_time=5)

        self.wait()