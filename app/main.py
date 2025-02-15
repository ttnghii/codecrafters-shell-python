import sys


def main():
    # Wait for user input
    while True:
        # Display prompt
        sys.stdout.write("$ ")
        command = input().strip("echo ")
        if command:
            print(command)


if __name__ == "__main__":
    main()
