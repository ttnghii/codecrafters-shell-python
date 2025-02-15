import sys
import shutil


keywords = ["exit", "echo", "type"]

def echo(text: str):
    print(text)

def not_found(text: str):
    print(f"{text}: command not found")

def type(text: str):
    if text in keywords:
        print(f"{text} is a shell built in")
    # cho biet path den app thuc thi run if cmd (chuoi bdien tep) was called
    elif path := shutil.which(text):
        print(f"{text} is {path}")
    else:
        print(f"{text}: not found")


def main():
    # Wait for user input
    while True:
        # Display prompt
        sys.stdout.write("$ ")
        command = input()
        keyword, _, arguments = command.partition(" ")

        match command:
            case "exit 0":
                sys.exit(0)
            case command if keyword not in keywords:
                not_found(command)
                continue
            case command if keyword == "echo":
                echo(arguments)
            case command if keyword == "type":
                type(arguments)


if __name__ == "__main__":
    main()
