#!/usr/bin/env python3
"""
Simple hello world program
"""


def say_hello(name="World"):
    """
    Return a greeting message
    
    Args:
        name: Name to greet (default: "World")
    
    Returns:
        str: Greeting message
    """
    return f"Hello, {name}!"


def main():
    """Main function"""
    print(say_hello())
    print(say_hello("GitHub Copilot"))


if __name__ == "__main__":
    main()
