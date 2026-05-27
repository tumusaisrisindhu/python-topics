from pathlib import Path

FILES_DIR = Path("files")


def list_files():
    print("\nAvailable Files:")

    for file in FILES_DIR.iterdir():
        if file.is_file():
            print("-", file.name)


def read_file(filename):

    filepath = FILES_DIR / filename

    try:
        with open(filepath, "r") as file:
            print("\nFile Content:\n")
            print(file.read())

    except FileNotFoundError:
        print("File not found")


def write_file(filename, content):

    filepath = FILES_DIR / filename

    with open(filepath, "w") as file:
        file.write(content)

    print("File written successfully")


def append_file(filename, content):

    filepath = FILES_DIR / filename

    with open(filepath, "a") as file:
        file.write("\n" + content)

    print("Content appended")


def delete_file(filename):

    filepath = FILES_DIR / filename

    if filepath.exists():
        filepath.unlink()
        print("File deleted")
    else:
        print("File not found")


def menu():

    while True:

        print("\n===== FILE MANAGER =====")
        print("1. List Files")
        print("2. Read File")
        print("3. Write File")
        print("4. Append File")
        print("5. Delete File")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            list_files()

        elif choice == "2":
            filename = input("File name: ")
            read_file(filename)

        elif choice == "3":
            filename = input("File name: ")
            content = input("Content: ")
            write_file(filename, content)

        elif choice == "4":
            filename = input("File name: ")
            content = input("Content: ")
            append_file(filename, content)

        elif choice == "5":
            filename = input("File name: ")
            delete_file(filename)

        elif choice == "6":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()