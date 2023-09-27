from manim import *

class IntegralAnimation(Scene):
    def construct(self):
        axes = Axes(
            y_range=[-1.5, 1.5],
            y_length=6,
            x_range=[0, PI],
            x_length=10,
            axis_config={
                "numbers_to_include": np.arange(0, PI + 1, 1)
            }
        )
        self.play(Create(axes))

        sin_graph = axes.get_graph(np.sin, x_range=[0, PI])
        self.play(Create(sin_graph))

        integral_area = self.get_integral_area(sin_graph, x_min=0, x_max=PI)
        self.play(Create(integral_area), run_time=2)

        self.wait(2)

    def get_integral_area(self, graph, x_min, x_max):
        graph_points = graph.points
        x_points = [point[0] for point in graph_points]
        y_points = [point[1] for point in graph_points]

        y_points.append(0)
        y_points.insert(0, 0)

        x_area = [x_min, *x_points, x_max]
        y_area = [*y_points, 0, 0]

        points = [
            [x, y, 0]
            for x, y in zip(x_area, y_area)
        ]

        integral_area = Polygon(*points, fill_color=GREEN, fill_opacity=0.5, stroke_color=GREEN)
        return integral_area