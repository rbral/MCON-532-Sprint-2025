"""
File Operations Exercises
Fill in each section with appropriate code based on what you learned in class.
"""

import os
import glob
import json

# 5.1 Reading and Writing Text Files
def write_and_read_file():
    print("--- write_and_read_file() ---")
    # TODO: Write "Hello, Python Students!" to sample.txt
    with open("sample.txt", "w") as text_file:
        text_file.write("Hello, Python Students!")

    # TODO: Then read it and print the contents
    with open("sample.txt", "r") as text_file:
        content = text_file.read()
        print(content)
    pass

# 5.2 Creating and Listing Directory Structure
def create_and_list_directory():
    print("\n--- create_and_list_directory() ---")
    # TODO: Create a new folder called "practice_folder"
    os.makedirs("practice_folder", exist_ok=True)
    # TODO: List all files/folders in the current directory
    print("Contents of current directory:")
    print(os.listdir("."))
    # TODO: List contents of "practice_folder"
    print("Contents of 'practice_folder':")
    print(os.listdir("practice_folder"))
    pass

# 5.3 Globbing (Pattern Matching for File Names)
def list_files_with_glob():
    print("\n--- list_files_with_glob() ---")
    # TODO: List all .txt files in current folder
    txt_files = glob.glob("*.txt")
    print("Text files in current folder:")
    print(txt_files)
    # TODO: List all .py files in current folder
    py_files = glob.glob("*.py")
    print("Python files in current folder:")
    print(py_files)
    pass

# 5.4 open() Modes for Different Scenarios
def open_file_modes():
    print("\n--- open_file_modes() ---")
    # TODO: Append "This is an appended line.\n" to log.txt
    with open("log.txt", "a") as f:
        f.write("This is an appended line.\n")
        print("Successfully appended to log.txt.")
    # TODO: Write binary data to a file (e.g. bytes of 0, 1, 2)
    with open("output.bin", "wb") as f:
        f.write(b'\x00\x01\x02')
        print("Wrote binary data to binary_output.bin")
    # TODO: Read that binary file and print the content
    with open("output.bin", "rb") as f:
        data = f.read()
        print("binary file content: ", data)
    pass

# 5.4.1 Append to a Text File

def append_to_file():
    print("\n--- append_to_file() ---")
    # TODO: Append "This is an appended line.\n" to log.txt
    with open("log.txt", "a") as f:
        f.write("This is an appended line.\n")
    print("Successfully appended to log.txt.")

# 5.4.2 Binary Write and Read
def binary_write_and_read():
    print("\n--- binary_write_and_read() ---")
    # TODO: Write binary data to a file
    binary_data = b'\x00\x01\x02'
    with open("binary.txt", "wb") as f:
        f.write(binary_data)
    print("Wrote binary data to binary_output.bin")

    # TODO: Read that binary file and print the content
    with open("binary.txt", "rb") as f:
        data = f.read()
    print("Binary file contents:")
    print(data)

# 5.5 Streaming Large Files (Line by Line)
def stream_large_file():
    print("\n--- stream_large_file() ---")
    # TODO: Create a large file with 10 lines ( you can copy large_file.txt below)
    # TODO: Read and print each line using a for loop
    with open("large_file.txt", "r") as file:
        for line in file:
            print(line.strip())

# 5.6 Read File as String or Parse as JSON
def read_and_write_json():
    print("\n--- read_and_write_json() ---")
    # TODO: Write a dictionary {"course": "Python", "students": 20} to output.json
    # TODO: Read it back and print the result
    with open("output.json", "w") as file:
        json.dump({"course": "Python", "students": 20}, file)
        print("Wrote JSON: {'course': 'Python', 'students': 20}")

    with open("output.json", "r") as file:
        data = json.load(file)
        print("Read from output.json:")
        print(data)  # data is now a Python dict
    pass

# Run all exercises
if __name__ == "__main__":
    write_and_read_file()
    create_and_list_directory()
    list_files_with_glob()
    open_file_modes()
    stream_large_file()
    read_and_write_json()