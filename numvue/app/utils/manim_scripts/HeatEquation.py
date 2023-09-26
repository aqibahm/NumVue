from manim import *

class HeatEquation(Scene):
    def construct(self):
        # Constants
        k = 0.2  # Thermal diffusivity
        L = 3    # Length of the object
        T0 = 100  # Initial temperature of the object
        T_surroundings = 25  # Temperature of the surroundings

        # Time parameters
        dt = 0.1  # Time step size
        t_total = 5  # Total time for animation

        # Calculate the number of steps
        num_steps = int(t_total / dt)

        # Initialize the temperature array
        num_points = 50  # Number of points to discretize the object
        dx = L / num_points
        temperature = np.full(num_points, T0)

        # Create the object
        object_shape = Rectangle(height=1, width=L, fill_opacity=1)
        object_shape.set_fill(GREY, 1)
        self.add(object_shape)

        # Iterate over time steps
        for step in range(num_steps):
            # Update temperature for each point
            for i in range(1, num_points - 1):
                temperature[i] += k * dt * ((temperature[i - 1] - 2 * temperature[i] + temperature[i + 1]) / dx**2)

            # Update the temperature display
            temperature_display = DecimalNumber(temperature[0], num_decimal_places=1, include_sign=True)
            temperature_display.next_to(object_shape, DOWN)
            self.add(temperature_display)

            # Update the object color based on temperature
            object_shape.set_fill(self.get_color(temperature[0] - T_surroundings), 1)

            # Wait for the time step
            self.wait(dt)

        self.wait()

    def get_color(self, temperature_difference):
        if temperature_difference < 0:
            return BLUE
        elif temperature_difference > 0:
            return RED
        else:
            return WHITE