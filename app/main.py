import sys


def main():
    # Display prompt
    sys.stdout.write("$ ")

    # Wait for user input
    command = input().strip()

    # Check if the input is empty
    if command: 
        print(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
