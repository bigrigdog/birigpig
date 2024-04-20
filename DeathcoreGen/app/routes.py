from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Welcome to DeathcoreGen!"

@app.route('/generate')
def generate_music():
    # Add music generation logic here
    return "Generated music will be displayed here."
