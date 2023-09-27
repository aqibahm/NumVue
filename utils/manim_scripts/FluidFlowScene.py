from manim import *

class FluidFlowScene(Scene):
    def construct(self):
        # Set up the vector field
        vector_field = self.get_vector_field()

        # Visualize curl, divergence, and convergence
        curl_arrows = self.get_curl_arrows(vector_field)
        div_arrows = self.get_divergence_arrows(vector_field)
        conv_arrows = self.get_convergence_arrows(vector_field)

        # Add the vector field and arrows to the scene
        self.play(Create(vector_field))
        self.play(Create(curl_arrows))
        self.play(Create(div_arrows))
        self.play(Create(conv_arrows))
        self.wait()

    def get_vector_field(self):
        x_range = np.arange(-5, 6, 0.5)
        y_range = np.arange(-5, 6, 0.5)
        vector_field = VGroup()

        for x in x_range:
            for y in y_range:
                vector_field.add(Arrow(
                    start=ORIGIN,
                    end=RIGHT*0.5,
                    fill_opacity=0,
                    stroke_color=YELLOW,
                ).shift([x, y, 0]))

        return vector_field

    def get_curl_arrows(self, vector_field):
        curl_arrows = VGroup()

        for vector in vector_field:
            rot_arrow = Arrow(
                start=vector.get_center(),
                end=vector.get_center() + Rotate(vector.get_vector(), 90),
                fill_opacity=0,
                stroke_color=RED,
            )

            curl_arrows.add(rot_arrow)

        return curl_arrows

    def get_divergence_arrows(self, vector_field):
        div_arrows = VGroup()

        for vector in vector_field:
            div_arrow = Arrow(
                start=vector.get_center(),
                end=vector.get_center() + vector.get_vector(),
                fill_opacity=0,
                stroke_color=GREEN,
            )

            div_arrows.add(div_arrow)

        return div_arrows

    def get_convergence_arrows(self, vector_field):
        conv_arrows = VGroup()

        for vector in vector_field:
            conv_arrow = Arrow(
                start=vector[len(vector) // 2],
                end=vector[len(vector) // 2] - vector.get_vector(),
                fill_opacity=0,
                stroke_color=BLUE,
            )

            conv_arrows.add(conv_arrow)

        return conv_arrows