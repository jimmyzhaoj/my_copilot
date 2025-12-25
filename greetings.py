#!/usr/bin/env python3
"""
greetings.py

Ask 'Who is there?' and print greeting messages "Merry Chrismas" to each name.
"""

def main():
    names_input = input("Who is there? (separate multiple names with commas) ")
    if not names_input.strip():
        print("No names provided.")
        return
    names = [n.strip() for n in names_input.split(",") if n.strip()]
    for name in names:
        print(f'Merry Chrismas, {name}!')


if __name__ == "__main__":
    main()
