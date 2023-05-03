import tkinter as tk
import time

class FocusedClock(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, font=("Helvetica", 16))
        self.label.pack(side="top", fill="both", expand=True)
        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S %p")
        current_date = time.strftime("%A, %B %d, %Y")
        self.label.config(text=f"{current_time}\n{current_date}")
        self.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Focused Clock")
    clock = FocusedClock(root)
    clock.pack(side="top", fill="both", expand=True)
    root.mainloop()
