import sys


def main():
    # Wait for user input
    while True:
        # Display prompt
        sys.stdout.write("$ ")
        command = input()
        # Check for exit command
        if command == "exit 0":
            sys.exit(0)
        if command:
            print(f"{command}: command not found") 


if __name__ == "__main__":
    main()
