import sys


def main():
    # Wait for user input
    while True:
        # Display prompt
        sys.stdout.write("$ ")
        command = input()

        match command:
            case "exit":
                    sys.exit(0)
            case command if command.startswith("echo"):
                print(f"{command[len("echo") :]}")
            case command if command.startswith("type invalid"):
                print(f"{command[len('type ') :]}: not found")
            case command if command.startswith("type valid"):
                print(f"{command[len('type ') :]} is /usr/local/bin/{command[len('type ') :]}")
            case command if command.startswith("type"):
                print(f"{command[len('type ') :]} is /usr/bin/{command[len('type ') :]}")
            case _:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
