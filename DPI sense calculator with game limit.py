def calculate_raw_accel_multiplier(mouse_dpi, raw_accel_multiplier, desired_dpi, game_dpi_limit=None, lowest_game_sense=None, highest_game_sense=None):
    """Calculates the modified Raw Accel multiplier to achieve a desired DPI, respecting game DPI and sensitivity limits.

    Args:
        mouse_dpi: The current DPI setting of your mouse.
        raw_accel_multiplier: Your original Raw Accel multiplier.
        desired_dpi: The effective DPI you want to achieve.
        game_dpi_limit: (Optional) The maximum effective DPI the game allows.
        lowest_game_sense: (Optional) The lowest in-game sensitivity the game allows.
        highest_game_sense: (Optional) The highest in-game sensitivity the game allows.

    Returns:
        The modified Raw Accel multiplier, rounded to 4 decimal places.
    """
    # Base calculation without game limits
    modified_multiplier = (desired_dpi / mouse_dpi) * raw_accel_multiplier
    
    # First, apply game DPI limit if provided
    if game_dpi_limit is not None:
        effective_dpi = mouse_dpi * modified_multiplier
        if effective_dpi > game_dpi_limit:
            modified_multiplier = (game_dpi_limit / mouse_dpi) * raw_accel_multiplier
            print(f"Warning: Desired DPI ({desired_dpi}) exceeds game limit ({game_dpi_limit}). Adjusted multiplier to fit limit.")
    
    # If sensitivity limits are provided, adjust the multiplier
    if lowest_game_sense is not None and highest_game_sense is not None:
        # Calculate the required sensitivity with the current multiplier
        effective_dpi = mouse_dpi * modified_multiplier
        required_sensitivity = desired_dpi / effective_dpi
        
        if required_sensitivity < lowest_game_sense:
            # Adjust multiplier to use the lowest sensitivity
            modified_multiplier = (desired_dpi / (mouse_dpi * lowest_game_sense)) * raw_accel_multiplier
            print(f"Warning: Desired sensitivity ({required_sensitivity:.4f}) is below game minimum ({lowest_game_sense}). Using lowest sensitivity.")
        elif required_sensitivity > highest_game_sense:
            # Adjust multiplier to use the highest sensitivity
            modified_multiplier = (desired_dpi / (mouse_dpi * highest_game_sense)) * raw_accel_multiplier
            print(f"Warning: Desired sensitivity ({required_sensitivity:.4f}) exceeds game maximum ({highest_game_sense}). Using highest sensitivity.")
    
    return round(modified_multiplier, 4)

try:
    # Get inputs from the user with error handling
    mouse_dpi = float(input("Enter your mouse DPI: "))
    raw_accel_multiplier = float(input("Enter your Raw Accel multiplier: "))
    desired_dpi = float(input("Enter your desired DPI: "))
    game_dpi_limit_input = input("Enter the game's DPI limit (or press Enter to skip): ")
    game_dpi_limit = float(game_dpi_limit_input) if game_dpi_limit_input else None
    lowest_game_sense_input = input("Enter the lowest game sensitivity (or press Enter to skip): ")
    lowest_game_sense = float(lowest_game_sense_input) if lowest_game_sense_input else None
    highest_game_sense_input = input("Enter the highest game sensitivity (or press Enter to skip): ")
    highest_game_sense = float(highest_game_sense_input) if highest_game_sense_input else None

    # Calculate the modified multiplier
    modified_multiplier = calculate_raw_accel_multiplier(
        mouse_dpi, raw_accel_multiplier, desired_dpi, game_dpi_limit, lowest_game_sense, highest_game_sense
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