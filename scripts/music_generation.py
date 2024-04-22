 
# music_generation.py 
 
import torch 
 
def generate_stereo_music(model, device): 
    input_noise = torch.randn((1, 2, 44100), device=device)  # Stereo input noise 
    with torch.no_grad(): 
        model.eval() 
        generated_waveform = model(input_noise).cpu().numpy().squeeze(0)  # Squeeze batch dimension 
    return generated_waveform 
