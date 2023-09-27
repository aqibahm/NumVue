from manim import *

class SineCurve(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-5, 5, 1),
            y_range=(-2, 2, 1),
            x_length=10,
            y_length=4,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": range(-5, 6)},
        )
        sine_curve = axes.get_graph(lambda x: np.sin(x), color=YELLOW, x_range=(-5,5))
        moving_point = always_redraw(
            lambda: Dot().move_to(sine_curve.point_from_proportion(self.t))
        )
        self.play(Create(axes), Create(sine_curve))
        self.wait()
        self.play(Create(moving_point))
        self.play(
            self.t.animate.set_value(1),
            run_time=5,
            rate_func=linear
        )
        self.wait()

        self.play(
            self.t.animate.set_value(0),
            run_time=5,
            rate_func=linear
        )
        self.wait()