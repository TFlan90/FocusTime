import tkinter as tk
from tkinter import ttk
import time
import winsound

# Function to update the clock labels
def update_clock():
    # Get current time
    current_time = time.localtime()
    if int(time.strftime("%H", current_time)) < 13:
        hours = time.strftime("%H", current_time)
    else:
         hours = str(int(time.strftime("%H", current_time)) - 12)
    minutes = time.strftime("%M", current_time)
    seconds = time.strftime("%S", current_time)

    # Update label text
    hr_label.config(text=hours)
    minute_label.config(text=minutes)
    sec_label.config(text=seconds)
    if int(time.strftime("%H", current_time)) > 12:
        ampm_label.config(text="PM")
    else:
        ampm_label.config(text="AM")

    # Schedule the update_clock function to be called after 1000ms 
    root.after(1000, update_clock)

# Countdown function
def start_countdown(total_seconds):
    def countdown(seconds):
        mins, secs = divmod(seconds, 60)
        countdown_label.config(text=f"{mins:02d}:{secs:02d}")
        if seconds > 0:
            root.after(1000, countdown, seconds - 1)
        else:
            countdown_label.config(text="Time's up!")
            winsound.MessageBeep()
    countdown(total_seconds)

# Function to show prompt and start timer
def show_focus_prompt():
    # Remove existing prompt widgets if any (clean start)
    for widget in [minutes_label, minutes_entry, confirm_button]:
        widget.pack_forget()

    minutes_label.pack(pady=5)
    minutes_entry.pack(pady=5)
    confirm_button.pack(pady=5)

def confirm_time():
    try:
        minutes = int(minutes_entry.get())
        if minutes <= 0:
            raise ValueError
        # Start countdown timer
        start_countdown(minutes * 60)
    except ValueError:
        countdown_label.config(text="Enter a positive integer!")




#main window
root = tk.Tk()
root.title("Focus Time")
root.geometry("500x300")
root.configure(bg="yellow")


#Frame and label for hours
hr_frame = ttk.Frame(root)
hr_frame.pack(side=tk.LEFT)

hr_label = ttk.Label(hr_frame,
                     text = "00",
                     font = ("Comic Sans", 50),
                     foreground= "white",
                     background = "purple",
                     anchor = "center")
hr_label.pack()

#Frame and label for minutes
minute_frame = ttk.Frame(root)
minute_frame.pack(side=tk.LEFT)

minute_label = ttk.Label(minute_frame,
                     text = "00",
                     font = ("Comic Sans", 50),
                     foreground= "white",
                     background = "green",
                     anchor = "center")
minute_label.pack()

#Frame and label for seconds
sec_frame = ttk.Frame(root)
sec_frame.pack(side=tk.LEFT)

sec_label = ttk.Label(sec_frame,
                     text = "00",
                     font = ("Comic Sans", 50),
                     foreground= "white",
                     background = "blue",
                     anchor = "center")
sec_label.pack()

#Frame and label for AM/PM
ampm_frame = ttk.Frame(root)
ampm_frame.pack(side=tk.LEFT)

ampm_label = ttk.Label(ampm_frame,
                     text = "AM",
                     font = ("Comic Sans", 50),
                     foreground= "white",
                     background = "Red",
                     anchor = "center")
ampm_label.pack()


 # Countdown timer label (below the clock)
countdown_label = tk.Label(root,
                           text="",
                           font=("Comic Sans", 48),
                           fg="black",
                           bg="yellow",
                           width=8)
countdown_label.pack(pady=10)

# Widgets for entering minutes and confirming timer
minutes_label = tk.Label(root, text="Enter minutes:", font=("Comic Sans", 14))
minutes_entry = tk.Entry(root, font=("Comic Sans", 14), width=5)

confirm_button = tk.Button(root,
                           text="I'm super cereal",
                           command=confirm_time,
                           relief="groove",
                           bd=6,
                           font=("Comic Sans", 12))       

        
        

focus_button = tk.Button(root, text="We focusin??", command=show_focus_prompt)
focus_button.pack(pady=20)

update_clock()
root.mainloop()
