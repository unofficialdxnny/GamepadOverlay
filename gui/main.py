import tkinter as tk
from tkinter import Canvas
import pygame

# Initialize pygame for controller handling
pygame.init()
pygame.joystick.init()

# Function to initialize a joystick (controller)
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

# Create the main window using Tkinter
root = tk.Tk()
root.title("Controller Input Display")
root.geometry("400x400")

# Dynamically create labels for each button based on the actual number of buttons
button_count = (
    joystick.get_numbuttons()
)  # Get the actual number of buttons on the joystick
button_labels = []
for i in range(button_count):  # Create labels based on the number of buttons
    label = tk.Label(root, text=f"Button {i}: Released", font=("Arial", 10))
    label.pack()
    button_labels.append(label)

# Create a canvas for joystick movement visualization
canvas = Canvas(root, width=200, height=200, bg="white")
canvas.pack(pady=20)

# Draw static joystick outlines
left_stick = canvas.create_oval(50, 50, 100, 100, outline="black", width=2)
right_stick = canvas.create_oval(150, 50, 200, 100, outline="black", width=2)


# Function to update the UI with controller inputs
def update_controller_state():
    pygame.event.pump()  # Process controller events

    # Update buttons' state
    for i in range(button_count):
        if joystick.get_button(i):
            button_labels[i].config(text=f"Button {i}: Pressed", fg="green")
        else:
            button_labels[i].config(text=f"Button {i}: Released", fg="black")

    # Update joystick position (left joystick example)
    axis_x = joystick.get_axis(0)  # Left stick horizontal
    axis_y = joystick.get_axis(1)  # Left stick vertical
    # Move the left joystick representation
    canvas.coords(
        left_stick,
        75 + axis_x * 25,
        75 + axis_y * 25,
        125 + axis_x * 25,
        125 + axis_y * 25,
    )

    # Right joystick
    axis_x_right = joystick.get_axis(2)  # Right stick horizontal
    axis_y_right = joystick.get_axis(3)  # Right stick vertical
    # Move the right joystick representation
    canvas.coords(
        right_stick,
        150 + axis_x_right * 25,
        75 + axis_y_right * 25,
        200 + axis_x_right * 25,
        125 + axis_y_right * 25,
    )

    # Keep updating
    root.after(50, update_controller_state)


# Start polling the controller state
update_controller_state()

# Start the Tkinter main loop
root.mainloop()

# Quit pygame when the application closes
pygame.quit()
