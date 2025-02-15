import sys


def main():
    # Wait for user input
    while True:
        # Display prompt
        sys.stdout.write("$ ")
        command = input().lstrip("echo ")
        if command:
            if "invalid" in command:
                print(f"{command}: command not found")
            print(command)



if __name__ == "__main__":
    main()
