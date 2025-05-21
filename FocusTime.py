import tkinter as tk
from tkinter import ttk
import time

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

update_clock()
root.mainloop()
