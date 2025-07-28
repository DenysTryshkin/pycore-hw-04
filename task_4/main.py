from chatbot import add_contact, change_contact, show_user_phone, get_contacts

command_hello = {"hello"}
command_add_username_phone = {"add username phone"}
command_change_user_name = {"change username phone"}
command_get_user_name = {"phone username"}
command_get_all_contacts = {"all"}
command_exit = {"close", "exit"}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_user_phone(args, contacts))
        elif command == "all":
            print(get_contacts(args, contacts))    
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
