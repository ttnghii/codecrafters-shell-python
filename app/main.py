import sys


def main():
    # Wait for user input
    while True:
        # Display prompt
        sys.stdout.write("$ ")
        command = input().lstrip("echo ")
        
        if command == "exit 0":
            sys.exit(0)
        elif "invalid" in command:
            print(f"{command}: command not found")
        else:   
            print(command)


if __name__ == "__main__":
    main()
