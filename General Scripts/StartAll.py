import os
import subprocess

# Get the directory of the current script
project_dir = os.path.dirname(os.path.abspath(__file__))

# Paths to the two scripts
start_script = os.path.join(project_dir, 'Button Scripts', 'Start.py')
start_logo_script = os.path.join(project_dir, 'Start Logo.py')

# Run both scripts
try:
    # Run Start.py
    subprocess.run(['python', start_script], check=True)

    # Run Start Logo.py
    subprocess.run(['python', start_logo_script], check=True)

except subprocess.CalledProcessError as e:
    print(f"Error occurred while running a script: {e}")