import sys


def main():
    # Display prompt
    sys.stdout.write("$ ")

    # Wait for user input
    command = input().strip()
    # Check if the input is empty
    if command:
        print(f"{command}: command not found")

    # Recursively call main to keep the shell running
    main()


if __name__ == "__main__":
    main()
