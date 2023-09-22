from manim import *

class NeuralNetwork(Scene):
    def construct(self):
        # Create input layer
        input_layer = self.create_layer(4, "Input", BLUE)

        # Create hidden layers
        hidden_layer1 = self.create_layer(5, "Hidden 1", GREEN).next_to(input_layer, RIGHT)
        hidden_layer2 = self.create_layer(3, "Hidden 2", YELLOW).next_to(hidden_layer1, RIGHT)

        # Create output layer
        output_layer = self.create_layer(2, "Output", RED).next_to(hidden_layer2, RIGHT)

        # Connect layers
        self.connect_layers(input_layer, hidden_layer1)
        self.connect_layers(hidden_layer1, hidden_layer2)
        self.connect_layers(hidden_layer2, output_layer)

        # Add layers to the scene
        self.play(Create(input_layer), Create(hidden_layer1), Create(hidden_layer2), Create(output_layer))
        self.wait(2)

    def create_layer(self, num_neurons, label, color):
        layer = VGroup()
        neurons = VGroup()

        for i in range(num_neurons):
            neuron = Circle(radius=0.2, color=color)
            neurons.add(neuron)

        layer.add(neurons)
        layer.add(Text(label).next_to(neurons, UP))

        return layer

    def connect_layers(self, layer1, layer2):
        for neuron1 in layer1[0]:
            for neuron2 in layer2[0]:
                self.play(Create(Line(neuron1.get_center(), neuron2.get_center())))
