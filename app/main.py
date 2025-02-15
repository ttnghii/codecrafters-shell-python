import sys


def main():
    # Wait for user input
    while True:
        # Display prompt
        sys.stdout.write("$ ")
        command, *args = input().strip()

        match command:
            case "exit":
                sys.exit(0)
            case "echo":
                print(" ".join(args))
            case default:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
