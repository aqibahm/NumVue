from manim import *

class NewtonsThirdLaw(Scene):
    def construct(self):
        # Creating two circles representing two objects
        circle1 = Circle(radius=0.5, color=BLUE).move_to(LEFT * 2)
        circle2 = Circle(radius=0.5, color=RED).move_to(RIGHT * 2)
        
        # Labels for the circles/objects
        label1 = Text("A").next_to(circle1, UP)
        label2 = Text("B").next_to(circle2, UP)
        
        # Displaying the circles and their labels
        self.play(FadeIn(circle1), FadeIn(circle2), Write(label1), Write(label2))
        
        # Moving circles towards each other
        self.play(circle1.animate.move_to(LEFT), circle2.animate.move_to(RIGHT))
        
        # Arrows representing the forces exerted due to Newton's Third Law
        arrow1 = Arrow(circle1.get_edge_center(RIGHT), circle2.get_edge_center(LEFT), color=YELLOW, buff=0)
        arrow2 = Arrow(circle2.get_edge_center(LEFT), circle1.get_edge_center(RIGHT), color=YELLOW, buff=0).reverse_direction()
        
        # Displaying the arrows
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        
        # Text description
        law_text = Text("For every action, there is an equal\nand opposite reaction.")
        law_text.move_to(DOWN * 2)
        
        self.play(Write(law_text))
        self.wait(3)
