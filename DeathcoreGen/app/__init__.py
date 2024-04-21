from flask import Flask, request, jsonify
from music_generator import generate_deathcore_music

app = Flask(__name__)

@app.route('/generate_music', methods=['POST'])
def generate_music():
    # Extract parameters from the request
    data = request.json
    tempo = data.get('tempo', 180)
    key = data.get('key', 'C')
    scale = data.get('scale', 'minor')
    
    # Generate music based on parameters
    generated_music = generate_deathcore_music(tempo, key, scale)
    
    # Return the generated music as JSON
    return jsonify({'generated_music': generated_music})

if __name__ == "__main__":
    app.run(debug=True)
