"""
Example: Getting user input and printing it out, plus date calculation utility.
"""

from datetime import datetime


def get_user_input(prompt: str = "Please enter something: ") -> str:
    """
    Get user input with a custom prompt.

    Args:
        prompt (str): The prompt message to display.

    Returns:
        str: The user's input.
    """
    return input(prompt)


def print_user_input(user_input: str) -> None:
    """
    Print the user's input.

    Args:
        user_input (str): The input to print.
    """
    print("You entered:", user_input)


def calculate_days_between_dates(date1: str, date2: str) -> int:
    """
    Calculate the absolute number of days between two dates.

    Args:
        date1 (str): First date in YYYY-MM-DD format.
        date2 (str): Second date in YYYY-MM-DD format.

    Returns:
        int: Number of days between the dates.

    Raises:
        ValueError: If dates are not in the correct format.
    """
    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((d2 - d1).days)
    except ValueError as e:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e


def main() -> None:
    """Main function to run the example."""
    user_input = get_user_input()
    print_user_input(user_input)

    # Example usage of date calculation
    try:
        days = calculate_days_between_dates("2023-01-01", "2023-01-10")
        print(f"Days between dates: {days}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()