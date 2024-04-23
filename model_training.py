import torch
import torch.nn as nn
import torch.optim as optim

class MusicGeneratorModel(nn.Module):
    def __init__(self):
        super(MusicGeneratorModel, self).__init__()
        self.lstm = nn.LSTM(input_size=256, hidden_size=512, num_layers=2, batch_first=True)
        self.fc = nn.Linear(512, 128)  # Assuming 128 is the size of the output space

    def forward(self, x):
        x, _ = self.lstm(x)
        x = self.fc(x[:, -1, :])  # Getting the last time step output
        return x

def train(model, train_loader, num_epochs=10):
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    model.train()
    for epoch in range(num_epochs):
        for batch, (features, labels) in enumerate(train_loader):
            optimizer.zero_grad()
            outputs = model(features)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}")

    print("Model training completed.")
    torch.save(model.state_dict(), 'music_generation_model.pth')