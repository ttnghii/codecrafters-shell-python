import sys


def main():
    # Wait for user input
    while True:
        # Display prompt
        sys.stdout.write("$ ")
        command = input()
        args = command.split()

        match args[0]:
            case "invalid":
                print(f"{command}: not found")
            case default:
                print(f"{command}: is a shell builtin")


if __name__ == "__main__":
    main()
