"""Entry point for prova."""
from .cli import *  # pragma: no cover
from .advcode import *  # pragma: no cover

    # nn = NeuralNetwork(2, 2, 2, hidden_layer_weights=[0.15, 0.2, 0.25, 0.3], hidden_layer_bias=0.35, output_layer_weights=[0.4, 0.45, 0.5, 0.55], output_layer_bias=0.6)

    # for i in range(10000):
    #     nn.train([0.05, 0.1], [0.01, 0.99])
    #     print(i, round(nn.calculate_total_error([[[0.05, 0.1], [0.01, 0.99]]]), 9))
    #     nn.inspect()
if __name__ == "__main__":  # pragma: no cover
    main()