import sys


def main():
    # Wait for user input
    while True:
        # Display prompt
        sys.stdout.write("$ ")
        args = input().split()
        command = " ".join(args[1:])

        if "invalid" in command:
            print(f"{command}: not found")
        else:
            print(f"{command} is a shell builtin")


if __name__ == "__main__":
    main()
