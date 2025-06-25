##Focus Time
This is a simple Python app that shows a real-time clock and includes a basic countdown timer with a sound notification when time’s up. It uses tkinter for the GUI.

Features
12-hour digital clock (with AM/PM)

Custom countdown timer

Plays a sound when the timer ends

Basic UI using Comic Sans and bright colors

How to Run
Make sure you have Python 3 installed.

Install dependencies:

nginx
Copy
Edit
pip install playsound
Run the script:

nginx
Copy
Edit
python focus_timer.py
Notes
To change the alarm sound, replace ghost-moan.wav with your own .wav file.

If you're using PyInstaller to make an .exe, the resource_path() function helps include the sound file properly.
