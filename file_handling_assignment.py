# file_handling_assignment.py

def create_and_write_file():
    try:
        # Create and write to the file
        with open('my_file.txt', 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("Here is the second line, including a number: 123.\n")
            file.write("And this is the third line with some more text.\n")
        print("File created and initial content written.")
    except (PermissionError, IOError) as e:
        print(f"Error occurred while writing the file: {e}")
    finally:
        print("Finished file creation and writing process.")

def read_and_display_file():
    try:
        # Read and display the file content
        with open('my_file.txt', 'r') as file:
            content = file.read()
        print("\nFile content after initial writing:")
        print(content)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except PermissionError as e:
        print(f"Permission denied: {e}")
    finally:
        print("Finished reading the file.")

def append_to_file():
    try:
        # Append more lines to the file
        with open('my_file.txt', 'a') as file:
            file.write("Appending a new line with some text.\n")
            file.write("Another appended line with different content.\n")
            file.write("And one more line to conclude the appending.\n")
        print("Additional lines appended to the file.")
    except (PermissionError, IOError) as e:
        print(f"Error occurred while appending to the file: {e}")
    finally:
        print("Finished appending process.")

def main():
    create_and_write_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()

if __name__ == "__main__":
    main()
