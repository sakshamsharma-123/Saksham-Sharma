import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File name {filename} created successfully!")

    except FileExistsError:
        print(f"File name {filename} already exits!")

    except Exception as E:
        print("Oops! An error occured.")

def view_all():
    files = os.listdir() 
    if not files:
        print("No file found!")
    else:
        print("Files in directory:\n")
        for file in files:
            print(file)
            
def del_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occured")

def read_file(filename):
    try:
        with open(f'{filename}', 'r') as f:
            content = f.read( )
        print(f"Content of {filename}:\n{content}")
    
    except FileNotFoundError:
        print(f"{filename} not found!")

    except Exception as e:
        print("An error occured")

def edit_file(filename):
    try:
        with open(f'{filename}', 'a') as f:
            content = input("Enter data to be added: ")
            f.write(content + '\n')
            print(f"{content} added to {filename}")

    except FileNotFoundError:
        print(f"{filename} not found!")

    except Exception as e:
        print("An error occured!")

def main():
    while True:
        print("\n\nFILE MANAGEMENT APP")
        print("___________________")
        print("1: Create a file")
        print("2: View all files")
        print("3: Delete a file")
        print("4: Read a file")
        print("5: Add content to a file")
        print("6: Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            filename = input("Enter the name of the file: ")
            create_file(filename)

        elif choice == '2':
            view_all()

        elif choice == '3':
            filename = input("Enter filename to be removed: ")
            del_file(filename)

        elif choice == '4':
            filename = input("Enter filename to read: ")
            read_file(filename)

        elif choice == '5':
            filename = input("Enter filename to add data: ")
            edit_file(filename)

        elif choice == '6':
            print("Closing the app...")
            break

        else:
            print("Invalid Input. Please enter (1-6)")

if __name__ == '__main__':
    main()

