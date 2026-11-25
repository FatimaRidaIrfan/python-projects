from pathlib import Path 

folder = Path(__file__).parent

while True:
    print("==== File Management System ====")
    print("1. View files and folders")
    print("2. Create a folder")
    print("3. Create a text file")
    print("4. Rename a file")
    print("5. Delete a file")
    print("6. Delete a folder")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        for item in folder.iterdir():
            print(item.name)

    elif choice == "2":
        folder_name = input("Enter folder name: ")

        new_folder = folder / folder_name
        if new_folder.exists():
            print("Folder already exists!")
        else:
            new_folder.mkdir()
            print("Folder created successfully!")

    elif choice == "3":
        file_name = input("Enter file name:")

        if not file_name.endswith(".txt"):
            file_name += ".txt"

        new_file = folder / file_name

        if new_file.exists():
            print("File already exists!")
        else:
            new_file.write_text("Hello Python!")
            print("File created successfully!")

    elif choice == "4":
        existing_file = input("Enter existing file name: ")
        new_filename = input("Enter new file name: ")

        old_file = folder / existing_file
        new_file = folder / new_filename

        if old_file.is_file():
            if new_file.exists():
                print("A file or folder with that name already exists!")
            else:
                old_file.rename(new_file)
                print("File renamed successfully!")
        else:
            print("File not found!")

    elif choice == "5":
        delete_file = input("Enter file name to delete: ")

        old_file = folder / delete_file
        if old_file.is_file():
            old_file.unlink()
            print("File deleted successfully!")
        else:
            print("File not found!")

    elif choice == "6":
        delete_folder = input("Enter folder name to delete: ")

        old_folder = folder / delete_folder
        if old_folder.is_dir():
            old_folder.rmdir()
            print("Folder deleted successfully!")
        else:
            print("Folder not found!")

    elif choice == "7":
        print("Exiting File Management System")
        break 
    else:
        print("Invalid choice")

