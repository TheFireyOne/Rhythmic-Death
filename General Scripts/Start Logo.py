from tkinter import Tk, Label, PhotoImage
from PIL import Image, ImageTk  # Requires Pillow library
import os

# Create a Tkinter window
root = Tk()
root.title("Combined Viewer")

# Construct the paths to the images
project_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
image1_path = os.path.join(project_dir, 'Sprites', 'logo.gif')
image2_path = os.path.join(project_dir, 'Sprites', 'Start1.gif')

# Resize and display the first sprite
try:
    img1 = Image.open(image1_path).resize((300, 300))  # Resize to 300x300
    image1 = ImageTk.PhotoImage(img1)
    label1 = Label(root, image=image1)
    label1.grid(row=0, column=0)  # Place in grid
except Exception as e:
    print(f"Error loading image1: {e}")

# Resize and display the second sprite
try:
    img2 = Image.open(image2_path).resize((300, 300))  # Resize to 300x300
    image2 = ImageTk.PhotoImage(img2)
    label2 = Label(root, image=image2)
    label2.grid(row=0, column=1)  # Place next to the first image
except Exception as e:
    print(f"Error loading image2: {e}")

# Run the Tkinter event loop
root.mainloop()