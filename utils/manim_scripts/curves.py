from manim import *

class curves(ThreeDScene):

    # Butterfly Parametric Curve
    def func(self, t):
            return np.array((np.cos(t)*(np.exp(np.cos(t))-2*np.cos(4*t)-(np.sin(t/12))**5),np.sin(t)*(np.exp(np.cos(t))-2*np.cos(4*t)-(np.sin(t/12))**5), 0))

    def construct(self):
        ax = ThreeDAxes()
        colors = ["#0000ff","#8bff26","#26e9ff","#ff3c00","#ffa600"]
        a = ValueTracker(.00001)
        b = ValueTracker(0.5)
        func1 = ParametricFunction(self.func, t_range = np.array([0, a.get_value()]), fill_opacity=0).set_color_by_gradient(colors)
        func1.add_updater(lambda mob: mob.become(ParametricFunction(self.func, t_range = np.array([0, a.get_value()]), fill_opacity=0).set_color_by_gradient(colors).scale(b.get_value())))
        self.add(func1)
        self.move_camera(45*DEGREES,45*DEGREES,0*DEGREES)
        self.begin_ambient_camera_rotation(45*DEGREES/6,about='theta')
        self.play(a.animate.set_value(12*PI),b.animate.set_value(1.5),run_time=60)
        self.stop_ambient_camera_rotation(about='theta')
        self.wait(5)