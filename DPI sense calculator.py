def calculate_raw_accel_multiplier(mouse_dpi, raw_accel_multiplier, desired_dpi):
    """Calculates the modified Raw Accel multiplier to achieve a desired DPI.

    Args:
        mouse_dpi: The current DPI setting of your mouse.
        raw_accel_multiplier: Your original Raw Accel multiplier.
        desired_dpi: The effective DPI you want to achieve.

    Returns:
        The modified Raw Accel multiplier, rounded to 4 decimal places.
    """
    modified_multiplier = (desired_dpi / mouse_dpi) * raw_accel_multiplier
    return round(modified_multiplier, 4)

try:
    # Get inputs from the user with error handling
    mouse_dpi = float(input("Enter your mouse DPI: "))
    raw_accel_multiplier = float(input("Enter your Raw Accel multiplier: "))
    desired_dpi = float(input("Enter your desired DPI: "))

    # Calculate the modified multiplier
    modified_multiplier = calculate_raw_accel_multiplier(
        mouse_dpi, raw_accel_multiplier, desired_dpi
    )

    # Print the result (core functionality)
    print("Modified Raw Accel multiplier:", modified_multiplier)

    # Optional clipboard feature
    try:
        import pyperclip
        pyperclip.copy(str(modified_multiplier))
        print("Result copied to clipboard!")
    except ImportError:
        print("Pyperclip not installed, skipping clipboard copy.")

except ValueError:
    print("Error: Please enter valid numbers")
except ZeroDivisionError:
    print("Error: Mouse DPI cannot be zero")

input("Press Enter to exit...")