import tkinter as tk
import pyperclip

# List of names
names = [
    "Norman", "JAFB", "Lynwood-M", "Eagle", "Harden", "Kauwela",
    "Fiskar", "Oconee", "Clarence", "Englandtown", "Kitesboro",
    "Suli", "Yunzhou", "Jepo", "Meihua", "Radang", "Kashio",
    "Kibo", "Umibutsu", "Bilabadi", "Tenang", "Udyanapura"
]

# Create the main window
root = tk.Tk()
root.title("Name Copier")
root.geometry("316x196")  # Default size
root.configure(bg="#111")  # Dark background
root.attributes("-topmost", True)  # Always on top
root.resizable(True, True)  # Allow resizing

# Frame to hold names
frame = tk.Frame(root, bg="#111")
frame.pack(expand=True, fill="both", padx=5, pady=5)

# Last copied label tracker
last_copied = None

def copy_name(name, label):
    global last_copied

    # Copy to clipboard
    copy_text = name.replace("-", " ") if name == "Lynwood-M" else name
    pyperclip.copy(copy_text)

    # Reset color of previous label
    if last_copied:
        last_copied.config(fg="white")

    # Highlight the copied name
    label.config(fg="red")
    last_copied = label

# Create name labels
for name in names:
    lbl = tk.Label(frame, text=name, fg="white", bg="#222", font=("Arial", 10, "bold"),
                   cursor="hand2", padx=6, pady=3)
    lbl.pack(anchor="w", padx=2, pady=1)  # Keep layout fixed
    lbl.bind("<Button-1>", lambda e, n=name, l=lbl: copy_name(n, l))

root.mainloop()

