from tkinter import Tk, Label, PhotoImage
import os

# Create a Tkinter window
root = Tk()
root.title("Rhythmic Death")
root.geometry("800x600")  # Set window size

# Construct the paths to the images
project_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
image1_path = os.path.join(project_dir, 'Sprites', 'logo.gif')
image2_path = os.path.join(project_dir, 'Sprites', 'Start1.gif')

# Display the first sprite
try:
    image1 = PhotoImage(file=image1_path)
    image1 = image1.subsample(2)  # Scale down by a factor of 2
    label1 = Label(root, image=image1)
    label1.pack(side="left", padx=50, pady=50)  # Place on the left
except Exception as e:
    print(f"Error loading image1: {e}")

# Display the second sprite
try:
    image2 = PhotoImage(file=image2_path)
    image2 = image2.subsample(4)  # Scale down by a factor of 4
    label2 = Label(root, image=image2)
    label2.pack(side="right", padx=10, pady=10)  # Place on the right
except Exception as e:
    print(f"Error loading image2: {e}")

# Run the Tkinter event loop
root.mainloop()
