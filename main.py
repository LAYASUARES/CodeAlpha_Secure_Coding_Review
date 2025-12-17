from database import create_table, add_user, search_user
from file_handler import read_file
from system_utils import run_command

def menu():
    print("""
=== Vulnerable Application ===
1. Add user
2. Search user
3. Read file
4. Run system command
5. Exit
""")

def main():
    create_table()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Username: ")
            email = input("Email: ")
            add_user(username, email)
            print("User added!\n")

        elif choice == "2":
            term = input("Search for username: ")
            results = search_user(term)
            print("Results:", results, "\n")

        elif choice == "3":
            filename = input("File to read: ")
            content = read_file(filename)
            print(content, "\n")

        elif choice == "4":
            cmd = input("Command to run: ")
            output = run_command(cmd)
            print(output, "\n")

        elif choice == "5":
            break

        else:
            print("Invalid option\n")

if __name__ == "__main__":
    main()
