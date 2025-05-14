import tkinter as tk
from tkinter import ttk
import time


root = tk.Tk()
root.title("Focus Time")
root.geometry("500x300")
root.configure(bg="yellow")

hr_frame = ttk.Frame(root)
hr_frame.pack(side=tk.LEFT)

hr_label = ttk.Label(hr_frame,
                     text = "00",
                     font = ("Comic Sans", 50),
                     foreground= "white",
                     background = "purple",
                     anchor = "center")
hr_label.pack()

minute_frame = ttk.Frame(root)
minute_frame.pack(side=tk.LEFT)

minute_label = ttk.Label(minute_frame,
                     text = "00",
                     font = ("Comic Sans", 50),
                     foreground= "white",
                     background = "green",
                     anchor = "center")
minute_label.pack()

sec_frame = ttk.Frame(root)
sec_frame.pack(side=tk.LEFT)

sec_label = ttk.Label(sec_frame,
                     text = "00",
                     font = ("Comic Sans", 50),
                     foreground= "white",
                     background = "blue",
                     anchor = "center")
sec_label.pack()



#label = tk.Label(root, text = "This will be a clock, one day")
#label.pack(padx=175, pady=175)


root.mainloop()
