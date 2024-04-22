 
# data_processing.py 
 
def prepare_stereo_waveforms(waveform, sample_rate=44100): 
    # Assume waveform is a NumPy array with shape (2, N) where N is the number of samples 
    # Convert waveform to PyTorch tensor with shape (1, 2, N) for model input 
    tensor_waveform = torch.tensor(waveform[np.newaxis, :, :], dtype=torch.float32) 
    return tensor_waveform 
