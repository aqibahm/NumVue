from manim import *

class QuantumMechanics(Scene):
    def construct(self):
        # Create the axis
        axes = Axes(
            x_range=[0, 4],
            y_range=[-1, 1],
            axis_config={"color": BLUE},
        )

        # Label the axis
        axes_labels = axes.get_axis_labels(x_label="Position (x)", y_label="Amplitude")

        # Add the axis and labels to the scene
        self.play(Create(axes), Write(axes_labels))

        # Create a list of quantum wave functions
        wave_functions = [
            lambda x: np.sin((n + 1) * np.pi * x / 4) * np.sqrt(2),
            lambda x: np.sin((n + 1) * np.pi * x / 4) * np.sqrt(2),
        ]

        colors = [YELLOW, RED]  # Colors for the wave functions

        # Create and animate the wave functions and probability densities
        for n, wave_function in enumerate(wave_functions):
            graph = axes.plot(
                lambda x: wave_function(x),
                color=colors[n],
            )

            self.play(Create(graph))
            self.wait(2)

            # Show the probability density
            prob_density = lambda x: wave_function(x) ** 2
            prob_graph = axes.plot(
                lambda x: prob_density(x),
                color=colors[n],
            )
            prob_label = Text("Probability Density", color=colors[n])
            prob_label.next_to(axes_labels, UP)

            self.play(Transform(graph, prob_graph), Write(prob_label))
            self.wait(2)

            # Fade out the wave function and probability density
            self.play(FadeOut(graph), FadeOut(prob_graph), FadeOut(prob_label))
            self.wait(1)

        # Wait for a few seconds at the end
        self.wait(3)
