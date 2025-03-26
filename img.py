import tkinter as tk
root = tk.Tk()
root.title("Image in Tkinter")
root.geometry('100x200')
# Load image
img = tk.PhotoImage(file="real_madrid.png")
# Create a label and set the image
label = tk.Label(root, image=img)
label.pack()
root.mainloop()