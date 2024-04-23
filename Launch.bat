@echo off
echo Setting up the Deathcore Generator...

REM Navigate to your project directory (modify the path as necessary)
cd path\to\your\project

REM Activate the virtual environment
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Launch the Flask app
echo Launching the Deathcore Generator...
python app.py

echo The Deathcore Generator is now running at http://localhost:5000
pause