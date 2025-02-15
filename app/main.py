import sys


def main():
    # Wait for user input
    while True:
        # Display prompt
        sys.stdout.write("$ ")
        command = input()
        args = command.split()

        match args[0]:
            case "exit":
                sys.exit(0)
            case "echo":
                print(" ".join(args[1:]))
            case default:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
