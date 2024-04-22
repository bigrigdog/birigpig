 
# app.py 
 
import streamlit as st 
from scripts.music_generation import generate_stereo_music 
import torch 
 
def main(): 
    st.title("Advanced Deathcore Music Generator") 
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') 
    model = StereoMusicModel() 
    model.load_state_dict(torch.load('models/musicgen_stereo_large.pth', map_location=device)) 
    model.to(device) 
 
    with st.sidebar: 
        generate = st.button("Generate Music") 
        upload = st.file_uploader("Upload WAV to inspire generation:", type=['wav']) 
 
    if generate: 
        generated_waveform = generate_stereo_music(model, device) 
        st.audio(generated_waveform, format='audio/wav') 
 
    if upload is not None: 
        # Process and potentially retrain model based on the upload 
        st.write("Uploaded Waveform") 
        st.audio(upload, format='audio/wav') 
