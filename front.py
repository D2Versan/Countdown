import tkinter as tk
from datetime import datetime, timedelta

class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Clock")

        self.target_datetime = datetime(2023, 12, 31, 23, 59, 59)

        self.label = tk.Label(root, font=("Times New Roman", 36))
        self.label.pack(pady=20)

        self.update_countdown()

    def update_countdown(self):
        current_datetime = datetime.now()
        time_left = self.target_datetime - current_datetime

        if time_left.total_seconds() <= 0:
            self.label.config(text="This is the end")
        else:
            days = time_left.days
            hours, remainder = divmod(time_left.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            countdown_str = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
            self.label.config(text=countdown_str)

        self.root.after(1000, self.update_countdown)

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()
