import torch

def generate_music(model, initial_tensor, sequence_length=500):
    """Generate music sequence from an initial tensor."""
    model.eval()
    outputs = [initial_tensor]
    with torch.no_grad():
        for _ in range(sequence_length):
            input_tensor = outputs[-1].unsqueeze(0)
            next_tensor = model(input_tensor)
            outputs.append(next_tensor)
    return outputs