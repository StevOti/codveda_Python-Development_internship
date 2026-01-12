# Task 3: Word Counter
# Description: Create a Python program that reads a
# text file and counts the number of words in it.

# Objectives:
# 1. Read a text file.
# 2. Split the content into words and count them.
# 3. Handle exceptions, such as file not found.

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        return "Error: The file was not found."
    except Exception as e:
        return f"An error occurred: {e}"
    
if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    result = count_words(file_path)
    print(f"Word Count: {result}")