import sys


def main():
    # Wait for user input
    while True:
        # Display prompt
        sys.stdout.write("$ ")
        command = input()
        args = command.split()

        if "invalid" in command:
            print(f"{" ".join(args[1:])}: not found")
        else:
            new_command = " ".join(args[1:])
            match args[0]:
                case "type":
                    print(f"{new_command} is a shell builtin")
                case "echo":
                    print(new_command)
                case "exit":
                    sys.exit(0)
                case default:
                    print(command)


if __name__ == "__main__":
    main()
