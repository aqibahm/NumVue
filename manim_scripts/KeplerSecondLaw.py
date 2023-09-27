from manim import *

class KeplerSecondLaw(Scene):
    def construct(self):
        # Create the ellipse representing the planet's orbit
        orbit = Ellipse(width=4, height=2, color=WHITE, stroke_opacity=0.7)

        # Create the Sun at one of the foci of the ellipse
        sun = Dot(point=orbit.get_start(), color=YELLOW)

        # Create labels for the Sun and the planet's orbit
        sun_label = Text("Sun", color=YELLOW).next_to(sun, UP)
        orbit_label = Text("Orbit", color=WHITE).next_to(orbit, UP)

        # Create the planet as a small dot on the ellipse
        planet = Dot(color=BLUE)

        # Create a line segment from the Sun to the planet
        line_to_planet = Line(sun.get_center(), planet.get_center(), color=RED)

        # Define color mappings for different time intervals
        colors = [GREEN, BLUE, PURPLE, PINK, ORANGE]

        # Animate the display
        self.play(Create(orbit), Create(sun), Write(sun_label), Write(orbit_label))
        self.wait(1)

        # Animate the planet's motion and the sweeping of areas
        for i in range(5):
            proportion_start = i / 5
            proportion_end = (i + 1) / 5

            planet.move_to(orbit.point_from_proportion(proportion_start))
            line_to_planet.put_start_and_end_on(sun.get_center(), planet.get_center())

            self.add(planet, line_to_planet)

            # Animate the planet's motion for the current time interval
            self.play(MoveAlongPath(planet, orbit, run_time=2), run_time=2)

            # Fill the swept area with a color
            area = Polygon(
                sun.get_center(),
                line_to_planet.get_start(),
                line_to_planet.get_end(),
                color=colors[i],
                fill_opacity=0.5,
            )
            self.play(Create(area))

        self.wait(1)