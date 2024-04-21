import torch.nn as nn

class DeathcoreGenerator(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(DeathcoreGenerator, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))  # Assuming output is in range [0, 1]
        return x
