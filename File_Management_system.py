
import os

def create_file(file_name):
    file = open(file_name, 'w')
    print(f"File '{file_name}' created successfully.")
    file.close()

def read_file(file_name):
    file = open(file_name, 'r')
    content = file.read()
    print(f"Contents of '{file_name}':\n{content}")
    file.close()

def append_file(file_name, content):
    file = open(file_name, 'a')
    file.write(content + '\n')
    print(f"Content appended to '{file_name}' successfully.")
    file.close()

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    else:
        print(f"File '{file_name}' not found.")

while True:
    print("\nFile Management Menu:")
    print("1. Create File")
    print("2. Read File")
    print("3. Append to File")
    print("4. Delete File")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        file_name = input("Enter the file name: ")
        create_file(file_name)
    elif choice == '2':
        file_name = input("Enter the file name: ")
        read_file(file_name)
    elif choice == '3':
        file_name = input("Enter the file name: ")
        content = input("Enter content to append: ")
        append_file(file_name, content)
    elif choice == '4':
        file_name = input("Enter the file name: ")
        delete_file(file_name)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
