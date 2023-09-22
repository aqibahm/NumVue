from manim import *

class curves2(ThreeDScene):

    def construct(self):

        colors = ["#0000ff","#8bff26","#26e9ff","#ff3c00","#ffa600"]
        a = ValueTracker(-7.999) # Needs to be just above lower limit then animated to end limit
        b = ValueTracker(1)      # This controls the scaling of curve
        r = ValueTracker(0)      # This controls the rotation of the curve copies
        h = ValueTracker(4)      # Misc variable when needed
        k = ValueTracker(1)      # Main variable to cycle through curve variations

        # a1 = np.sin(4*t)
        # b1 = np.cos(0.5*k.get_value()*t)*np.sqrt(np.cos(np.cos(k.get_value()*t)))

        func1 = ParametricFunction(lambda t: np.array((np.sin(4*t),np.cos(0.5*k.get_value()*t)*np.sqrt(np.cos(np.cos(k.get_value()*t))),0)), t_range = np.array([-8, a.get_value()]), fill_opacity=0).set_color_by_gradient(colors)
        func2 = ParametricFunction(lambda t: np.matmul(np.array((np.sin(4*t),np.cos(0.5*k.get_value()*t)*np.sqrt(np.cos(np.cos(k.get_value()*t))),0)),np.array([[np.cos(r.get_value()*PI/180), -np.sin(r.get_value()*PI/180),0],[np.sin(r.get_value()*PI/180),np.cos(r.get_value()*PI/180),0],[0,0,1]])), t_range = np.array([-8, a.get_value()]), fill_opacity=0).set_color_by_gradient(colors)
        # K = MathTex( r'k=',color=YELLOW).to_edge(UL)
        # kvalue = DecimalNumber(k.get_value(),num_decimal_places=2,color=YELLOW).next_to(K,RIGHT)
        
        
        func1.add_updater(lambda mob: mob.become(ParametricFunction(lambda t: np.array((np.sin(4*t),np.cos(0.5*k.get_value()*t)*np.sqrt(np.cos(np.cos(k.get_value()*t))),0)), t_range = np.array([-8, a.get_value()]), fill_opacity=0).set_color_by_gradient(colors).scale(b.get_value())))
        func2.add_updater(lambda mob: mob.become(ParametricFunction(lambda t: np.matmul(np.array((np.sin(4*t),np.cos(0.5*k.get_value()*t)*np.sqrt(np.cos(np.cos(k.get_value()*t))),0)),np.array([[np.cos(r.get_value()*PI/180), -np.sin(r.get_value()*PI/180),0],[np.sin(r.get_value()*PI/180),np.cos(r.get_value()*PI/180),0],[0,0,1]])), t_range = np.array([-8, a.get_value()]), fill_opacity=0).set_color_by_gradient(colors).scale(b.get_value())))
        # kvalue.add_updater(lambda mob: mob.set_value(k.get_value()))
        # kvalue.add_updater(lambda mob: mob.next_to(K,RIGHT))
        
        

        self.add(func1)
        self.add(func2)


        self.move_camera(45*DEGREES,45*DEGREES,0*DEGREES)
        self.begin_ambient_camera_rotation(45*DEGREES/6,about='theta')
        
        self.play(a.animate.set_value(8),b.animate.set_value(3.5),r.animate.set_value(90),run_time=5)
        self.play(k.animate.set_value(2.01),run_time=3)
        self.wait(2)
        self.play(k.animate.set_value(2.3),run_time=3)
        self.wait(2)
        self.play(k.animate.set_value(2.65),run_time=3)
        self.wait(2)
        self.play(k.animate.set_value(3.21),run_time=3)
        self.wait(2)
        self.play(k.animate.set_value(4.01),run_time=3)
        self.wait(2)
        self.play(k.animate.set_value(4.4),run_time=3)
        self.wait(2)
        self.play(k.animate.set_value(4.8),run_time=3)
        self.wait(2)
        self.play(k.animate.set_value(5.3),run_time=3)
        self.wait(2)
        self.play(k.animate.set_value(6.41),run_time=3)
        self.wait(2)
        self.play(k.animate.set_value(6.85),run_time=3)
        self.wait(2)
        self.play(k.animate.set_value(8.07),run_time=3)
        self.wait(2)
        self.play(k.animate.set_value(9.15),run_time=3)
        self.wait(2)
        self.play(k.animate.set_value(9.62),run_time=3)
        self.wait(2)
        self.play(k.animate.set_value(9.99),run_time=3)
        self.wait(2)
        self.play(k.animate.set_value(10),run_time=3)
        self.wait(2)
        self.stop_ambient_camera_rotation(about='theta')
        self.wait(5)