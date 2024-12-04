"""
This is a simple Python application that greets the user.
"""

def greet(name):
    """
    Returns a greeting message for the given name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


print(greet("World"))
