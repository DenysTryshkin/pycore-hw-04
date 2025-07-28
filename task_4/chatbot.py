def add_contact(args, contacts):
    if len(args) < 2:
        return f"Not enough values to unpack (expected 2, got {len(args)})"
    name, phone = args
    contacts[name] = phone
    return "Contact added."
    

def change_contact(args, contacts):
    if len(args) < 2:
        return f"Error: please provide both name and phone."
    name, phone = args
    if name not in contacts:
      return f"Error: '{name}' not found"
    contacts[name] = phone
    return f"Contact updated."


def show_user_phone(args, contacts):
    if len(args) < 1:
        return f"Error: please provide a name"
    name = args[0]
    if name not in contacts:
        return f"Error: {name} not found"
    return contacts[name]


def get_contacts(args, contacts):
    if not contacts:
        return f"No contacts saved"
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)