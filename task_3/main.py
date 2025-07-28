import sys
from colorama import Fore
from pathlib import Path

def show_directory(directory_path, indent=0):
    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"The specified path '{directory_path}' does not exist or is not a directory.")
        return
    
    print(" " * indent +Fore.BLUE + f"📁 {path.name}/")

    for item in path.iterdir():
        if item.is_dir():
            show_directory(item, indent=indent + 4)

        elif item.is_file():
            print(" " * (indent + 2) + Fore.GREEN + f"📄 {item.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Please specify the path to the directory.")
        sys.exit(1)

    directory_path = sys.argv[1]

    show_directory(directory_path)

