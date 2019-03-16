import tkinter as tk

print(tk.__doc__)
root = tk.Tk()
root.title("Hello world!wo!wo!")
thelabel = tk.Label(root, text="Hello world!")
thelabel.pack()
root.mainloop()
