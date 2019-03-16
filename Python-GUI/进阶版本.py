import tkinter as tk


class App:
    def __init__(self, windown):
        frame = tk.Frame(windown)
        frame.pack(side=tk.LEFT,  padx=10, pady=10)
        self.hi_there = tk.Button(frame, text="打招呼", fg="black",bg="yellow", command=self.say_hi)
        self.hi_there.pack()

    @staticmethod
    def say_hi():
        print("什么鬼东西啊！")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop( )
