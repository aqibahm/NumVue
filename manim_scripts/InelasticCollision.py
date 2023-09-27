from manim import *

class InelasticCollision(Scene):
    def construct(self):
        # Parameters
        body_radius = 0.5
        
        # Bodies: positions and velocities
        bodies = [
            {"position": LEFT * 3 + UP * 2, "velocity": RIGHT * 0.2 + DOWN * 0.15},
            {"position": RIGHT * 3 + UP, "velocity": LEFT * 0.2 + DOWN * 0.15},
            {"position": LEFT * 3 + DOWN * 2, "velocity": RIGHT * 0.15 + UP * 0.2},
            {"position": RIGHT * 3 + DOWN, "velocity": LEFT * 0.15 + UP * 0.2}
        ]
        
        # Create Mobjects for each body
        for body in bodies:
            body["mobject"] = Circle(radius=body_radius, color=WHITE).move_to(body["position"])

        # Display the bodies
        for body in bodies:
            self.play(FadeIn(body["mobject"]))

        # Animation loop
        for _ in range(50):  # 50 steps for the animation; can be adjusted
            for i, body1 in enumerate(bodies):
                for j, body2 in enumerate(bodies):
                    if i < j:  # Avoid double-checking pairs and self-collisions
                        dist = np.linalg.norm(body1["mobject"].get_center() - body2["mobject"].get_center())
                        if dist < 2 * body_radius:
                            # Inelastic collision: They stick together
                            avg_velocity = (body1["velocity"] + body2["velocity"]) / 2
                            body1["velocity"] = avg_velocity
                            body2["velocity"] = avg_velocity

                            # Show force vectors during collision
                            force_arrow1 = Arrow(body1["mobject"].get_center(), body1["mobject"].get_center() + body1["velocity"], color=YELLOW)
                            force_arrow2 = Arrow(body2["mobject"].get_center(), body2["mobject"].get_center() + body2["velocity"], color=YELLOW)
                            self.play(GrowArrow(force_arrow1), GrowArrow(force_arrow2), run_time=0.1)
                            self.remove(force_arrow1, force_arrow2)
                            
            # Update positions
            for body in bodies:
                body["mobject"].shift(body["velocity"])
            self.wait(0.1)

