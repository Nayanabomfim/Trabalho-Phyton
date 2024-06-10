import tkinter as tk

class Stopwatch:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cronômetro")
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        self.label = tk.Label(self.root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack()

        self.start_button = tk.Button(self.root, text="Iniciar", command=self.start)
        self.start_button.pack(side="left")

        self.stop_button = tk.Button(self.root, text="Parar", command=self.stop)
        self.stop_button.pack(side="left")

        self.reset_button = tk.Button(self.root, text="Resetar", command=self.reset)
        self.reset_button.pack(side="left")

        self.update_time()

    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
                if self.minutes == 60:
                    self.minutes = 0
                    self.hours += 1
            time_string = f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
            self.label.config(text=time_string)
        self.root.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.root.mainloop()