import pygame
import time

# Initialize pygame and the joystick module
pygame.init()
pygame.joystick.init()

# Check if any joystick is connected
if pygame.joystick.get_count() == 0:
    print("No joystick connected.")
else:
    # Initialize the joystick
    joystick = pygame.joystick.Joystick(0)  # You can select other joysticks with indices
    joystick.init()

    print(f"Joystick Name: {joystick.get_name()}")

    # Main loop to check for inputs
    running = True
    while running:
        for event in pygame.event.get():
            # Check if a button is pressed
            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")

            # Check if a button is released
            if event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} released")

            # Check axis movements (like joysticks or triggers)
            if event.type == pygame.JOYAXISMOTION:
                axis = event.axis
                value = joystick.get_axis(axis)
                print(f"Axis {axis} moved to {value:.2f}")

        # This sleep helps reduce CPU usage
        time.sleep(0.01)
