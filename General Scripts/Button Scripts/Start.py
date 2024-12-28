from tkinter import Tk, Label, PhotoImage
import os

username = os.getlogin()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the image
# Navigate up one directory from script_folder and then into Sprites
image_path = os.path.join(script_dir, '..', 'Sprites', 'Start1.gif')

# Resolve the path to an absolute path
image_path = os.path.abspath(image_path)

print(f"Image path: {image_path}")

# Create a Tkinter window
root = Tk()
root.title("Rhythmic Death")

# Load the GIF image using Tkinter's PhotoImage
try:
    image = PhotoImage(file=image_path)  # Create PhotoImage object

    # Create a label to display the image
    label = Label(root, image=image)  # Set the image attribute to the PhotoImage object
    label.pack()

except Exception as e:
    print(f"Error loading image: {e}")

# Run the Tkinter event loop
root.mainloop()